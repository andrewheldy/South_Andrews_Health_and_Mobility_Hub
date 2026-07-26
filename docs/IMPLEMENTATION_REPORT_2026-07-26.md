# Canon Ratification and Repository Refactor Phase 1 Implementation Report

**Implementation date:** 2026-07-26
**Decision authority:** Owner
**Branch:** `main`
**External-use status:** internal_only

## 1. Executive result

The Project Canon was successfully ratified with the qualifications required by the owner. Repository refactor Phase 1 was completed within D-P11’s limits.

The implementation records D-P1, D-P2, D-P8, D-P9, D-P11, and D-P12; preserves D-P5, D-P6, D-P7, D-P10, and the other program/economic matters as unresolved; establishes governance succession and records hygiene; adds structured registers/exports and validation; protects original sources; and does not build model vNext, ODP v2, a prospectus, or a frontend.

The negative feasibility conclusion remains prominent: both current models indicate that the presently modeled base project at an $8,000,000 land basis does not satisfy their respective modeled institutional return requirements.

## 2. Decisions recorded

Ratified:

- D-P1 — $8,000,000 working opening-offer strategy input only; no inferred transaction authority, ceiling, walk-away, or final conditions.
- D-P2 — healthcare anchor; mobility/energy/data/AV systems enabling or optional; no speculative optional revenue in a governance-clean base case.
- D-P8 — controlled status system and preserved lineage.
- D-P9 — current `AGENTS.md` and governance set are operative; recovered prior governance enters as historical evidence pending reconciliation.
- D-P11 — repository refactor Phase 1 within original-source/model and unresolved-decision protections.
- D-P12 — canonical address, with source-specific parcel aliases preserved.

Pending:

- D-P3 — convertible-structure scope/premium.
- D-P4 — successor-model treatment of optional AV/data revenue.
- D-P5 — program and floor-plate basis.
- D-P6 — medical-office/clinical rent basis.
- D-P7 — tax-credit treatment.
- D-P10 — 6-story versus 8-story selection.

## 3. Files created

Repository navigation and workflow:

- `.gitignore`
- `README.md`
- `WORKFLOW.md`

Decision records:

- `docs/decisions/README.md`
- `docs/decisions/D-P1-land-offer-mandate.md`
- `docs/decisions/D-P2-project-thesis.md`
- `docs/decisions/D-P8-records-hygiene.md`
- `docs/decisions/D-P9-governance-succession.md`
- `docs/decisions/D-P11-repository-refactor-phase-1.md`
- `docs/decisions/D-P12-canonical-address.md`

Indexes, controls, and standards:

- `docs/canon/README.md`
- `docs/registers/README.md`
- `docs/research/README.md`
- `docs/technical/README.md`
- `docs/financial/README.md`
- `docs/program/README.md`
- `docs/partnerships/README.md`
- `docs/external/README.md`
- `docs/external/EXTERNAL_PUBLICATION_CHECKLIST.md`
- `docs/archive/ARCHIVE_MAP.md`
- `docs/standards/METADATA_SCHEMA.md`
- `docs/standards/SOURCE_HANDLING.md`
- `docs/standards/STRUCTURED_EXPORTS.md`
- `docs/standards/VALIDATION.md`
- `templates/document-metadata-template.md`

Generated/working boundaries:

- `derived/README.md`
- `derived/workbooks/README.md`
- `derived/documents/README.md`
- `models/README.md`
- `models/current/.gitkeep`
- `models/working/.gitkeep`
- `models/archived/.gitkeep`
- `models/exports/.gitkeep`
- `models/exports/model-input-template.json`

Schemas and automation:

- `schemas/export-envelope.schema.json`
- `schemas/statement.schema.json`
- `schemas/model-input-contract.schema.json`
- `scripts/README.md`
- `scripts/generate_exports.py`
- `scripts/validate_repository.py`
- `scripts/verify_workbook_claims.py`

Structured outputs:

- `exports/README.md`
- `exports/project-manifest.json`
- `exports/executive-status.json`
- `exports/claims-register.json`
- `exports/assumptions-register.json`
- `exports/decisions-register.json`
- `exports/open-questions.json`
- `exports/risks-register.json`
- `exports/source-register.json`
- `exports/key-metrics.json`
- `exports/scenario-register.json`
- `exports/missing-research.json`

Implementation record:

- `docs/IMPLEMENTATION_REPORT_2026-07-26.md`

## 4. Files modified

Governance:

- `AGENTS.md` — added D-P9 governance succession, D-P12 canonical address handling, and the separation of statement type from evidence class.
- `CLAUDE.md` — added current-governance succession and canonical-address rules.
- `docs/governance/SOURCE_AUTHORITY.md` — made D-P9 succession operative.
- `docs/governance/CLAIMS_AND_EVIDENCE_POLICY.md` — added statement typing and the external-publication gate.
- `docs/governance/WORKFLOW.md` — recorded the Phase 1 ratification scope and unresolved-decision boundary.

Ratified canon and operative registers:

- `docs/planning/Project Canon.md` — promoted from draft to ratified; added stable statement IDs/classes; qualified Broward Health demand language; preserved the negative feasibility conclusion; distinguished strategy from fact; preserved unresolved decisions/scenarios.
- `docs/planning/Decision Log.md` — recorded six ratified decisions with date, owner authority, scope, rationale, affected documents, supersession, and review triggers; kept pending decisions pending.
- `docs/planning/Executive Planning Summary.md` — replaced the former pre-ratification status with the ratified/implemented state and retained the pending-decision boundary.
- `docs/planning/Open Questions.md` — closed OQ-01/OQ-12/OQ-19/OQ-23, partially resolved OQ-20, and preserved the remaining questions.
- `docs/planning/Master Assumption Register.md` — limited ACQ-01 to the D-P1 strategy scope and made ceiling/walk-away explicitly unresolved.
- `docs/planning/Contradictions Matrix.md` — recorded D-P2/D-P8/D-P1 treatments and retained all material unresolved conflicts.
- `docs/planning/Missing Research Register.md` — reclassified missing prior governance as historical dependencies under D-P9.
- `docs/planning/Risk Register.md` — closed the thesis ambiguity at strategy level and removed unsupported price-ceiling/walk-away treatment.
- `docs/planning/Source Inventory.md` — made the inventory operative and recorded Phase 1 hygiene/source-protection treatment.
- `docs/planning/Source Authority Register.md` — recorded D-P1’s limited authority and D-P2’s clean-base AV rule.

Planning architecture and downstream references:

- `docs/planning/Canonical Data Model.md` — replaced the draft model with the ratified Phase 1 statement/evidence/status schema.
- `docs/planning/Repository Refactoring Plan.md` — recorded Phase 1 completion and protected original-source filenames.
- `docs/planning/Document Update Order.md` — marked steps 0–3 complete and retained later gates.
- `docs/planning/Implementation Roadmap.md` — moved owner review/Phase 1 to complete and retained studies/model/prospectus gates.
- `docs/planning/Document Dependency Graph.md` — changed status to current.
- `docs/planning/Repository Knowledge Graph.md` — changed status and corrected D-P1 treatment.
- `docs/planning/Archive Recommendations.md` — converted to current guidance and clarified that original-source operations remain unauthorized.

Scope, program, and strategy records:

- `docs/planning/Current Project Scope.md` — made D-P2 operative and clarified the governance-clean AV base case.
- `docs/planning/Current Development Program.md` — preserved scenario status and qualified co-working demand/commitment.
- `docs/planning/Canonical Financial Assumptions.md` — corrected the $8,000,000 input to D-P1’s limited strategy scope.
- `docs/planning/Canonical Construction Assumptions.md` — changed status to current working assumptions.
- `docs/planning/Canonical Healthcare Strategy.md` — removed assertive displacement/parking-deficit language and substituted the approved qualified demand statement.
- `docs/planning/Canonical Mobility Strategy.md` — distinguished governance-clean base treatment from the preserved S3 conflict.
- `docs/planning/Canonical Infrastructure Strategy.md` — changed status to current working strategy with sizing unresolved.

## 5. Files moved or renamed

No files were moved or renamed. Existing paths and Git history were preserved.

The tracked macOS metadata artifact `sources/.DS_Store` was removed from the repository index and `.DS_Store` was added to `.gitignore`. It was not project evidence and is not an original source.

## 6. Sources protected

All eight governed original sources were checked and remained unchanged:

| Source | SHA-256 |
|---|---|
| `sources/current/South_Andrews_Corrected_Assumptions.md` | `b1aa5c31af384cc68a1ebb94172c8a1710e853233d51dd90633ce694d7b504ad` |
| `sources/current/South Andrews 6v8 Story Model.xlsx` | `ee5146a7cd1495aace3c72aeb78bf7200c2abfedbd0bec64cce7ab09753e4fab` |
| `sources/current/South_Andrews_8M_Construction_Feasibility.xlsx` | `0d9299f93013c45579ff29bb6765c75eff5e70337af0429e4ec39cf9e4be0a0e` |
| `sources/current/Andrews ODP with Dashboard.docx` | `a336c00a9471efb8243aa57f6e1b4eae9186167c7cef3a3ca7e260e749040487` |
| `sources/legacy/Institutional Development Prospectus Vol0.docx` | `28ed83d76f8b5cf051c4417fa0c6fc3b1076d9d2854c50ded4bf41cf4458d0ab` |
| `sources/reference/Andrew’s Appraisal.pdf` | `4adea2b61b43e28de402646e96e4293396a2e83f940dabfe14f90dba4f519206` |
| `sources/reference/Appraisal Valuation .xlsx` | `176676736467606fbe439af23c0476eb0f48fb93da5b9d55ad8fec4017570b79` |
| `sources/reference/NativeRealty_905 S Andrews - Development Feasibility & Massing Study.pdf` | `c2ce97c4948be7e51c9d587864d409e8c75b9911b7281e6ca20cedd7cc0d5d3e` |

Read-only workbook verification confirmed:

- S2 `Assumptions!B18` = $8,000,000.
- S2 `Returns!B13:B17` and `B27:B31` contain the cited yield, value, loss, IRR, and multiple outputs with formulas.
- S3 `Assumptions!D7` = $8,000,000.
- S3 `Financing & Returns!D11:E11` contains $194,400 AV-bay revenue with formulas.
- S3 `Financing & Returns!D21:E28` contains the cited yield, support-gap, and value-gap outputs with formulas.

No workbook value or formula was changed.

## 7. Structured outputs and governing sources

| Export | Governing human source |
|---|---|
| `project-manifest.json` | Project Canon; Decision Log |
| `executive-status.json` | Executive Planning Summary; Project Canon |
| `claims-register.json` | Project Canon; Claims and Evidence Policy |
| `assumptions-register.json` | Master Assumption Register |
| `decisions-register.json` | Decision Log; individual decision records |
| `open-questions.json` | Open Questions |
| `risks-register.json` | Risk Register; Project Canon |
| `source-register.json` | Source Inventory; Source Authority Register |
| `key-metrics.json` | Project Canon; Master Assumption Register |
| `scenario-register.json` | Project Canon; Current Development Program |
| `missing-research.json` | Missing Research Register |

Each export contains schema version, generated date, source-of-truth path, document status, provenance, validation result, and unresolved dependencies. Each reports validation status `passed`.

## 8. Validation results

Checks performed:

- Required export/envelope and JSON-schema-file checks.
- Decision-ID validity/completeness and duplicate decision/assumption/claim/model-input checks.
- Claim and assumption provenance/status/scenario checks.
- External-eligible claim dependency check.
- Canonical project name/address, ownership/site-control, scenario, and negative-feasibility checks.
- Future-model contract coverage and incompatible-floor-plate separation.
- Governance-clean AV revenue = $0 check.
- Original-source existence and SHA-256 integrity checks.
- Internal Markdown link checks.
- Missing-governance/current-authority language checks.
- Ownership/control, historical project-name, canonical-address, and assertive Broward-demand language searches.
- Python script compilation.
- Git whitespace/error check.
- Direct read-only workbook cell/formula verification.
- Final source diff and full implementation diff review.

First automated pass: 104 checks; 2 metadata failures. Corrections made:

1. Added explicit D-P1/OQ-20 provenance to the unresolved ceiling/walk-away assumption.
2. Changed CAN-012 from unrestricted external eligibility to approved-with-caveat because S3 retains a known successor-model correction dependency.

Final automated pass: 103 checks; **0 errors; 0 warnings**.

## 9. Remaining conflicts

- Program/floor-plate basis: 35,000 SF versus 28,000/24,000 SF.
- Medical-office/clinical rent: $36 versus $50/RSF and independently validated market basis.
- Tax-credit treatment.
- Exit capitalization rate, target yield on cost, and institutional hurdle.
- Negotiating authority, land-price ceiling, walk-away price, and final offer conditions.
- Final 6-story versus 8-story selection.
- Charger mix/count beyond the approximately 40-port placeholder.
- Solar/BESS capacity and roof allocation.
- Optional AV staging and edge/data revenue; S3’s current AV-bay inclusion remains a disclosed source-model conflict.
- Health-system, operator, medical co-working, mobility, financing, and public-support commitments.
- Entitlement/zoning confirmation and utility/FPL capacity.
- Missing prior governance, market study/library, electrical load model, survey/title/environmental records, and other listed research dependencies.
- Architectural test-fit, environmental, geotechnical, flood/stormwater, traffic/access, parking-operations, and partner-demand studies.

## 10. Next authorized work

1. Recover missing governance and research documents.
2. Commission architectural test-fit.
3. Obtain zoning verification.
4. Initiate FPL capacity/load study.
5. Validate MOB and clinical rents.
6. Obtain tax-credit advice.
7. Establish owner land-price ceiling and transaction authority.
8. Build model vNext after the required evidence and decisions.
9. Generate ODP v2.
10. After audit/corrections, prepare the external prospectus and frontend.

## 11. Git status

- Branch: `main`.
- Commits created: **0**.
- Uncommitted changes: **yes** — all Phase 1 implementation changes listed in this report, including removal of the tracked `sources/.DS_Store` artifact.
- Pushed: **no**.
