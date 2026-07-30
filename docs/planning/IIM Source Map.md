---
title: "IIM Source Map"
document_status: current
scenario_status: current
source_provenance: repository_authored
verification_status: unverified
external_use_status: internal_only
date_last_reviewed: 2026-07-26
governing_sources:
  - AGENTS.md
  - docs/governance/SOURCE_AUTHORITY.md
  - docs/governance/CLAIMS_AND_EVIDENCE_POLICY.md
  - docs/planning/Project Canon.md
dependencies:
  - docs/planning/Contradictions Matrix.md
  - docs/planning/Open Questions.md
  - docs/planning/Missing Research Register.md
supersedes: []
superseded_by: []
---

# IIM Source Map

**Status:** current · **Last reviewed:** 2026-07-26 · **External-use status:** internal_only
**Related:** [IIM Architecture and Writing Plan](IIM%20Architecture%20and%20Writing%20Plan.md) · [Project Canon](Project%20Canon.md) · [Contradictions Matrix](Contradictions%20Matrix.md) · [Source Authority Register](Source%20Authority%20Register.md)

This document maps every chapter of the planned [Institutional Investment Memorandum](../investment/Institutional%20Investment%20Memorandum.md) (IIM) to its governing sources, canon statements, decisions, register entries, prohibited assertions, and current drafting status. It is a Stage 1 audit artifact: mapping only, no persuasive prose. The IIM itself is an **internal** investment-committee document; it is not the gated Prospectus vNext (Document Update Order Step 8) and does not satisfy the [External Publication Checklist](../external/EXTERNAL_PUBLICATION_CHECKLIST.md).

## 1. Drafting-status vocabulary

Each chapter carries one primary drafting classification:

- **verified analysis** — restates documented record facts or verified-fact-class evidence with provenance.
- **qualified analysis** — analysis on source-derived claims, working assumptions, or model outputs, written with the required caveats.
- **scenario analysis** — presents unadopted alternatives (dual bases, 6- vs 8-story, charger mixes) without selecting one.
- **placeholder pending research** — the evidence does not exist in the repository; the chapter states the gap and the study that fills it.
- **not yet suitable for publication** — internal drafting is possible, but no external use of the chapter's content is permitted before the Step 8 gates.

Every chapter of the IIM is `internal_only`; the last classification therefore additionally applies, in whole, to the external question. Register ID vocabularies used below: `CAN-###` canon statements · `D-P#` decisions · `OQ-##` open questions · `R-#` risks · `S1`–`S8` sources · `MA-##`/`MB-##` missing documents/studies · assumption IDs per [Master Assumption Register](Master%20Assumption%20Register.md) (`SITE-`, `ZON-`, `ACQ-`, `PRG-`, `CST-`, `FIN-`, `REV-`, `EXT-`, `NRG-`, `HC-`, `MOB-`).

## 2. Chapter-by-chapter source map

### Chapters 1–3 — Executive and thesis layer

| Ch | Chapter | Governing sources | Canon / decisions | Registers | Prohibited or unsafe assertions | External verification needed | Drafting status |
|---|---|---|---|---|---|---|---|
| 1 | Executive Decision Summary | [Executive Planning Summary](Executive%20Planning%20Summary.md); [Project Canon](Project%20Canon.md) §§1–3, 7 | CAN-001…004, CAN-020…022; D-P1, D-P2 | OQ-14/15/17/18/20; R-13; MB-01/02/03/07/13 | Any implied feasibility, transaction authority, or readiness beyond the readiness table | None for drafting; all §6 gates for external use | qualified analysis |
| 2 | Investment Thesis | D-P2 record; [Canonical Healthcare Strategy](Canonical%20Healthcare%20Strategy.md) | CAN-010…013; D-P2 | HC-01…11; MB-07/08/17; MA-07 | "Guaranteed demand"; spillover certainty; mobility-led framing | MB-07, MB-17, MA-07 recovery | qualified analysis |
| 3 | Project Definition and Strategic Positioning | AGENTS.md identity/scope; [Current Project Scope](Current%20Project%20Scope.md); PROJECT_GLOSSARY.md | CAN-001, CAN-002, CAN-010, CAN-011; D-P2, D-P12 | SITE-16/17; scenario register (rejected concepts) | Historical names as active; residential/hotel/rental-car framing as current | None (definitional) | verified analysis (of the record) with qualified positioning |

### Chapters 4–6 — Site, transaction, entitlement

| Ch | Chapter | Governing sources | Canon / decisions | Registers | Prohibited or unsafe assertions | External verification needed | Drafting status |
|---|---|---|---|---|---|---|---|
| 4 | Property and Site | S6 (site facts within appraisal scope); S8; S1 §1; [Source Authority Register](Source%20Authority%20Register.md) rows 4–6, 8 | CAN-002; Canon §6; D-P12 | SITE-01…17; MA-10 (survey); MB-10 | Site control; clean title/environmental condition; verified BFE | Survey update (MB-10); title; geotech (MB-06) | verified analysis (site facts) with caveats |
| 5 | Transaction Context and Land Basis | D-P1 record; S1 §§4, 8; S6 (value opinion); S7 (residuals); S8 p.7 | CAN-003, CAN-004; D-P1 | ACQ-01…09; OQ-20; R-16; MB-19; MA-18 | $8.0M as value, ceiling, walk-away, or authority; $11.1M as market-clearing fact; any offer/contract implication | Owner authority decision (OQ-20); MB-19 memo | qualified analysis |
| 6 | Regulatory and Entitlement Context | S6 zoning section; S8 p.4; S1 §5; S4 zoning table (subordinate) | Canon §6 | ZON-01…09; OQ-03/11; R-5; MB-01, MB-18; MA-09/15 | "By right" height above six stories; approved entitlement; confirmed FAR | Zoning Verification Letter + pre-application (MB-01); counsel (MB-18) | qualified analysis (working statement only) |

### Chapters 7–9 — Demand theses

| Ch | Chapter | Governing sources | Canon / decisions | Registers | Prohibited or unsafe assertions | External verification needed | Drafting status |
|---|---|---|---|---|---|---|---|
| 7 | Healthcare Demand Thesis | [Canonical Healthcare Strategy](Canonical%20Healthcare%20Strategy.md); S4/S5 (SD via missing MA-07) | CAN-013 (blocked_pending_resolution) | HC-01…05, HC-08; OQ-08; MB-07/08/17; MA-07 | Displacement, parking deficit, guaranteed spillover, endorsement; demand claims without the 10.4% vacancy counterweight (HC-05) | MB-17 (Broward facts); MA-07 recovery; MB-07 | qualified analysis |
| 8 | Medical Office and Med-Tail Market | [Canonical Financial Assumptions](Canonical%20Financial%20Assumptions.md) §2; S2/S3 rent inputs | — (D-P6 pending — not authority) | REV-01 (DUAL), REV-03; OQ-15; MB-07; HC-07 | Either rent value as validated; S2's "FACT" tag; blended/averaged rents | MB-07 rent comps and absorption | scenario analysis + placeholder pending research |
| 9 | Parking and Mobility Thesis | [Canonical Mobility Strategy](Canonical%20Mobility%20Strategy.md); S4 (shared-parking logic) | CAN-011, CAN-031; D-P2 | REV-04/05/06/07; MOB-01…05; OQ-16/21/22; MB-09/15; MA-16 | Guaranteed parking demand; AV service/partners/revenue; charger economics as validated | Parking study (MB-09); FPL (MB-03); operator evidence (MB-15) | qualified analysis (parking) + scenario analysis (mobility optionality) |

### Chapters 10–14 — Program, infrastructure, delivery

| Ch | Chapter | Governing sources | Canon / decisions | Registers | Prohibited or unsafe assertions | External verification needed | Drafting status |
|---|---|---|---|---|---|---|---|
| 10 | Development Program Alternatives | [Current Development Program](Current%20Development%20Program.md); scenario register | Canon §5; CAN-030…034 | PRG-01…15 (DUAL family); OQ-14; R-15; MB-02 | Presenting either basis as adopted; mixing bases; any single stall/GBA/RSF figure without basis label | Test-fit (MB-02); D-P5 | scenario analysis |
| 11 | Test-Fit and Massing Requirements | [Current Development Program](Current%20Development%20Program.md) §§3, 5; S3 circulation notes; S8 massing | CAN-030; D-P3 (pending — not authority) | PRG-08/11; OQ-02/05/10; MB-02/04 | Implying validated circulation, stall efficiency, or ingress/egress | Test-fit brief (MB-02); traffic study (MB-04) | qualified analysis (requirements statement) |
| 12 | Infrastructure and Utility Strategy | [Canonical Infrastructure Strategy](Canonical%20Infrastructure%20Strategy.md); S3 `Energy & Mobility` | CAN-031, CAN-034 | NRG-01…10; CST-08…13, CST-16/17; OQ-04/21; MB-03; MA-11 | Confirmed FPL/utility capacity; "data center" language; solar/BESS sizing as decided | FPL will-serve/load study (MB-03); recover MA-11 | qualified analysis; utility capacity placeholder pending research |
| 13 | Flood, Resilience, Environmental, and Insurance | S6 p.28 (Zone AE — verified); [Canonical Infrastructure Strategy](Canonical%20Infrastructure%20Strategy.md) §§5–6 | Canon §6 | SITE-07/08/11; R-1, R-18; MB-05/06/11/12; MA-13 | Environmental condition claims (blocked — no reports in repo); quantified insurance costs | Phase I ESA recovery + refresh (MA-13/MB-11); geotech (MB-06); insurance quotes (MB-12) | verified (flood zone) + placeholder pending research (environmental, insurance) |
| 14 | Construction and Delivery Strategy | [Canonical Construction Assumptions](Canonical%20Construction%20Assumptions.md); S2/S3 cost inputs | CAN-030, CAN-033 | CST-01…24 (mostly DUAL); OQ-10; R-4/6/9; MB-16 | Finalized construction cost; single-value unit costs; comparing durations without definition note | GC pricing (MB-16); structural engineering (D-P3 predicate) | scenario analysis |

### Chapters 15–19 — Economics and stakeholders

| Ch | Chapter | Governing sources | Canon / decisions | Registers | Prohibited or unsafe assertions | External verification needed | Drafting status |
|---|---|---|---|---|---|---|---|
| 15 | Operating and Revenue Model | [Canonical Financial Assumptions](Canonical%20Financial%20Assumptions.md) §2; S2/S3 | CAN-012; D-P2 | REV-01…13; OQ-15/16/22; R-19 | Speculative revenue in base case; blended rents; validated parking pricing | MB-07/09; model vNext (D-P4) | scenario analysis |
| 16 | Financial Feasibility | [Canonical Financial Assumptions](Canonical%20Financial%20Assumptions.md) §6; S2 `Returns`; S3 `Financing & Returns`; `scripts/verify_workbook_claims.py` output | CAN-020…022; Canon §3 | EXT-01…06; OQ-17/18; R-13, R-20 | Omitting or softening the negative finding; presenting model outputs as facts; calling workbooks audited | Model vNext + formal model audit; MA-06 recreation | qualified analysis (mandatory content) |
| 17 | Capital Structure and Incentives | [Canonical Financial Assumptions](Canonical%20Financial%20Assumptions.md) §§3–4; S4 §11.2 | — (D-P7 pending — not authority) | FIN-01…05; CST-14/15; OQ-17; R-14; MB-13/14 | Secured grants/TIF/QOZ benefits/credits; underwriting any credit above $0 | Tax counsel (MB-13); incentives scan (MB-14) | qualified analysis |
| 18 | Partner and Stakeholder Strategy | [Canonical Healthcare Strategy](Canonical%20Healthcare%20Strategy.md) §§3–4; [partnerships index](../partnerships/README.md) | CAN-013, CAN-032; D-P2 | HC-06/09; OQ-08; MOB-01; MB-08/15/17 | Any commitment, LOI, or endorsement; informal interest presented as more | Operator LOI evidence (MB-08); system conversations documented | qualified analysis |
| 19 | Public Benefits and Civic Alignment | [Canonical Mobility Strategy](Canonical%20Mobility%20Strategy.md) §5; S4 §11.2; SITE-17 | CAN-011 | MB-14, MB-20 | Quantified economic impact (no analysis exists); City endorsement; secured public support | Economic-impact analysis (MB-20); incentives scan (MB-14) | qualified analysis + placeholder pending research (impact figures) |

### Chapters 20–25 — Risk, decisions, diligence, record

| Ch | Chapter | Governing sources | Canon / decisions | Registers | Prohibited or unsafe assertions | External verification needed | Drafting status |
|---|---|---|---|---|---|---|---|
| 20 | Development Schedule and Critical Path | [Implementation Roadmap](Implementation%20Roadmap.md) Track P; [Document Update Order](Document%20Update%20Order.md) | D-P11 (scope limits) | MB-01…20 sequencing; OQ resolution order | Presenting Track P items as authorized/funded; schedule certainty | None for drafting; each item owner-gated | qualified analysis |
| 21 | Risk Register and Failure Conditions | [Risk Register](Risk%20Register.md) | Canon §3 (R-13 linkage) | R-1…R-20 | Minimizing R-13; omitting negotiation/evidence-fragility risks | Specialist confirmation of ratings | qualified analysis |
| 22 | Decision Agenda | [Decision Log](Decision%20Log.md); `docs/decisions/` | D-P1…D-P12 states | OQ-11/14/15/17/18/20/21 | Citing pending decisions as authority; implying any pending decision is resolved | None (record of record) | verified analysis (of the decision record) |
| 23 | Diligence Plan | [Missing Research Register](Missing%20Research%20Register.md); [Implementation Roadmap](Implementation%20Roadmap.md) | D-P1 diligence conditions | MA-01…18; MB-01…20 | Describing any study as commissioned/funded/authorized | Each study is itself the verification | qualified analysis |
| 24 | Investment Committee Recommendation | This map §5; owner amendments A1/A5/A7 (2026-07-26 review) | All ratified decisions; Canon §3 | All critical OQ/MB items | Manufactured positive recommendation; recommendation language implying authorization | None (judgment, labeled as recommendation) | qualified analysis |
| 25 | Appendices and Evidence Index | [Source Inventory](Source%20Inventory.md); [Source Authority Register](Source%20Authority%20Register.md); `exports/` | Canon §8 | S1–S8 with SHA-256 integrity records | Treating exports as authority; quoting S5 figures | None (record of record) | verified analysis (of the record) |

## 3. Condensed conflict table (material conflicts the IIM must disclose)

Full register: [Contradictions Matrix](Contradictions%20Matrix.md). Columns per `skills/source-reconciliation/SKILL.md`. The IIM must present these as unresolved wherever the topic appears; it may not resolve, average, or silently select.

| Topic | Old value | Old source | Current value | Controlling source | Status | Treatment |
|---|---|---|---|---|---|---|
| Program/floor-plate basis | 35,000 SF plate | S2 `Assumptions!B8` | 28,000/24,000 SF plates | None — escalated | current working assumptions (two) | Unresolved (OQ-14/D-P5); IIM presents both bases, never mixed |
| Medical office rent | $36/RSF ("FACT" tag — overclaim) | S2 `Assumptions!B53` | $50/RSF (illustrative) | None — escalated | SD vs WA | Unresolved (OQ-15/D-P6); IIM presents both, neither validated |
| Tax credits | 30% ITC captured | S2 `Assumptions!B38` | $0 underwritten (§48E change; §30C deadline 6/30/2026) | S3 position interim, counsel pending | current working assumption (conflicting) | Unresolved (OQ-17/D-P7); IIM underwrites $0 pending counsel |
| Exit cap / hurdle | 6.25% cap; 150+ bps spread | S2 `Assumptions!B69`, `Summary!D9` | 7.25% cap; 7.0% YoC target | None — escalated | current working assumptions | Unresolved (OQ-18); IIM reports both metrics |
| Parking revenue construct | $2,400/space/yr blended | S2 `Assumptions!B56` | $275/stall/mo × 55% monetized | None — escalated | current working assumptions | Unresolved (OQ-16/MB-09); survey basis missing (MA-16) |
| AV revenue in base NOI | $0 (toggle OFF) | S2 `Assumptions!B63` | $194,400/yr included in S3 base | D-P2 rule controls; S3 in tension | S2 treatment governance-aligned | Escalated (OQ-22); IIM uses governance-clean framing, discloses S3 contamination |
| Height/entitlement framing | "110 ft ~10 stories by right" | S4 zoning table | ">6 stories = enhanced Level III review; ~12-story ceiling subject to review" | Composite S8+S1 working statement | source-derived, conflicting | Unresolved (OQ-03/11); IIM uses the working statement only |
| Land value | $12.0M listing; $11.1M appraisal | S6 | **$7.5M working opening-offer basis** (D-P13, tactical negotiation figure); $8.0M modeled basis (strategy only); $8.96M analyst residual | D-P13 (offer basis); D-P1 (modeled basis, input only); S6 controls the appraisal-opinion topic | working assumption / model input / appraisal opinion / analyst output | Values disclosed side by side (MB-19); no ceiling adopted; offer basis and modeled basis never blended |
| Utility allowance | $750K | S2 `Assumptions!B33` | $1.5M/$1.8M placeholder | None — escalated | current working assumptions | Unresolved (OQ-04/MB-03); "subject to utility confirmation" |
| Construction duration | 18/21 mo (construction only) | S2 | 30/34 mo (build + lease-up) | Definitional difference | current working assumptions | Disclose definitions; never compare carry without normalizing |

## 4. Repository discrepancies found during the IIM audit (2026-07-26)

Documented here for owner review. **No register, export, or governed document was modified.** Proposed entries below are drafts pending owner ratification; pending items are not authority.

| # | Finding | Evidence | Proposed treatment (owner decision required) |
|---|---|---|---|
| 1 | `docs/IMPLEMENTATION_REPORT_2026-07-26.md` §11 states "Commits created: 0; Uncommitted changes: yes; Pushed: no" — stale; the Phase 1 change set was committed and pushed in commit `89455fe` ("Planning phase 2") | `git log` / `git status` 2026-07-26 | Leave the dated report unaltered; note the correction in the next implementation report |
| 2 | The Project Canon uses `external_eligible_with_caveat` (CAN-002/010/011/022), which is not one of the four `external_use_status` values in `docs/standards/METADATA_SCHEMA.md` (`approved_with_caveat` is the schema term) | Canon §§1–3 vs METADATA_SCHEMA.md | Proposed vocabulary reconciliation at the next canon maintenance pass (D-P8 scope) |
| 3 | Risk-ID divergence: the planning [Risk Register](Risk%20Register.md) uses R-1…R-20 while `exports/risks-register.json` renumbers a 9-item subset as R-01…R-09 (export "R-01 base-case return gap" ≈ planning R-13; planning R-1 is flood) | Both registers, 2026-07-26 | Proposed: align export IDs to planning IDs at the next export regeneration; until then cite planning IDs only (the IIM does) |
| 4 | Repository directory name `South_Andrews_Health_and_Mobility_Hub` differs from the canonical project name ("Healthcare") | CAN-001 vs filesystem path | Cosmetic; renaming a repository is an owner/platform action; no document should derive the project name from the path |
| 5 | `exports/missing-research.json` contains 34 entries; the governing [Missing Research Register](Missing%20Research%20Register.md) lists 38 (MB-17…MB-20 absent from the export) | Export vs register, 2026-07-26 | Proposed: add MB-17…MB-20 to the generator mapping at the next authorized export regeneration |
| 6 | Exports are generated from literals in `scripts/generate_exports.py`, not parsed from the governed markdown; markdown/export coupling is by discipline (documented in `docs/standards/STRUCTURED_EXPORTS.md`) | Script inspection | By design; noted so future sessions edit registers first, then the generator mapping |

Proposed register entries derived from the above (drafts, not entered): an Open Questions item for the export/register divergences (findings 3 and 5) and a Contradictions Matrix §G row for finding 2. Findings 1, 4, and 6 need no register entry; they are maintenance notes.

## 5. Standing constraints carried into every IIM chapter

1. Canonical name **South Andrews Healthcare and Mobility Hub** (CAN-001); canonical address **901–917 South Andrews Avenue, Fort Lauderdale, Florida** (D-P12); aliases only in source-specific contexts.
2. The $8,000,000 figure appears only under D-P1 treatment: acquisition-strategy input; not proof of value; not authority; not a ceiling or walk-away; classified `internal_only`. **Amended 2026-07-29:** it is now the **modeled land basis** (CAN-004a). The **$7,500,000** D-P13 working opening-offer basis (CAN-004) is subject to the same per-occurrence rule and must additionally be labelled a tactical negotiation figure, not an economically supported land value. The two bases are never blended.
3. The feasibility finding (Canon §3) is mandatory content and may not be omitted, softened, or contradicted (Canon §8.4).
4. Broward Health language per CAN-013 only; the HC-05 vacancy counterweight accompanies any demand claim.
5. Dual program bases are never mixed (Canon §5); every sized figure names Basis A (S2) or Basis B (S3).
6. Governance-clean base case excludes speculative AV/charging/edge/solar-upside revenue (CAN-012); S3's AV-bay inclusion is disclosed, not adopted.
7. All partners prospective; pending decisions are never cited as authority.
8. All planning-level estimates labeled; workbook outputs are unverified model outputs (R-20), never "audited."
9. Every material claim carries the claims-policy record fields at an institutionally useful level (statement ID or register ID, source locator, evidence class, external-use status).
10. The IIM is `internal_only`; external use requires the full checklist plus Document Update Order Step 8 gates (model vNext, ODP v2, independent audit).
