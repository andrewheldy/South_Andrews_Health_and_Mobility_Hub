# Construction Budget Basis

**Status:** Planning-level budget basis; **no scheme adopted** · **Prepared:** 2026-07-27
**External-use status:** internal_only
**Estimate classification:** AACE International **Class 5** (concept screening, 0–2% project definition). Expected accuracy range **−30% to +50%**.
**Pricing date:** Q3 2026 · **Geographic basis:** Fort Lauderdale, Broward County, Florida — HVHZ, FEMA Zone AE
**Related:** [Program and Scenario Reconciliation](../planning/Program%20and%20Scenario%20Reconciliation.md) · [Contradiction and Validation Register](../planning/Contradiction%20and%20Validation%20Register.md) · [Electrical Basis of Design](../technical/Electrical%20Basis%20of%20Design.md)
**Derived model:** [`models/working/build_integrated_development_model.py`](../../models/working/build_integrated_development_model.py) → `South_Andrews_Integrated_Development_Model.xlsx`, `integrated-development-model.json`

> **This is not a cost estimate.** It is a planning-level budget basis assembled from two unaudited project models and published benchmarks. There is **no contractor pricing, no design documentation, no geotechnical report, no utility study, and no environmental report** in the repository. Every unit rate is a current working assumption pending GC validation (MB-16). Confidence is **low** on any single line and **medium** only on the order of magnitude of the totals.

---

## 1. Basis, exclusions, and confidence

### Stated basis

| Element | Adopted for this budget | Alternative on record |
|---|---|---|
| Geometry | Basis B — 28,000 GSF ground/parking plate, 24,000 GSF office plate, 360 GSF/stall (S3 `Assumptions!D9:D12`) | Basis A — 35,000 SF uniform plate, 350 SF/stall (S2 `Assumptions!B8,B9`). **Never mixed** (OQ-14) |
| Unit costs | S3 `Assumptions!D29:D43` — 2026 WGI-benchmarked | S2 `Assumptions!B24:B42`. Deltas at §6 |
| Soft-cost structure | S3 — 8% A&E + 5% permits/fees + 4% owner + 8% contingency = **25% of hard**, plus $25/office RSF leasing | S2 — 18% soft + 7.5% contingency + 4% developer fee on hard+soft ≈ **29.7% of hard**. Structures differ; totals differ materially |
| Financing | 60% LTC, 8.0% all-in, 55% average balance, 1.5% fee (S3 `Assumptions!D50:D53`) | 65% LTC, 7.5%, no fee modelled (S2). Lender term sheet resolves |
| Tax credits | **0% underwritten** (S3 `Energy & Mobility!B20,B21`) | S2 nets 30% ITC from solar. Rejected as the interim rule (OQ-17) |
| Land | $8,000,000 — the D-P1 working opening-offer input. An acquisition-strategy input only; not proof of value, not a price ceiling, walk-away price, or transaction authority | Appraised $11.1M (S6); prior listing $12.0M; residual context $8.96M (S7) |

### Explicit exclusions

Not carried in any figure below: land carry beyond the modelled construction period · property-tax reassessment following sale (S6 p.40 records reassessment **is** triggered) · owner's project-management staffing · imaging equipment purchase · medical gases · tenant-funded kitchen and clinical equipment · off-site depot land or construction · operating reserves beyond lease-up · flood, HVHZ and coastal insurance premiums (never quantified in any source — MB-12) · escalation beyond the Q3 2026 pricing date · builder's risk and payment/performance bonds (assumed inside the contractor's general conditions and fee, which are themselves inside the unit rates) · unusual title, transfer or financing costs.

### Confidence by line

| Confidence | Lines |
|---|---|
| **Medium** | Structured parking concrete (benchmarked to WGI 2026 national median $98.75/SF, adjusted); office shell & core; ground podium; TI allowances; soft-cost percentages; financing |
| **Low** | Demolition; flood/stormwater sitework; AV/mobility fit-out; edge data infrastructure; roof garden; solar; BESS |
| **Very low — placeholder only** | **FPL service / transformer / switchgear.** Three values exist across sources spanning $750K–$5.0M with no engineered basis (CVR-16 / OQ-25) |
| **Unquantified — new allowance** | **Environmental remediation.** Carried at $250,000. S6 p.10 lists a Phase I **and a Phase II** ESA among documents reviewed; S6 p.28 states no environmental information was provided; neither report is in the repository. A Phase II is normally commissioned only after a Phase I identifies a recognised environmental condition (CVR-44 / OQ-28) |

## 2. Acquisition and transaction

| Line | SA-A | SA-B | SA-C | SA-C0 | Basis |
|---|---|---|---|---|---|
| Land purchase | $8,000,000 | $8,000,000 | $8,000,000 | $8,000,000 | D-P1 working opening-offer input — strategy input only, not proof of value or authority |
| Closing / acquisition costs (2%) | $160,000 | $160,000 | $160,000 | $160,000 | S3 `Assumptions!D8`; excludes unusual title, transfer or financing costs |
| **Subtotal** | **$8,160,000** | **$8,160,000** | **$8,160,000** | **$8,160,000** | |

**Not carried and required before any offer:** legal and land-use counsel retainers · title commitment and premium · updated ALTA survey (the survey of record is dated 2015 — MA-10) · lender costs and appraisal · acquisition due-diligence budget (Phase I refresh, geotechnical, zoning verification) · **carrying cost between closing and construction start** · **property-tax reassessment**, which S6 p.40 confirms is triggered by sale. Current assessment is $1,894,400 against an $8.0M–$11.1M value range; a reassessment toward market would multiply the current $39,268 tax bill several times over. This is a real and unmodelled holding cost in any land-bank strategy.

## 3. Core hard costs

Line-item detail is in the derived workbook. Summary by scenario:

| Line | SA-A | SA-B | SA-C | SA-C0 |
|---|---|---|---|---|
| Demolition and disposal | $400,000 | $400,000 | $400,000 | $400,000 |
| Environmental remediation allowance | $250,000 | $250,000 | $250,000 | $250,000 |
| Flood / stormwater / resilient sitework | $1,450,000 | $1,250,000 | $1,150,000 | $900,000 |
| Site paving, curb, lighting, landscape, streetscape | — | — | — | $850,000 |
| Ground podium + active frontage shell | $7,000,000 | $7,000,000 | $7,000,000 | $4,760,000 |
| Structured parking concrete + flat decks | $16,100,000 | $9,660,000 | $6,440,000 | — |
| Office / medical-ready shell and core | $13,920,000 | $13,920,000 | $6,960,000 | — |
| Installed networked Level 2 chargers (40) | $300,000 | $300,000 | $300,000 | $300,000 |
| EV-ready expansion conduit / pathways | $100,000 | $50,000 | $25,000 | $37,500 |
| FPL service / transformer / switchgear allowance | $3,500,000 | $1,500,000 | $900,000 | $600,000 |
| Mobility circulation, gates, security, staging | $2,400,000 | $1,250,000 | $750,000 | $600,000 |
| Rooftop / canopy solar | $800,000 | $360,000 | $240,000 | $400,000 |
| Battery energy storage system | $1,100,000 | $300,000 | — | — |
| Edge data / teleoperations infrastructure | $1,750,000 | $1,250,000 | — | — |
| Staff rooftop garden / shade amenity | $720,000 | $540,000 | — | — |
| **Core hard subtotal** | **$49,790,000** | **$38,030,000** | **$24,415,000** | **$9,097,500** |

### Unit rates and their sources

| Component | Rate | Source and rationale |
|---|---|---|
| Structured parking | **$115/GSF** | S3 `Assumptions!D32`. WGI 2026 national median $98.75/SF, adjusted upward for South Florida, HVHZ, flat-floor adaptability and mixed-use complexity. Yields **$41,818/gross stall** at 360 GSF/stall — against WGI's national median of $33,300/space |
| Ground podium / active frontage | **$250/GSF** | S3 `Assumptions!D31`. Concrete podium, façade, lobby, service, flood-resistant ground level |
| Office / medical-ready shell & core | **$290/GSF** | S3 `Assumptions!D33`. HVHZ shell/core with elevated MEP backbone. S2 carries $310. Range $290–310 may be quoted with both citations; **never a midpoint** |
| Single-storey medical shell (SA-C0) | **$340/GSF** | Analyst allowance for an elevated, HVHZ, medical-capable single-storey structure |
| Level 2 charger installed | **$7,500/port** | S3 `Assumptions!D36`, DOE benchmarks. S2 carries $8,000 |
| EV-ready rough-in | **$1,250/port** | S3 `Assumptions!D37`. Conduit, pathway, panel allocation. S2 uses a different construct ($400/stall to 100% of stalls) |
| Solar | **$2.40/W** rooftop; **$4.00/W** canopy | S3 `Assumptions!D40` for rooftop. Canopy rate adopted from the corrected electrical workbook, which correctly identifies that canopy structures cost materially more (CVR-17) |
| BESS | **$600/kWh** ≤500 kWh; **$550/kWh** ≥1,000 kWh | S3 `Assumptions!D41,E41` |
| Roof garden | **$90/SF** | S3 `Assumptions!D43` |

### Convertibility and structural premium

The convertible-parking strategy (flat plates, ~12 ft floor-to-floor, 50–100 psf design loading, universal grid, removable external ramps) is an adopted design intent (CAN-030, CST-24) carrying a premium of **10–15%** at the low-to-mid range, per S4 Table 34, with a full-conversion case cited as high as ~32%. S2 embeds +12% inside its $105/SF rate; S3 embeds it inside the $115/SF premium. **The premium is not shown as a separate line in either model and cannot be independently extracted.** A GC must price convertible and conventional decks side by side (MB-16 / OQ-10) so the option's cost is visible before it is bought.

**EV structural loading.** Battery-electric vehicles are materially heavier than the passenger-car loading assumed in older garage design. Where a deck is intended to carry a fleet or dense charging, the design live load and the fatigue case both need review. This is not addressed in any source and is a design-phase item.

## 4. Tenant improvements

| Line | SA-A | SA-B | SA-C | SA-C0 |
|---|---|---|---|---|
| Office / clinical TI — $135/RSF | $5,508,000 | $5,508,000 | $2,754,000 | — |
| Ground med-tail / café TI — $106.25/RSF | $1,062,500 | $1,062,500 | $1,275,000 | $1,487,500 |
| **TI subtotal** | **$6,570,500** | **$6,570,500** | **$4,029,000** | **$1,487,500** |

The **$135/RSF** office/clinical allowance (S3 `Assumptions!D34`) is described as "moderate medical-office TI." S2 carries **$75/RSF** for "medical-capable spec suites," citing a market range of $60–90. The gap is **material** (~$2.4–3.7M on a 6-storey scheme) and is a scope-definition difference, not a pricing difference: spec office suites and clinical-capable suites are different products (OQ / CST-06).

**Separated deliberately and NOT in any figure above:**

| Scope | Treatment |
|---|---|
| Warm shell / medical office shell | Inside the $290/GSF shell & core |
| Turnkey clinical suites | Above the $135/RSF allowance; tenant- or operator-funded |
| Medical co-working fit-out | Operator-funded; no operator identified (OQ-08) |
| Urgent care | Tenant-funded above allowance |
| **Imaging-ready shell** | **Not carried.** Requires structural slab reinforcement, shielding provisions, dedicated cooling, and vibration control |
| **Imaging equipment (MRI/CT/X-ray)** | **Not carried and should not be.** Owner purchase is not required by any operating model on record. Vendor-financed or tenant-funded |
| Medical gases, enhanced plumbing | Not carried; use-specific |
| Emergency power / continuity | Not carried beyond life-safety inside shell & core. Clinical continuity requirements are operator-driven |
| Infection-control and healthcare-code premiums | Not carried; applies only to licensed clinical space |
| Pharmacy, DME, wellness, café, food service | Inside the ground TI allowance, which is a landlord allowance only. Operator kitchen and medical equipment is tenant-funded |

## 5. Soft costs, financing, and totals

| Line | SA-A | SA-B | SA-C | SA-C0 |
|---|---|---|---|---|
| A&E (8% of core hard) | $3,983,200 | $3,042,400 | $1,953,200 | $727,800 |
| Permits / impact / utility fees (5%) | $2,489,500 | $1,901,500 | $1,220,750 | $454,875 |
| Developer / legal / insurance / owner (4%) | $1,991,600 | $1,521,200 | $976,600 | $363,900 |
| Construction contingency (8%) | $3,983,200 | $3,042,400 | $1,953,200 | $727,800 |
| **Core soft subtotal** | **$12,447,500** | **$9,507,500** | **$6,103,750** | **$2,274,375** |
| Construction interest + financing fees (core) | $5,899,310 | $4,177,312 | $2,220,160 | $863,309 |
| **Core all-in development cost** | **$76,296,810** | **$59,874,812** | **$40,898,910** | **$20,395,184** |
| **Tenant-ready all-in development cost** | **$86,303,671** | **$69,800,422** | **$46,763,515** | **$22,336,743** |
| Cost excluding land (core) | $68,296,810 | $51,874,812 | $32,898,910 | $12,395,184 |
| Modelled duration (build + initial lease-up) | 34 mo | 30 mo | 22 mo | 16 mo |

**Contingency is not double-counted.** A single 8% construction contingency is applied to hard cost. There is no separate design contingency and no separate owner contingency in this structure — which is itself a weakness at Class 5. A defensible Class 5 budget would normally carry design contingency **in addition to** construction contingency. Adding a 5% design contingency would increase core all-in cost by roughly $2.6M (SA-A), $2.0M (SA-B), $1.3M (SA-C). **This is a recommended correction at model vNext and is not applied above.**

## 6. Unit-cost metrics

| Metric | SA-A | SA-B | SA-C | SA-C0 |
|---|---|---|---|---|
| Core all-in per GSF | $353 | $374 | $379 | $1,457 |
| Parking structure per gross stall | $41,818 | $41,818 | $41,818 | n/a |
| **Core all-in per operational fleet/staging position** | **$544,977** | **$3,326,378** | **$1,514,774** | **$1,274,699** |
| Tenant-ready per clinical + ground RSF | $1,699 | $1,374 | $1,443 | $1,595 |
| Land as % of core all-in | 10.5% | 13.4% | 19.6% | 39.2% |

The **cost per operational fleet position** is the metric that most clearly exposes the mobility thesis. At **$545,000 per usable fleet position**, structured fleet capacity on South Andrews is not a rational way to house vehicles. An off-site industrial depot at benchmark land and construction rates houses a vehicle for a small fraction of that. This single ratio is the strongest quantitative argument for the two-site strategy.

## 7. Cost sensitivity

Factors applied per S3 `Sensitivity!A6:D8`: low = 0.90 hard / 0.90 soft / 7.0% rate; high = 1.12 hard / 1.15 soft / 9.5% rate.

| Case | SA-A | SA-B | SA-C | SA-C0 |
|---|---|---|---|---|
| Low | $68,951,486 (3.23%) | $54,344,245 (3.46%) | $37,456,315 (3.28%) | $19,126,796 (2.91%) |
| **Base** | **$76,296,810 (2.92%)** | **$59,874,812 (3.14%)** | **$40,898,910 (3.00%)** | **$20,395,184 (2.73%)** |
| High | $85,893,197 (2.59%) | $67,077,146 (2.80%) | $45,350,903 (2.71%) | $22,029,740 (2.53%) |

Yields shown are core, parking construct P1, AV excluded. **No case in any scenario approaches the 7.0% target.** The spread between low and high cases is roughly $17M on SA-A and $13M on SA-B — larger than the entire land basis.

## 8. Basis A cost comparison

Restating SA-B's components on S2's unit rates, holding Basis B geometry constant, isolates the pure unit-cost disagreement:

| Component | S3 rate | S2 rate | Delta on SA-B geometry |
|---|---|---|---|
| Structured parking (84,000 GSF) | $115/GSF = $9,660,000 | $105/GSF = $8,820,000 | −$840,000 |
| Office shell & core (48,000 GSF) | $290/GSF = $13,920,000 | $310/GSF = $14,880,000 | +$960,000 |
| Office TI (40,800 RSF) | $135/RSF = $5,508,000 | $75/RSF = $3,060,000 | −$2,448,000 |
| Demolition | $400,000 + $1,250,000 sitework | $850,000 bundled | −$800,000 (definitional) |
| Soft-cost structure | 25% of hard | ~29.7% of hard | +~$1.8M on S2 basis |

The disagreements substantially offset on hard cost; the **material** divergence is TI scope (spec vs clinical-capable) and soft-cost structure. Neither is resolvable without GC pricing (MB-16) and a tenant-standard decision.

**This is a rate comparison only.** A true Basis A budget would also change every area and stall count and would produce materially larger totals — S2's own 6-storey total development cost is **$71,515,960** against S3's $59,538,875, on a program 50,000 GSF larger. The two must never be blended.

## 9. Deferrable and stranded cost

### What can be deferred

| Item | SA-B value | Trigger for installation |
|---|---|---|
| Chargers beyond the initial 40 | $50,000 conduit now; hardware later | Utilisation data or a signed operator |
| DC fast charging | Stub-outs and pads only; hardware $0 | Operator commitment + confirmed FPL capacity |
| Battery energy storage | $300,000 | Demand-charge data after 12 months of operation |
| Edge / teleoperations data room | $1,250,000 | A signed tenant. **Nothing in the repository supports building this speculatively** |
| Roof garden | $540,000 | Amenity decision; can follow lease-up |
| Solar beyond a base array | $360,000 | Tax-credit clarity (OQ-17) and roof study |
| **Total deferrable** | **≈ $2.5M** | |

### What becomes stranded if the off-site depot never lands

| Item | Exposure |
|---|---|
| Mobility circulation, gates, security, staging | $1,250,000 |
| Edge data / teleoperations infrastructure | $1,250,000 |
| EV-ready conduit beyond installed ports | $50,000 |
| Incremental FPL service above a clinical-only requirement | $600,000 |
| **Total at risk** | **$3,150,000** |

Roughly **$3.15M of SA-B's budget exists only to serve a mobility operation that depends on a depot site the owner does not control.** None of it should be committed before the depot-site gate closes.

## 10. Minimum functional cost

| Question | Answer |
|---|---|
| Minimum to make South Andrews function as a staging and implementation site, no AV deployment | **$4,986,750 excluding land** (site enablement package — see [Program and Scenario Reconciliation](../planning/Program%20and%20Scenario%20Reconciliation.md) §6) |
| Minimum with a credible income-producing building | **$20,395,184 core all-in including land** (SA-C0) |
| Minimum with clinical space and expansion capability | **$40,898,910 core all-in including land** (SA-C) |
| Leading full-build hypothesis | **$59,874,812 core / $69,800,422 tenant-ready** (SA-B) |
| Maximum-fleet case | **$76,296,810 core / $86,303,671 tenant-ready** (SA-A) |

The assignment's concern about "an unjustified $75 million–$100 million speculative development" is well founded: **SA-A tenant-ready lands at $86.3M, and S2's Basis A 8-storey scheme reaches $94,974,410.** Both sit squarely in that range and neither clears any return test.

## 11. What must happen before these numbers mean anything

1. **GC pricing** on two schemes, with convertible and conventional decks priced separately (MB-16).
2. **FPL will-serve study.** A single line currently spans $750K–$5.0M (CVR-16 / OQ-25).
3. **Recover the Phase I and Phase II ESAs.** The $250,000 remediation allowance is a placeholder against an unknown (CVR-44 / OQ-28).
4. **Geotechnical borings.** No foundation type has been established; deep foundations are not carried anywhere.
5. **Architect test-fit** to fix areas and stall counts (MB-02 / OQ-14).
6. **Insurance quotes** — flood, HVHZ, coastal. Flagged as a high risk in every source and quantified in none (MB-12).
7. **Tax counsel** on §48E and §30C (MB-13 / OQ-17).
8. **Add a design contingency** at model vNext (§5).
