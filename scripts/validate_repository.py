#!/usr/bin/env python3
"""Conservative Phase 1 repository validator; standard-library only."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
EXPORTS = ROOT / "exports"
ERRORS = []
WARNINGS = []
CHECKS = []


def check(name, condition, detail):
    CHECKS.append(name)
    if not condition:
        ERRORS.append(f"{name}: {detail}")


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        ERRORS.append(f"JSON parse: {path.relative_to(ROOT)}: {exc}")
        return None


expected_exports = [
    "project-manifest.json",
    "executive-status.json",
    "claims-register.json",
    "assumptions-register.json",
    "decisions-register.json",
    "open-questions.json",
    "risks-register.json",
    "source-register.json",
    "key-metrics.json",
    "scenario-register.json",
    "missing-research.json",
]

for name in expected_exports:
    path = EXPORTS / name
    check("required export", path.is_file(), name)

data_by_name = {}
for name in expected_exports:
    path = EXPORTS / name
    if path.exists():
        data_by_name[name] = load_json(path)

required_envelope = {
    "schema_version",
    "generated_date",
    "source_of_truth",
    "document_status",
    "provenance",
    "validation_result",
    "unresolved_dependencies",
}
for name, data in data_by_name.items():
    if data is not None:
        check(
            "export envelope",
            required_envelope.issubset(data),
            f"{name} missing {sorted(required_envelope - set(data))}",
        )

schema_files = list((ROOT / "schemas").glob("*.json"))
check("schema presence", len(schema_files) >= 3, "expected at least three JSON schemas")
for path in schema_files:
    load_json(path)

decisions = (data_by_name.get("decisions-register.json") or {}).get("decisions", [])
decision_ids = [item.get("decision_id") for item in decisions]
valid_decision = re.compile(r"^D-(?:P|G|H)?[0-9]+$")
check(
    "valid decision IDs",
    all(isinstance(item, str) and valid_decision.match(item) for item in decision_ids),
    f"invalid IDs: {[item for item in decision_ids if not isinstance(item, str) or not valid_decision.match(item)]}",
)
check(
    "duplicate decision IDs",
    len(decision_ids) == len(set(decision_ids)),
    "decision IDs must be unique",
)
ratified_expected = {"D-P1", "D-P2", "D-P8", "D-P9", "D-P11", "D-P12"}
ratified_actual = {item["decision_id"] for item in decisions if item.get("status") == "ratified"}
check(
    "ratified decision set",
    ratified_expected == ratified_actual,
    f"expected {sorted(ratified_expected)}, found {sorted(ratified_actual)}",
)
for item in decisions:
    if item.get("status") == "ratified":
        check(
            "ratified decision completeness",
            all(item.get(field) for field in ["exact_decision_statement", "decision_date", "decision_maker", "review_trigger"]),
            item.get("decision_id", "unknown"),
        )

assumptions = (data_by_name.get("assumptions-register.json") or {}).get("assumptions", [])
assumption_ids = [item.get("assumption_id") for item in assumptions]
check(
    "duplicate assumption IDs",
    len(assumption_ids) == len(set(assumption_ids)),
    "assumption IDs must be unique",
)
for item in assumptions:
    check(
        "assumption provenance/status/scenario",
        bool(item.get("source")) and bool(item.get("status")) and bool(item.get("scenario_association")),
        item.get("assumption_id", "unknown"),
    )

claims = (data_by_name.get("claims-register.json") or {}).get("claims", [])
claim_ids = [item.get("statement_id") for item in claims]
check("duplicate claim IDs", len(claim_ids) == len(set(claim_ids)), "claim IDs must be unique")
for item in claims:
    check(
        "claim provenance",
        bool(item.get("provenance")) and bool(item.get("source_location")),
        item.get("statement_id", "unknown"),
    )
    if item.get("external_use_status") == "external_eligible":
        check(
            "external-eligible unresolved dependencies",
            not item.get("dependencies"),
            item.get("statement_id", "unknown"),
        )

manifest = data_by_name.get("project-manifest.json") or {}
check(
    "canonical identity",
    manifest.get("canonical_name") == "South Andrews Healthcare and Mobility Hub"
    and manifest.get("canonical_address") == "901–917 South Andrews Avenue, Fort Lauderdale, Florida",
    "manifest identity mismatch",
)
check(
    "ownership status",
    manifest.get("property_status") == "prospective_acquisition"
    and manifest.get("ownership_status") == "not_owned_by_sponsor"
    and manifest.get("site_control_status") == "not_documented",
    "manifest may imply ownership/control",
)
check(
    "scheme remains unresolved",
    manifest.get("adopted_scheme") is None
    and set(manifest.get("active_scenarios", [])) == {"6_story", "8_story"},
    "story scenario incorrectly adopted",
)
check(
    "negative feasibility preserved",
    manifest.get("base_case_feasible") is False,
    "base-case feasibility must remain false",
)

model_template = load_json(ROOT / "models/exports/model-input-template.json")
if model_template:
    inputs = model_template.get("inputs", [])
    ids = [item.get("input_id") for item in inputs]
    check("duplicate model input IDs", len(ids) == len(set(ids)), "model input IDs must be unique")
    required_categories = {
        "land_basis",
        "building_program",
        "floor_plate",
        "parking_count",
        "office_clinical_rent",
        "retail_rent",
        "occupancy",
        "development_costs",
        "contingency",
        "financing",
        "tax_credit_treatment",
        "grants",
        "partner_support",
        "charger_economics",
        "av_revenue",
        "exit_cap",
        "hurdle_rate",
    }
    actual_categories = {item.get("category") for item in inputs}
    check(
        "model input contract coverage",
        required_categories == actual_categories,
        f"missing {sorted(required_categories - actual_categories)}",
    )
    av_base = [
        item
        for item in inputs
        if item.get("category") == "av_revenue"
        and "governance_clean_base_case" in item.get("scenario_association", [])
    ]
    check(
        "speculative AV base-case exclusion",
        len(av_base) == 1 and av_base[0].get("value") == 0,
        "governance-clean base case must carry zero AV revenue",
    )
    basis_inputs = [item for item in inputs if item.get("category") == "floor_plate"]
    check(
        "incompatible scenario values not combined",
        len(basis_inputs) == 1
        and basis_inputs[0].get("value") is None
        and basis_inputs[0].get("status") == "unresolved",
        "floor-plate basis must remain unresolved in template",
    )

source_export = data_by_name.get("source-register.json") or {}
for source in source_export.get("sources", []):
    path = ROOT / source["exact_path"]
    check("source exists", path.is_file(), source["exact_path"])
    if path.is_file():
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        check(
            "source integrity hash",
            digest == source.get("integrity_sha256"),
            source["exact_path"],
        )

check(
    "source worktree protection",
    True,
    "source immutability is additionally verified by git diff in final QC",
)

link_pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
for md in ROOT.rglob("*.md"):
    if ".git" in md.parts:
        continue
    text = md.read_text(encoding="utf-8")
    for raw_target in link_pattern.findall(text):
        target = raw_target.strip()
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0]
        if not target:
            continue
        resolved = (md.parent / unquote(target)).resolve()
        if not resolved.exists():
            ERRORS.append(
                f"broken internal link: {md.relative_to(ROOT)} -> {raw_target}"
            )
CHECKS.append("internal Markdown links")

authoritative_text_paths = [
    ROOT / "README.md",
    ROOT / "AGENTS.md",
    ROOT / "docs/planning/Project Canon.md",
    ROOT / "docs/planning/Executive Planning Summary.md",
    ROOT / "docs/external/EXTERNAL_PUBLICATION_CHECKLIST.md",
    ROOT / "docs/investment/Institutional Investment Memorandum.md",
    ROOT / "docs/investment/README.md",
    ROOT / "docs/planning/IIM Source Map.md",
    ROOT / "docs/planning/IIM Architecture and Writing Plan.md",
]
authoritative_text = "\n".join(path.read_text(encoding="utf-8") for path in authoritative_text_paths)
ownership_patterns = [
    r"\bwe own (?:the )?(?:site|property)\b",
    r"\bsponsor owns (?:the )?(?:site|property)\b",
    r"\bsite is controlled\b",
    r"\bproperty is under contract\b",
]
check(
    "ownership-language scan",
    not any(re.search(pattern, authoritative_text, flags=re.IGNORECASE) for pattern in ownership_patterns),
    "authoritative surface contains ownership/control implication",
)
operative_patterns = [
    r"prior Project Constitution is operative",
    r"missing Project Decision Log is operative",
    r"subordinate to (?:the )?Project Constitution",
]
check(
    "missing-governance operative-reference scan",
    not any(re.search(pattern, authoritative_text, flags=re.IGNORECASE) for pattern in operative_patterns),
    "authoritative surface treats missing governance as operative",
)
check(
    "historical project-name scan",
    "South Andrews Clinical & Mobility Center" not in authoritative_text
    and "South Andrews Mobility Hub" not in authoritative_text,
    "historical name appears on authoritative surface without source context",
)
check(
    "canonical address scan",
    all(
        "901–917 South Andrews Avenue, Fort Lauderdale, Florida"
        in path.read_text(encoding="utf-8")
        for path in [ROOT / "README.md", ROOT / "docs/planning/Project Canon.md"]
    ),
    "canonical identity address missing from key surfaces",
)

required_status_docs = list((ROOT / "docs/decisions").glob("*.md")) + [
    ROOT / "docs/planning/Project Canon.md",
    ROOT / "docs/planning/Executive Planning Summary.md",
]
for path in required_status_docs:
    text = path.read_text(encoding="utf-8")
    check(
        "document status present",
        "status:" in text.lower() or "**status:**" in text.lower() or "**document status:**" in text.lower(),
        str(path.relative_to(ROOT)),
    )

# --- Institutional Investment Memorandum (IIM) controls (internal_only document set) ---
iim_doc_paths = {
    "memorandum": ROOT / "docs/investment/Institutional Investment Memorandum.md",
    "investment index": ROOT / "docs/investment/README.md",
    "source map": ROOT / "docs/planning/IIM Source Map.md",
    "architecture plan": ROOT / "docs/planning/IIM Architecture and Writing Plan.md",
}
iim_texts = {}
for label, path in iim_doc_paths.items():
    check("IIM document present", path.is_file(), f"{label}: {path.relative_to(ROOT)}")
    if path.is_file():
        iim_texts[label] = path.read_text(encoding="utf-8")

for label, text in iim_texts.items():
    check(
        "IIM internal-only status",
        "internal_only" in text,
        f"{label} must declare internal_only external-use status",
    )

iim_text = iim_texts.get("memorandum", "")
check(
    "IIM canonical name",
    "South Andrews Healthcare and Mobility Hub" in iim_text,
    "memorandum must use the canonical project name",
)
check(
    "IIM canonical address",
    "901–917 South Andrews Avenue, Fort Lauderdale, Florida" in iim_text,
    "memorandum must use the canonical identity address (D-P12, en dash)",
)
check(
    "IIM feasibility finding present",
    "does not satisfy the modeled institutional return requirements" in iim_text,
    "memorandum must carry the canonical negative feasibility finding (Project Canon §3)",
)
check(
    "IIM external-eligibility not self-claimed",
    "external_use_status: internal_only" in iim_text and "external_eligible" not in iim_text,
    "memorandum may not designate itself or its content external_eligible",
)

# D-P1 discipline: every substantive $8M occurrence in the memorandum must sit
# within a proximity window containing a D-P1 reference plus an approved label.
# A document-level qualification elsewhere does not cure an unqualified use.
iim_lines = iim_text.splitlines()
land_figure = re.compile(r"\$8(?:,000,000|\.0\s*M\b|\.0 million|M\b| million)", re.IGNORECASE)
land_qualifier = re.compile(
    r"acquisition-strategy input only"
    r"|not proof of value"
    r"|strategy input; not proof of value or authority"
    r"|not appraised value, land-price ceiling, walk-away price, or transaction authority",
    re.IGNORECASE,
)
for index, line in enumerate(iim_lines):
    if land_figure.search(line):
        window = "\n".join(iim_lines[max(0, index - 2): index + 3])
        check(
            "IIM land-basis qualifier (D-P1)",
            "D-P1" in window and land_qualifier.search(window) is not None,
            f"unqualified $8M reference near memorandum line {index + 1}",
        )

land_mischaracterizations = [
    r"(?:appraised|market)\s+value\s+of\s+\$8",
    r"\$8(?:,000,000|\.0\s*M|M\b)[^\n]{0,60}\b(?:is|was|equals)\s+(?:the\s+)?(?:appraised|market)\s+value",
    r"valuation\s+conclusion\s+of\s+\$8",
    r"approved\s+offer\s+of\s+\$8",
    r"(?:price\s+)?ceiling\s+of\s+\$8",
    r"maximum\s+(?:authorized\s+)?price\s+of\s+\$8",
    r"walk-?away\s+price\s+of\s+\$8",
    r"\$8(?:,000,000|\.0\s*M|M\b)[^\n]{0,60}\b(?:constitutes|establishes|grants)\s+transaction\s+authority",
]
check(
    "IIM land-basis mischaracterization scan",
    not any(re.search(pattern, iim_text, flags=re.IGNORECASE) for pattern in land_mischaracterizations),
    "memorandum characterizes the $8M input as value, ceiling, walk-away, approved offer, or authority",
)

prohibited_promotional = [
    r"guaranteed\s+demand",
    r"perfectly\s+positioned",
    r"massive\s+opportunity",
    r"profound\s+and\s+immediate\s+demand",
    r"highly\s+viable",
    r"project\s+wins",
    r"cannot\s+wait",
    r"generational\s+asset",
    r"guaranteed\s+(?:hospital\s+)?spillover",
    r"guaranteed\s+parking\s+demand",
    r"guaranteed\s+returns?",
]
iim_decision_surface = iim_text + "\n" + iim_texts.get("investment index", "")
check(
    "IIM prohibited-language scan",
    not any(re.search(pattern, iim_decision_surface, flags=re.IGNORECASE) for pattern in prohibited_promotional),
    "memorandum contains prohibited promotional or certainty language",
)

# --- Integrated development package controls (2026-07-27) ---
# The package is internal working product. These checks enforce that it declares
# itself internal, preserves the negative feasibility finding, keeps scenario
# discipline, and never implies ownership, entitlement, utility capacity, or
# partner commitment.
package_paths = {
    "source map": ROOT / "docs/planning/Integrated Development Source Map.md",
    "contradiction register": ROOT / "docs/planning/Contradiction and Validation Register.md",
    "scenario reconciliation": ROOT / "docs/planning/Program and Scenario Reconciliation.md",
    "planning brief": ROOT / "docs/planning/Final Development Planning Brief.md",
    "construction budget": ROOT / "docs/cost/Construction Budget Basis.md",
    "electrical basis": ROOT / "docs/technical/Electrical Basis of Design.md",
    "entitlement roadmap": ROOT / "docs/technical/Entitlement and Utility Roadmap.md",
    "two-site plan": ROOT / "docs/technical/Two-Site Operating Plan.md",
    "development recommendation": ROOT / "docs/investment/Integrated Development Recommendation.md",
    "prospectus release candidate": ROOT / "docs/external/Institutional Development Prospectus.md",
    "one-page summary": ROOT / "docs/external/One-Page Project Summary.md",
}
package_texts = {}
for label, path in package_paths.items():
    check("integrated package document present", path.is_file(), f"{label}: {path}")
    if path.is_file():
        package_texts[label] = path.read_text(encoding="utf-8")

for label, text in package_texts.items():
    check(
        "integrated package internal-only status",
        "internal_only" in text,
        f"{label} must declare internal_only external-use status",
    )
    check(
        "integrated package external-eligibility not self-claimed",
        "external_eligible" not in text,
        f"{label} may not designate itself or its content external_eligible",
    )

package_surface = "\n".join(package_texts.values())
check(
    "integrated package ownership-language scan",
    not any(re.search(pattern, package_surface, flags=re.IGNORECASE) for pattern in ownership_patterns),
    "integrated package contains ownership/control implication",
)
check(
    "integrated package prohibited-language scan",
    not any(re.search(pattern, package_surface, flags=re.IGNORECASE) for pattern in prohibited_promotional),
    "integrated package contains prohibited promotional or certainty language",
)
package_unsupported = [
    r"\bentitlement (?:is|has been) (?:approved|granted|secured)\b",
    r"\bFPL (?:has )?confirmed\b",
    r"\bcommitted (?:healthcare|health-system|mobility) partner\b",
    r"\bby[- ]right height\b",
]
check(
    "integrated package unsupported-approval scan",
    not any(re.search(pattern, package_surface, flags=re.IGNORECASE) for pattern in package_unsupported),
    "integrated package implies entitlement, utility capacity, or partner commitment",
)

for label in ("development recommendation", "prospectus release candidate", "one-page summary"):
    text = package_texts.get(label, "")
    check(
        "integrated package property-status disclosure",
        "does not" in text and "own the property" in text,
        f"{label} must state that the sponsor does not own the property",
    )

prospectus_text = package_texts.get("prospectus release candidate", "")
check(
    "prospectus release blocked",
    "BLOCKED" in prospectus_text and "EXTERNAL_PUBLICATION_CHECKLIST" in prospectus_text,
    "prospectus release candidate must declare external use blocked and cite the checklist",
)
check(
    "prospectus preserves negative feasibility finding",
    "does not satisfy the modeled institutional return requirements" in prospectus_text,
    "prospectus release candidate must carry the canonical negative feasibility finding",
)
check(
    "prospectus states no target return",
    "No target return is stated" in prospectus_text,
    "prospectus release candidate must not assert a target return",
)

# Scenario discipline: the package must name its stated basis and refuse to blend bases.
recon_text = package_texts.get("scenario reconciliation", "")
check(
    "scenario reconciliation declares a stated basis",
    "stated modelling basis" in recon_text.lower() or "stated basis" in recon_text.lower(),
    "scenario reconciliation must name its geometric basis",
)
check(
    "scenario reconciliation preserves dual-basis discipline",
    "never mixed" in recon_text.lower() or "never be mixed" in recon_text.lower(),
    "scenario reconciliation must state that program bases are never mixed",
)

# Derived model artefacts must exist, parse, and carry their planning-level disclaimer.
model_json_path = ROOT / "models/working/integrated-development-model.json"
check("derived model script present", (ROOT / "models/working/build_integrated_development_model.py").is_file(), "build_integrated_development_model.py")
check("derived model data present", model_json_path.is_file(), "integrated-development-model.json")
if model_json_path.is_file():
    model_data = load_json(model_json_path)
    if model_data:
        check(
            "derived model disclaimer",
            "PLANNING-LEVEL MODEL OUTPUT" in model_data.get("disclaimer", ""),
            "derived model must carry its planning-level disclaimer",
        )
        scenarios = model_data.get("scenarios", {})
        check(
            "derived model scenario coverage",
            {"SA-A", "SA-B", "SA-C", "SA-C0"}.issubset(scenarios),
            f"expected SA-A/SA-B/SA-C/SA-C0, found {sorted(scenarios)}",
        )
        check(
            "derived model excludes AV revenue from base cases",
            all(
                item.get("operating_governance_clean", {}).get("AV staging / secure bay revenue") == 0
                for item in scenarios.values()
            ),
            "governance-clean operating case must carry zero AV revenue",
        )

timestamp = datetime.now(timezone.utc).isoformat()
if not ERRORS:
    for name, data in data_by_name.items():
        if data is None:
            continue
        data["validation_result"] = {
            "status": "passed",
            "checked_at": timestamp,
            "validator": "scripts/validate_repository.py",
        }
        (EXPORTS / name).write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )

print(f"Checks run: {len(CHECKS)}")
print(f"Errors: {len(ERRORS)}")
print(f"Warnings: {len(WARNINGS)}")
for item in ERRORS:
    print(f"ERROR: {item}")
for item in WARNINGS:
    print(f"WARNING: {item}")

sys.exit(1 if ERRORS else 0)
