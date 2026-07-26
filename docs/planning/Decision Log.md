# Decision Log

**Status:** Ratified operative register · **Date:** 2026-07-26 · **Decision authority:** Owner
**Governing rule:** An owner decision controls only when its content, date, decision-maker, and scope are documented.
**Related:** [Project Canon](Project%20Canon.md) · [Open Questions](Open%20Questions.md) · [`docs/decisions/`](../decisions/)

The `D-P#` identifiers are preserved from planning so citations and history remain stable. `ratified` means the exact scope below is an explicit current owner decision. `pending` is not authority.

## Ratified owner decisions

| ID | Title | Exact decision / authorized scope | Status | Date | Decision maker | Review trigger |
|---|---|---|---|---|---|---|
| **D-P1** | Land-offer mandate | Working opening offer: **$8,000,000**. This is an acquisition-strategy input, not proof of value and not, by itself, authority to submit an offer. Negotiating authority, maximum authorized purchase price, walk-away price, and final offer conditions remain unresolved pending diligence. Sponsor does not own, control, or have the property under contract. Preserve the diligence conditions in the individual record. | **ratified** | 2026-07-26 | Owner | New diligence, transaction authority, or owner price decision |
| **D-P2** | Project thesis | Develop and evaluate the project as healthcare-anchored and mixed-use institutional. Parking, EV, AV, solar, storage, data, and related mobility systems are enabling infrastructure or optional value layers. Base feasibility must not depend on speculative optional revenue. Historical mobility-led concepts remain preserved as rejected or superseded scenarios. | **ratified** | 2026-07-26 | Owner | Owner changes the thesis or a contractually supported optional revenue source is proposed |
| **D-P8** | Records hygiene | Use the ratified repository status vocabulary and preserve lineage. Do not overwrite or erase historical claims. | **ratified** | 2026-07-26 | Owner | Status schema amendment |
| **D-P9** | Governance succession | `AGENTS.md` and the current `docs/governance/` set are operative unless and until authenticated prior governance is recovered, classified as historical evidence, reconciled, and expressly acted on. Missing prior governance remains a missing dependency. | **ratified** | 2026-07-26 | Owner | Authenticated prior governance is recovered |
| **D-P11** | Repository refactor Phase 1 | Authorize directories, indexes, schemas, status headers, registers, exports, archive maps, validation, templates, links, generated-output boundaries, and plan-authorized moves of repository-authored documents with history preserved. Original sources and model values/formulas remain immutable. No unresolved program or economic choice is resolved. | **ratified** | 2026-07-26 | Owner | Phase 2 proposal or any source-file operation |
| **D-P12** | Canonical address | Use **901–917 South Andrews Avenue, Fort Lauderdale, Florida** as the standard project identity address. Preserve parcel-specific addresses and quoted source text in legal, title, survey, appraisal, environmental, tax, and parcel-specific contexts. Record aliases in structured data. | **ratified** | 2026-07-26 | Owner | Title/survey evidence changes the identity address |

Full decision records, rationale, affected documents, supersession treatment, and review triggers are in [`docs/decisions/`](../decisions/).

## Pending owner decisions

| ID | Decision required | Required predicate | Status |
|---|---|---|---|
| **D-P3** | Convertible-structure scope and acceptable premium | Test-fit, structural engineering, code review, and GC pricing | pending |
| **D-P4** | Model-vNext correction and treatment of optional AV/data revenue | Model-vNext authorization; contractual support if any optional revenue is proposed | pending |
| **D-P5** | Program and floor-plate basis | Architectural/parking test-fit | **pending** |
| **D-P6** | Medical-office and clinical rent basis | Independent MOB/clinical rent study | **pending** |
| **D-P7** | Tax-credit treatment | Qualified tax advice | **pending** |
| **D-P10** | Final 6-story versus 8-story selection | D-P5/D-P6/D-P7, entitlement work, model vNext, and owner review | pending |

Also unresolved without a later owner decision: exit capitalization rate; target yield on cost; institutional hurdle rate; negotiating authority; land-price ceiling and walk-away price; charger mix/count beyond the planning placeholder; solar/BESS sizing and roof allocation; optional AV/data revenue; partner commitments; public support; entitlement approval; and utility capacity.

## Historical decisions cited but not present

| ID | Reconstructed content | Source and treatment | Status |
|---|---|---|---|
| D-H1 / cited Decision-001 | Mixed-use clinical/mobility concept; “Pure Mobility Nexus” rejected | ODP citation only; thesis content superseded by the precise D-P2 ratification | historical_claim |
| D-H2 / cited Decision-002 | Convertible parking strategy | ODP citation only; strategy remains a working requirement pending D-P3 | historical_claim |
| D-H3 / cited Decision-003 | No speculative day-one AV/edge revenue | ODP citation only; base-case rule is now controlled by D-P2 | historical_claim |

The missing source Decision Log remains tracked as MA-02 and is not silently recreated by this register.

## Register discipline

1. Preserve IDs and append decisions; a superseding decision names what it supersedes.
2. Never cite a pending decision as authority.
3. Record decision-maker, date, exact statement, scope, rationale/evidence, affected documents, supersession, and review trigger.
4. After a decision, regenerate structured exports and run repository validation.
