# Electrical Basis of Design

**Status:** Planning-level basis of design; **not an engineered design** · **Prepared:** 2026-07-27
**External-use status:** internal_only
**Related:** [Contradiction and Validation Register](../planning/Contradiction%20and%20Validation%20Register.md) · [Integrated Development Source Map](../planning/Integrated%20Development%20Source%20Map.md) · [Entitlement and Utility Roadmap](Entitlement%20and%20Utility%20Roadmap.md) · [Two-Site Operating Plan](Two-Site%20Operating%20Plan.md)

> **NOTHING IN THIS DOCUMENT IS AN FPL COMMITMENT, A LOAD LETTER, OR AN ENGINEERED DESIGN.** No licensed electrical engineer has reviewed this project. No FPL capacity study, will-serve letter, or service application exists. Every load, service size, voltage, and cost figure below is a planning-level estimate requiring engineer and utility confirmation before it drives any commitment.

---

## 1. Audit of the electrical load workbook

The assignment directed an audit of the electrical load model rather than a restatement of its summary. That audit produced findings serious enough that its **conclusions are not adopted**, though its **method is largely sound and partly adopted**.

### 1.1 Provenance — the workbook is not a governed source

| Finding | Detail |
|---|---|
| Location | `~/Downloads/South_Andrews_Electrical_Load_Model_CORRECTED.xlsx` and `…_CORRECTED_1.xlsx` |
| Repository status | **Neither file is in `sources/`.** Not registered, not hashed, not governed |
| Duplication | Both files are **byte-identical** (SHA-256 `f7cfe13a6b33ac7095a596aa2d01a6d27197c8c23cbb8c96e9dba1861994b400`). `_1` is a duplicate download, not a revision |
| The original it corrects | **Not present in any searched location.** Its contents survive only as the "Uploaded" column of the workbook's own `Reconciliation` sheet — an account written by the corrector, not the original |
| Downstream dependency | S3 `Sources!A8` cites this model as the basis for its 9.6 kW/port and 1,500 kWh/kW-yr factors |
| Self-assessment | The workbook's own `Load Build-Up!A47`: *"NOTHING HERE IS AN ENGINEERED LOAD LETTER. An electrical engineer and an FPL capacity study must confirm before this drives any commitment."* That caution is correct and is carried forward |

Structure: three sheets — `Reconciliation` (17 rows), `Inputs` (51 rows), `Load Build-Up` (47 rows). Every formula was inspected. There are no broken links, no circular references, and no external links. Cell references resolve correctly.

### 1.2 What the workbook gets right — and is adopted

| Item | Assessment |
|---|---|
| **Ampacity formula** `kW×1000/(V×√3×PF)` | Correct three-phase relationship. **Adopted** |
| **NEC 625.42 continuous-load treatment** | Correctly identifies that EV supply equipment is a continuous load and must be sized at 125%. The original model omitted this. **Adopted in principle** — with the qualification at §1.4 |
| **Fleet energy-first method** | Computing daily fleet energy (vehicles × miles × kWh/mile) and dividing by the charging window, rather than summing charger nameplates, is the correct way to size a managed depot. **Adopted** |
| **Charging-window sensitivity** | `Load Build-Up!A46`: lengthening the charging window is the cheapest lever on the whole service. **Correct and important** |
| **Solar canopy cost** | Its $4.00/W override against the project's $2.60/W is right: canopy structures cost materially more than rooftop arrays. **Adopted for canopy-mounted capacity** |
| **Demand-charge warning** | `Load Build-Up!A45` flags that the project's $0.13/kWh energy assumption carries no demand component, and that at a large peak this is a six-figure annual omission. **Correct, material, and not modelled anywhere in the project** |
| **Battery as load-management infrastructure** | Correctly reframes storage from amenity to infrastructure. **Adopted as an operating concept** — but see §1.4 on service sizing |
| **Site facts** | 38,207 SF / RAC-RPO / Zone AE all confirmed against S6 |

### 1.3 What the workbook gets wrong — and is not adopted

**Finding E-1 — It models a building this project has not chosen to build.**
Its `Inputs` sheet carries a **55,000 SF on-site depot charging 120 vehicles** — approximately **1,444 kW managed**, the single largest load in the model and larger than the entire original model it corrects. This is precisely the function the two-site strategy relocates off South Andrews. Sizing the site's service from this workbook would provision South Andrews for a program the owner is being advised against.

**Finding E-2 — Its area basis is internally inconsistent.**
`Reconciliation!C5` states "216,000 SF GBA." Its own `Inputs` areas sum to **205,000 SF** (35,000 office + 10,000 med-tail + 55,000 depot + 105,000 parking). An 11,000 SF discrepancy sits inside the reconciliation tab itself.

**Finding E-3 — It understates clinical area by treating one floor as the whole program.**
`Inputs!B5` carries 35,000 SF of office/clinical, annotated "L6." Under Basis A the 6-storey scheme has 70,000 GSF of office; under Basis B, 48,000 GSF. The building load is understated even while the charging load is overstated.

**Finding E-4 — It subtracts battery capacity from the service size.**
`Load Build-Up!D25` deducts 700 kW of battery peak-shave directly from the service basis to produce a "MANAGED SERVICE BASIS." **This is not a service size an engineer can stamp.** A utility service must serve the load when storage is unavailable, depleted, or out for maintenance. Reducing a service below connected demand on the strength of storage requires a code-recognised energy management system (NEC Art. 750, and the load-management provisions of Art. 625) *and* utility concurrence. Neither is documented. Storage legitimately manages **demand charges**; it does not by itself reduce **required service capacity**.

**Finding E-5 — It stacks diversity factors with the NEC continuous multiplier.**
It applies coincidence factors (0.5 to Level 2, 0.6 to DC fast charging) and then multiplies the result by 1.25. NEC 625.42 permits sizing to the maximum an energy management system will allow; it does not generally permit discretionary coincidence factors on unmanaged EVSE. The two conventions are mixed, producing a figure that is neither the code minimum nor a clean diversified estimate. It is defensible **only** if a documented load-management system enforces the assumed coincidence.

**Finding E-6 — It reinstates a 30% solar ITC.**
`Inputs!B47` = 0.30 and `Load Build-Up!B37` nets solar capital by it. This contradicts S3 `Energy & Mobility!B21` (0% underwritten, citing 2025–2026 §48E changes) and the repository's adopted interim rule under OQ-17. **Rejected**; solar is carried gross.

**Finding E-7 — Its service cost figures are JUDGMENT-class with no basis.**
`Inputs!B50/B51` carry $3.5M managed / $5.0M unmanaged. Both are self-classified JUDGMENT. Against S2's $750K and S3's $1.5–1.8M, the project now holds a **6.7× spread** on a single line with no engineered support anywhere (CVR-16 / OQ-25).

**Finding E-8 — Every citation is a placeholder.**
`Reconciliation!B15` records that the original carried placeholder references `[1]`–`[8]`, and `C15` states these remain "Still unverified." No load figure in the lineage rests on a cited standard or a utility document.

### 1.4 Adoption summary

| Element | Treatment |
|---|---|
| Ampacity formula, energy-first fleet method, charging-window sensitivity, canopy solar cost, demand-charge warning | **Adopted** |
| NEC 625.42 continuous factor | **Adopted**, with the sizing convention to be stated explicitly by the engineer |
| Battery as demand-charge and resilience infrastructure | **Adopted as an operating concept** |
| Battery as a service-size reduction | **Rejected** pending an EMS design and FPL concurrence |
| 55,000 SF on-site depot load | **Rejected** for the recommended strategy; retained only in the SA-A maximum-fleet case |
| 30% solar ITC | **Rejected** per OQ-17 |
| $3.5M / $5.0M service cost | **Not adopted**; carried as the upper bound of an unresolved range |
| 216,000 SF GBA | **Rejected** — internally inconsistent and matches no adopted basis |

## 2. Existing and proposed service

| Item | Status |
|---|---|
| Existing service | Three 1959-era one-storey commercial buildings served by FPL (S6 pp.26–27). **Existing service capacity, voltage, transformer size and point of connection are entirely unknown.** No utility record is in the repository |
| Utility | Florida Power & Light (S6 p.27) |
| Proposed voltage — clinical-anchored cases | **480Y/277 V, 3-phase, 4-wire secondary** from a utility pad-mount transformer |
| Proposed voltage — maximum-fleet case | **Medium voltage (13.2 kV) primary** with owner-side transformation. Above roughly 3,000 A at 480 V, medium-voltage service with owner transformers becomes standard and often cheaper |
| Power factor | 0.90 assumed. A correction requirement is likely at this load class and is not budgeted |
| Redundancy | No redundancy is designed. The 2020 Sistrunk substation fire is cited in S4 §3.3 as the rationale for on-site resilience — **context only**, and it does not establish a requirement |
| **Service entrance constraints** | The transformer and switchgear zone must be independently accessible **without entering the secure mobility loop** (S3 `Energy & Mobility!A28`), must meet FPL clearance and access requirements, and — because the entire site is in **FEMA Zone AE** — must have **all electrical equipment elevated above the base flood elevation**. No numeric BFE is stated in any source; S6 p.28 gives only the generic AE definition and S4 Table 2 carries "≈ 5 ft" at low confidence. **The BFE must be established by survey before any equipment elevation is designed** |

## 3. Building loads

Load densities carry a **material unresolved conflict** (CVR-12 / OQ-24):

| Load | S3 planning density | Corrected workbook density | Note |
|---|---|---|---|
| Office / clinical | **5 W/GSF** | **18 W/SF connected × 0.70 demand = 12.6 W/GSF** | S3 explicitly *excludes* imaging, ASC, kitchen and major tenant equipment. The workbook explicitly *includes* clinical capability. **A 2.5× difference. They measure different things and neither is engineered** |
| Ground floor / med-tail | 6 W/GSF | 22 W/SF connected × 0.80 = 17.6 W/GSF | Food service (hoods, refrigeration) is power-dense; the higher figure is more realistic where a café or kitchen is present |
| Garage / parking | 0.5 W/GSF | 1.5 W/SF connected × 0.80 = 1.2 W/GSF | Lighting, fans, controls |
| Depot / ventilated charging hall | not modelled | 3 W/SF × 0.90 | Mechanical ventilation plus lithium-battery off-gas detection and exhaust — legitimately higher than an ordinary garage |
| Elevators / life safety / miscellaneous | inside the above | 100 kW | Reasonable allowance |

Loads not separately identified in **any** source and which an engineer must add: HVAC (central plant or distributed), domestic and fire pumps, fire alarm and sprinkler systems, garage exhaust and CO/NO₂ monitoring, kitchen equipment, telecom and data rooms, exterior and site lighting, signage, irrigation, and landlord miscellaneous power.

**This document adopts the higher (clinical-capable) densities for planning**, because the project's stated thesis is clinical space, and because under-sizing a service is far more expensive to remedy than over-sizing conduit. The lower S3 densities are retained as the alternative and both are reported.

## 4. EV charging scenarios

Per-port nameplate 9.6 kW (Level 2), 150 kW (DC fast charge). Managed-charging coincidence 0.50 for Level 2, 0.60 for DC fast charge.

| Case | Ports | Connected kW | Diversified demand kW | At NEC 125% |
|---|---|---|---|---|
| **Initial — 40 L2 managed** | 40 | 384 | 192 | 240 |
| 60 L2 managed | 60 | 576 | 288 | 360 |
| 80 L2 managed | 80 | 768 | 384 | 480 |
| 120 L2 managed (8-storey EV-ready total) | 120 | 1,152 | 576 | 720 |
| **Unmanaged 40 L2** (no load management) | 40 | 384 | 384 | 480 |
| + 8 DC fast chargers at 150 kW | 8 | 1,200 | 720 | 900 |
| **On-site depot, 120 vehicles / 8-hour window** | 60 points | 3,600 | 1,444 | 1,805 |
| On-site depot, 120 vehicles / 10-hour window | 60 points | 3,600 | 1,155 | 1,444 |
| On-site depot, 120 vehicles / 12-hour window | 60 points | 3,600 | 963 | 1,203 |

**Management is worth more than any other lever.** Unmanaged 40-port charging draws twice the managed peak. And extending a depot charging window from 8 to 12 hours cuts the depot peak by **481 kW** — more than the entire initial public charging installation. If a depot is ever built, **the charging window is the first thing to negotiate with the operator**, before any equipment is specified.

**Level 2 versus DC fast charging.** Level 2 at 9.6 kW suits clinical visitors (60–180 minute dwell), staff (8–10 hours), and overnight fleet. DC fast charging suits only short-dwell public or fleet top-up and brings disproportionate service, switchgear, and demand-charge consequences. S3's position — **stub-outs and pads only, hardware installed after an operator commitment** — is correct and adopted. S2's eight installed DC fast chargers are not adopted (OQ-21).

**Tariff and demand-limiting.** No FPL rate schedule analysis exists anywhere in the repository. Demand charges are entirely unmodelled — the project carries only a $0.13/kWh energy assumption. At a 1,000 kW peak, commercial demand charges are plausibly a six-figure annual expense. **This is a material omission in both current models** and must be added to the operating pro forma at model vNext.

## 5. Medical imaging

Not committed in any current program, and correctly carried as a toggle.

| Modality | Planning peak | Continuous / standby | Practical implications |
|---|---|---|---|
| MRI | ~75 kW planning figure | Cryocooler and chiller run continuously; quench line to exterior required | RF shielding; magnetic exclusion zones; slab reinforcement; dedicated cooling; vibration isolation. Siting on an upper floor over parking is problematic |
| CT | ~100 kW peak, short-duration | Modest standby | High momentary demand; voltage regulation matters; lead shielding |
| X-ray / fluoroscopy | ~50 kW peak, very short duration | Low | Lead shielding; least demanding |
| **Combined suite** | **~225 kW** as carried in the workbook | — | On a diversified feeder the three rarely peak together; a diversity factor of 0.6–0.7 is typical |

**Diversified feeder demand for a full suite: roughly 135–160 kW.** This is a planning figure only. **Every imaging load must be confirmed against the specific equipment vendor's published data before design** — nameplate figures vary widely by model, and vendors publish momentary, continuous, and standby figures separately.

**Recommendation: imaging does not belong in Phase 1.** It should be a **tenant-funded fit-out gated on confirmed FPL capacity** (consistent with HC-10). The shell should carry spare conduit, spare breaker positions, and a structural allowance so imaging remains possible — but no imaging equipment, shielding, or dedicated cooling should be bought speculatively.

## 6. Service sizing by scenario

Method: connected load × demand factor, summed; non-EV total diversified at 0.90; charging demand multiplied by the NEC 125% continuous factor; battery peak-shave **not** deducted (Finding E-4). Recommended service target adds 25% headroom.

| Scenario | Base building demand | Depot charging | Public L2 | Public DCFC | Service basis | Amps @ 480 V | Indicated class | Recommended target |
|---|---|---|---|---|---|---|---|---|
| **SA-A** (8-storey, on-site depot, 8 DCFC) | 1,070 kW | 1,444 kW | 192 kW | 720 kW | **3,208 kW** | 4,287 A | **Medium voltage (13.2 kV)** | **4.0 MVA** |
| **SA-B** (6-storey, two-site, no DCFC) | 1,003 kW | — | 192 kW | — | **1,143 kW** | 1,527 A | 480 V secondary | **1.4 MVA** |
| **SA-C** (4-storey minimum viable) | 700 kW | — | 192 kW | — | **870 kW** | 1,163 A | 480 V secondary | **1.1 MVA** |
| **SA-C0** (staging ground) | 346 kW | — | 192 kW | — | **552 kW** | 737 A | 480 V secondary | **0.7 MVA** |

### The decisive electrical finding

**Moving the depot off South Andrews reduces the service requirement from approximately 3,208 kW to 1,143 kW — a 64% reduction — and moves the site from medium-voltage primary service to a conventional 480 V secondary.**

That single change avoids owner-side transformers, a utility vault, medium-voltage switchgear, primary metering, and the associated FPL contribution-in-aid-of-construction. Against the workbook's own cost figures the avoided capital is on the order of **$2.0M** ($3.5M medium-voltage case against S3's $1.5M secondary allowance), plus roughly **$1.1M** of battery that exists largely to hold the medium-voltage case down. **The two-site strategy is worth approximately $3M in avoided electrical capital alone**, before any land or structure saving.

### Reconciliation to the workbook and to S3

| Figure | Corrected workbook | S3 | This document |
|---|---|---|---|
| Program modelled | 205,000 SF incl. 55,000 SF depot | 160,000 / 212,000 GSF, no depot | Basis B, per scenario |
| Base building demand | 991.5 kW | 642 kW (6-st) / 776 kW (8-st) | 1,003 kW (SA-B) — higher than S3 because clinical densities are adopted; lower than the workbook's implied figure because no depot systems load applies |
| Charging demand | 2,317 kW | 192 kW | 192 kW (SA-B) / 2,356 kW (SA-A) |
| Service basis | 3,089 kW "managed" (after battery deduction) | 0.80 / 0.97 MVA calculated; **1.5 / 2.0 MVA recommended** | 1,143 kW → **1.4 MVA** (SA-B) |
| Service class | Medium voltage | Not addressed | 480 V secondary for all clinical-anchored cases |

S3's recommended 1.5 MVA target for its 6-storey scheme and this document's 1.4 MVA for SA-B are **materially consistent**, despite arriving from different load densities — S3's lower densities plus a larger headroom factor land in the same place as higher densities plus a standard headroom factor. That convergence is mildly reassuring, but **it is not verification.** Both remain planning targets.

## 7. Recommended electrical phasing

| Phase | Scope | Trigger |
|---|---|---|
| **Phase 1 — install** | 480Y/277 V service sized to **1.5 MVA** for a clinical-anchored scheme (SA-B) or **1.0 MVA** for SA-C. Main switchgear with **spare breaker positions**. Distribution to clinical floors, ground floor, garage. 40 managed Level 2 ports. Elevated electrical rooms above BFE | Construction start |
| **Phase 1 — provide, do not install** | Conduit, pathway and panel capacity to the full EV-ready count (80 ports for SA-B). Spare conduit from switchgear to the roof (future solar/BESS) and to a future imaging zone. Stub-outs and equipment pads for 4 DC fast chargers. Space and structural provision for a second transformer | Construction start — **this is the cheapest capacity the project will ever buy** |
| **Phase 2 — chargers** | Energise ports beyond 40 in blocks of 20 | Sustained utilisation above ~70% on installed ports, or a signed operator |
| **Phase 2 — battery** | 500 kWh BESS for demand-charge management and ride-through | **12 months of actual interval data** showing a demand-charge exposure that justifies it. Do not buy storage on a forecast |
| **Phase 2 — solar** | Rooftop array, canopy where it also provides shade | Roof study completed and tax-credit position resolved (OQ-17) |
| **Phase 3 — imaging** | Dedicated feeder, cooling, shielding | Signed clinical tenant **and** confirmed FPL capacity. Tenant-funded |
| **Phase 3 — DC fast charging** | Hardware into the pre-installed pads | Signed operator **and** confirmed FPL capacity |
| **Second service / dual vault** | Trigger threshold: if total demand approaches **2.5 MVA**, or if any DC fast-charge bank above ~600 kW is contemplated, re-open the medium-voltage question with FPL before committing | Load growth |

**Long-lead procurement.** Utility transformers, medium-voltage switchgear, and large switchboards have carried lead times of **12 months or more** since 2022 and remain volatile. The **FPL application must be filed at or before schematic design**, not at permit. A late application is one of the few things that can delay a certificate of occupancy after construction is otherwise complete.

**Utility milestones, in order:** (1) preliminary load letter to FPL with the planning load; (2) FPL capacity confirmation for the target service; (3) service application with engineered load calculation; (4) transformer and vault siting agreement, including flood elevation; (5) contribution-in-aid-of-construction quotation; (6) equipment release; (7) service installation and energisation.

## 8. What this document cannot resolve

| Item | Required to resolve |
|---|---|
| Actual available capacity at this location | **FPL will-serve / capacity study (MB-03)** — the highest-value single diligence item in the project |
| Clinical load density (5 vs 12.6 W/GSF) | Licensed electrical engineer on the adopted program (OQ-24) |
| Whether a battery may reduce service size | Engineer's EMS design plus FPL concurrence |
| Base flood elevation and equipment elevation | Survey and civil design (MB-05) |
| Service cost ($750K–$5.0M) | FPL contribution-in-aid-of-construction quotation (OQ-25) |
| Demand-charge exposure | FPL rate schedule analysis — **not performed by anyone** |
| Imaging loads | Equipment vendor confirmation |
| Existing service capacity | FPL records request |

**No figure in this document may be presented as an FPL commitment or as an engineered load.**
