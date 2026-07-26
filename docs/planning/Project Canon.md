# Project Canon

**Document status:** Ratified · **Ratification date:** 2026-07-26 · **Decision authority:** Owner
**External-use status:** Internal governing record; individual statements retain their own eligibility
**Governing documents:** `AGENTS.md`, the current `docs/governance/` set, and explicit current owner decisions
**Related:** [Decision Log](Decision%20Log.md) · [Master Assumption Register](Master%20Assumption%20Register.md) · [Contradictions Matrix](Contradictions%20Matrix.md)

This is the human-reviewed canonical project record. Structured exports are derived views and do not replace it. Ratification adopts the explicitly identified strategies and decisions; it does not convert assumptions, source-derived claims, or model outputs into verified facts.

## 1. Canonical identity and status

| ID | Statement | Statement type | Evidence class | Provenance / locator | Confidence | External use | Dependencies / caveat | Supersession |
|---|---|---|---|---|---|---|---|---|
| CAN-001 | The canonical project name is **South Andrews Healthcare and Mobility Hub**. | owner_decision | verified fact | D-G1; `AGENTS.md`; `PROJECT_GLOSSARY.md` | high | external_eligible | Older names remain historical source identifiers. | Supersedes active use of older project names. |
| CAN-002 | The canonical identity address is **901–917 South Andrews Avenue, Fort Lauderdale, Florida**. | owner_decision | current working assumption | D-P12 | high as owner-selected identity string | external_eligible_with_caveat | Preserve parcel/source-specific addresses for legal, title, survey, appraisal, environmental, tax, and quoted contexts. | Address aliases remain preserved. |
| CAN-003 | **Prospective acquisition. The sponsor does not currently own the property.** | owner_decision | verified fact | D-G3; D-P1; `AGENTS.md` | high | external_eligible | Do not imply control, contract, acquisition, or commitment without future evidence. | None. |
| CAN-004 | The working opening-offer input is **$8,000,000**. It is not proof of value and does not itself authorize an offer. | adopted_strategy | current working assumption | D-P1; S2 `Assumptions!B18`; S3 `Assumptions!D7`; S8 p.7 | high as adopted strategy | internal_only | Negotiating authority, maximum price, walk-away price, and final conditions are unresolved; diligence required. | Supersedes any treatment as proven value or price ceiling. |

## 2. Ratified thesis

| ID | Statement | Statement type | Evidence class | Provenance | Confidence | External use | Dependencies / caveat | Supersession |
|---|---|---|---|---|---|---|---|---|
| CAN-010 | Healthcare is the project anchor. | adopted_strategy | current working assumption | D-P2 | high as adopted strategy | external_eligible_with_caveat | Strategy, not verified demand or partner commitment; subject to market validation, test-fit, entitlement, operator input, and economics. | Supersedes active mobility-led thesis. |
| CAN-011 | Structured parking, EV charging/readiness, AV staging readiness, solar, battery storage, data infrastructure, and related mobility systems are enabling infrastructure or optional value layers. | adopted_strategy | current working assumption | D-P2 | high as adopted strategy | external_eligible_with_caveat | Scope and sizing remain subject to test-fit, engineering, code, utility, operator, and economic validation. | Supersedes treatment as the primary thesis. |
| CAN-012 | A governance-clean base case excludes speculative AV, charging, fleet-operating, edge-compute, and similar optional revenue unless contractually supported and later approved. | owner_decision | current working assumption | D-P2 | high | approved_with_caveat | S3 currently includes AV-bay revenue in modeled base NOI; that model output must be caveated and corrected only in an authorized successor model. | Supersedes historical base-case treatment inconsistent with this rule. |
| CAN-013 | Broward Health’s nearby expansion **may** create complementary demand for independent providers, outpatient services, workforce support, parking, and related healthcare uses. The extent, timing, and rent implications have not been independently validated. | source_derived_claim | source-derived but not independently verified | S4/S5 citing missing Market Study MA-07 | low | blocked_pending_resolution | Recover or independently rebuild the market study. No claim of displacement, parking deficit, guaranteed spillover, or endorsement is permitted. | Stronger demand language is retained only as an internal historical hypothesis. |

## 3. Feasibility finding

> **Both current financial models independently indicate that the base project, as presently modeled at an $8,000,000 land basis, does not satisfy the modeled institutional return requirements.**

| ID | Statement | Statement type | Evidence class | Provenance / locator | Confidence | External use | Dependencies / caveat |
|---|---|---|---|---|---|---|---|
| CAN-020 | S2 reports yield on cost of 3.83% / 4.02%, development profit of approximately −$27.7M / −$33.9M, and ten-year unlevered IRRs of approximately 1.2% / 1.9% for its 6-/8-story scenarios. | model_output | model output | S2 `Returns!B13:B31` | high as workbook output | approved_with_caveat | Planning-level model output; S2 program and inputs are not adopted facts. |
| CAN-021 | S3 reports core yield on cost of 3.83% / 4.07%, annual support gaps of approximately $1.89M–$3.23M, and value gaps of approximately −$28.1M to −$47.7M across its modeled cases. | model_output | model output | S3 `Financing & Returns!D21:E28` | high as workbook output | approved_with_caveat | Planning-level model output; S3 includes AV-bay revenue in base NOI and uses a different, unadopted program basis. |
| CAN-022 | The convergent conclusion is that the presently modeled base project does not meet the respective modeled institutional return requirements. | model_output | model output | S2 `Returns`; S3 `Financing & Returns` | high as convergent model conclusion | external_eligible_with_caveat | Neither model proves actual feasibility or market value. Current negative findings must not be omitted. |

Feasibility may require one or more of: a lower land basis; revised program; validated differentiated rents; a health-system or operator anchor; master lease or minimum-use agreement; capital contribution; public support; grant or TIF proceeds; cost reduction; phased capitalization; or contractually supported mobility or energy revenue. These are **recommendations or potential mechanisms only**. None is documented as secured.

## 4. Program and strategy status

The following are adopted planning strategies or working requirements—not verified facts:

| ID | Strategy / requirement | Type | Evidence class | Current treatment and dependency |
|---|---|---|---|---|
| CAN-030 | Convertible parking, universal grid, and removable/conversion-friendly ramp strategy | adopted_strategy | recommendation | Subject to test-fit, structural engineering, code review, operator needs, cost, and D-P3. |
| CAN-031 | EV conduit readiness and approximately 40 initial chargers | adopted_strategy | current working assumption | Planning placeholder only; charger mix/count, FPL capacity, and economics unresolved. |
| CAN-032 | Medical co-working concept | scenario | current working assumption | No operator commitment; market/operator validation required. |
| CAN-033 | Phase sequencing: enabling infrastructure first, flexible clinical/medical-office program later, optional systems demand- or partner-gated | adopted_strategy | recommendation | Subject to test-fit, financing, operator input, and economics. |
| CAN-034 | Roof garden; solar/BESS readiness; small data room; external AV ingress or staging concepts | scenario | current working assumption | Sizing, roof allocation, engineering, utility capacity, code, demand, and economics unresolved. No optional revenue in the clean base case. |

## 5. Scenario discipline

- **6-story scenario:** active scenario; not adopted.
- **8-story scenario:** active scenario; not adopted.
- **35,000 SF plate basis (S2):** active modeled basis; not adopted.
- **28,000/24,000 SF plate basis (S3/S8):** active modeled basis; not adopted.
- Incompatible program bases must never be combined. Architectural and parking test-fit plus D-P5 are required.
- Healthcare-led scenario: adopted thesis, but its detailed program is unresolved.
- Mobility-led, car-rental fleet hub, seller Agora, residential-led, and hotel-led concepts: preserved historical or rejected scenarios, not deleted.

## 6. Site and entitlement evidence

The repository contains strongly corroborated source statements for a 38,207 SF / approximately 0.88-acre three-parcel assemblage, one folio, the cited frontages, RAC-RPO zoning, Zone AE mapping, and existing older commercial improvements. These remain subject to their source scopes and to updated title, survey, zoning, environmental, flood/stormwater, and technical diligence.

No canon statement represents entitlement approval, City support, final height, final FAR, approved design, utility/FPL capacity, environmental clearance, or site control. The working entitlement path above six stories remains unverified pending City confirmation.

## 7. Unresolved decisions and dependencies

The canon does not resolve: D-P5 program/floor plate; D-P6 office/clinical rent; D-P7 tax credits; exit cap; target yield on cost; institutional hurdle; final land ceiling or walk-away; story selection; charger mix/count beyond the placeholder; solar/BESS sizing; roof allocation; AV/data revenue; partner commitments; grants/TIF/QOZ/bond/subsidy proceeds; entitlement; or utility capacity.

Missing prior governance, market evidence, survey/title/environmental records, electrical-load support, and the required diligence studies remain listed in the [Missing Research Register](Missing%20Research%20Register.md) and structured export.

## 8. Maintenance and external-use rules

1. Owner decisions are recorded in the [Decision Log](Decision%20Log.md) and individual records.
2. Each material statement carries a stable ID, type, evidence class, provenance, confidence, external-use status, review date, dependencies, and supersession treatment in the claims export.
3. Statement type never promotes evidence class: an adopted strategy is not a verified fact.
4. No downstream model, prospectus, interface, caption, or rendering may contradict the canon or omit the current feasibility finding.
5. External use must pass `docs/external/EXTERNAL_PUBLICATION_CHECKLIST.md`.
6. Review date for this ratification: **2026-07-26**.
