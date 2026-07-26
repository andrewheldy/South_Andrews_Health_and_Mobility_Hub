# Master Assumption Register

**Status:** Current operative evidence register · **Last reviewed:** 2026-07-26
**Governing documents:** `AGENTS.md` (evidence classifications), `docs/governance/CLAIMS_AND_EVIDENCE_POLICY.md`
**Related:** [Contradictions Matrix](Contradictions%20Matrix.md) · [Canonical Financial Assumptions](Canonical%20Financial%20Assumptions.md) · [Canonical Construction Assumptions](Canonical%20Construction%20Assumptions.md)

Every material assumption extracted from the repository's sources, with provenance at cell/page level. **Class** uses AGENTS.md classifications: VF = verified fact · SD = source-derived but not independently verified · WA = current working assumption · MO = model output · REC = recommendation · OQ = open question · SUP = superseded assumption · REJ = rejected scenario. **Conf** = confidence H/M/L. **Canonical?**: YES (adopt), DUAL (two live values — never mix bases), CTX (context only), NO (superseded/rejected).

Source IDs: S1–S8 per [Source Inventory](Source%20Inventory.md). Where S2 and S3 give one value each, both are listed as `S2: x | S3: y`.

## 1. Site & property

| ID | Assumption | Value(s) | Source (location) | Class | Conf | Superseded? | Canonical? | Notes |
|---|---|---|---|---|---|---|---|---|
| SITE-01 | Land area | 38,207 SF / 0.88 ac (0.8771) | S6 p.27–28 (ALTA-based); S8 p.3; S2 `Assumptions!B7`; S3 `Assumptions!D6` | VF | H | No | YES | Strongest multi-source fact in repo |
| SITE-02 | Assemblage / folio | 3 parcels, one folio 50-42-15-01-0711; owner Highlands Equity Investments LLC | S6 p.3; S8 p.3 | VF | H | No | YES | Title confirmation still pending (MB-10) |
| SITE-03 | Address string | 901–917 S Andrews Ave (variants 901–915, 917, 905) | S6, S4, S8; S7 reconciliation note | SD | M | Variants | YES (901–917) | See Contradictions A row 7 |
| SITE-04 | Frontages | ±275 ft S Andrews / ±170 ft SW 9th; corner | S6 p.28; S8 p.3 | VF | H | No | YES | Survey (MA-10) controls geometry when recovered |
| SITE-05 | Zoning district | RAC-RPO (Regional Activity Center – Residential and Professional Office) | S6 zoning p.37; S4 | VF | H | No | YES | S7's "Residential Permitted Overlay" expansion is wrong |
| SITE-06 | Future land use | SRAC | S4 Table 2 ("Site Intel FACT") | SD | M | No | YES | Verify at MB-01 |
| SITE-07 | Flood zone | FEMA AE, entire site; map 12011C0557J (7/31/2024) | S6 p.28 | VF | H | No | YES | — |
| SITE-08 | Base flood elevation | ≈ 5 ft | S4 Table 2 | SD | L | No | YES (caveated) | Confirm via survey/civil |
| SITE-09 | QOZ status | Federal Qualified Opportunity Zone | S4/S5 ("Site Intel FACT") | SD | M | No | YES (caveated) | Independently checkable; confirm in diligence |
| SITE-10 | Existing improvements | Three 1959-era commercial buildings (Marty's Bar & Grill + 2), interim use | S6 p.1/32; S8 p.3 | VF | H | No | YES | — |
| SITE-11 | Topography/soils | Moderate slopes; soils appear typical/adequate | S6 p.28 | WA | L | No | YES (caveated) | Geotech pending (MB-06) |
| SITE-12 | Encumbrances | No known adverse easements/encumbrances | S6 p.28 (appraisal assumption) | WA | L | No | YES (caveated) | Title work pending (MB-10) |
| SITE-13 | 2024 assessment / taxes | $1,894,400 assessed; $39,268 taxes | S6 p.4 | SD | H | No | CTX | Assessment ≠ market value |
| SITE-14 | Utilities present | City water/sewer; FPL electric; Florida City Gas; multi-provider telecom | S6 p.27; S4 §3.3 | SD | M | No | YES (capacity unverified) | Capacity ≠ availability; MB-03 |
| SITE-15 | Fiber | Tier-1 connectivity (Hotwire 10 Gbps, AT&T, Lumen, Crown Castle) | S4 §3.3 ("FACT") | SD | M | No | YES (caveated) | Via missing Site Intel report |
| SITE-16 | Hardy Park adjacency (protected north views) | Immediately north; no future neighbor can build out that edge | S8 p.3; S4 | SD | H | No | YES | — |
| SITE-17 | Transit position | Brightline 1.8 mi; future BCR South station south; FLL 2.8 mi; I-95 1.5 mi | S8 p.3; S4/S5 | SD | M | No | YES | BCR South is "planned" — status language required |

## 2. Zoning & entitlement

| ID | Assumption | Value(s) | Source | Class | Conf | Superseded? | Canonical? | Notes |
|---|---|---|---|---|---|---|---|---|
| ZON-01 | Height ceiling | Up to 12 stories (S8/S1) · 110 ft ~10 stories "by right" + 150 ft via bonuses (S4) | S8 p.4; S1 §5; S4 Table 29 | SD (conflicting) | M | No | DUAL → OQ-03/11 | Working line: >6 stories = enhanced/Level III review; ceiling ~12 subject to review |
| ZON-02 | Review trigger | Above 6 stories: enhanced (Level III) site plan & design review | S8 p.4; S1 §5; S6 zoning text ("Heights above 6 floors and up to 12 floors … shall be reviewed") | SD | H | No | YES | Convergent across three sources |
| ZON-03 | Density | 50 du/net acre (~43–44 units on 0.88 ac) | S6 p.37; S4; S8 | SD | H | No | YES (CTX — no residential in scope) | — |
| ZON-04 | Parking requirement | 1 space / 250 SF GFA (office/retail) | S6 p.37; S4; S8 | SD | H | No | YES | City medical-specific method to confirm (MB-01) |
| ZON-05 | Build-to / setbacks | 0 ft build-to on Andrews; 10 ft only abutting residential | S4 Table 29 | SD | M | No | YES (caveated) | Via missing Site Intel |
| ZON-06 | FAR | No max FAR (form-based) per S4/S8; "exact maximum FAR not yet verified" per S1 | S4; S8; S1 §5 | OQ | — | No | OQ | S7's FAR 4/6/8 are analyst scenarios only |
| ZON-07 | Use pathway | Standalone garage/rental not an enumerated principal use → accessory parking to permitted principal use | S8 p.4 | SD | M | No | YES (process logic) | Applies to any parking-heavy program incl. ours |
| ZON-08 | Live Local / TDR / bonus paths | Not yet verified | S1 §5; S4 Ch.10 | OQ | — | No | OQ | MB-18 |
| ZON-09 | Entitlement process | Pre-app → Level III site plan → permit; no rezoning anticipated | S8 pp.4,6 | SD | M | No | YES (working) | MB-01 verifies |

## 3. Acquisition & valuation

| ID | Assumption | Value(s) | Source | Class | Conf | Superseded? | Canonical? | Notes |
|---|---|---|---|---|---|---|---|---|
| ACQ-01 | Working opening-offer input | $8,000,000 ($209/SF) | D-P1; S2 `Assumptions!B18`; S3 `Assumptions!D7`; S8 p.7 | WA (owner-adopted strategy) | H (as strategy input) | No | YES | Not proof of value or offer-submission authority; diligence conditions apply |
| ACQ-02 | Negotiation ceiling / walk-away | **Unresolved**; third-party/context ranges are not adopted | S8 p.7; S3 `Sensitivity!A13:A15` ($8.0/8.75/9.5M cases); D-P1 | OQ/REC context | M | No | OQ | Negotiating authority, maximum price, walk-away, and final conditions require later owner decision |
| ACQ-03 | Appraised value | $11,100,000 ($290/SF), fee simple, as-is 9/18/2025 | S6 p.5 | SD (appraisal opinion) | H (that it was concluded) | No | CTX | Never cite as market-clearing fact |
| ACQ-04 | Prior listing | $12,000,000 (not currently listed) | S6 p.1 | SD | M | Yes (stale anchor) | CTX | — |
| ACQ-05 | Residual supported value (multifamily basis) | $8.96M ($234/SF); coverage 80.7%; "CAUTION — NEGOTIATE" | S7 `Residual Land Value!C36–C45` | MO (analyst) | M | No | CTX | Different program; negotiation context only |
| ACQ-06 | Hub-only residual value | ~$0.81M | S7 `Mobility Hub Economics!C14` | MO (analyst) | M | No | CTX | Shows pure-hub program supports minimal land value |
| ACQ-07 | Closing costs | 2% of land | S3 `Assumptions!D8` | WA | M | No | YES (working) | S2 does not model closing costs — minor gap |
| ACQ-08 | Exposure/marketing time | ~12 months each | S6 p.5–6 | SD | H | No | YES | — |
| ACQ-09 | Appraisal comp critique | 2 comps coerced/assemblage; 2 superior RAC-CC; broad adjusted range | S1 §4; S8 p.7; S6 p.43 (comp data) | SD (interpretation) | H | No | YES | Standing caveat on ACQ-03 |

## 4. Program & massing (DUAL-BASIS FAMILY — never mix columns)

| ID | Assumption | S2 basis (35k plate) | S3 basis (28k/24k plates) | Source | Class | Conf | Canonical? | Notes |
|---|---|---|---|---|---|---|---|---|
| PRG-01 | Floor plate | 35,000 SF uniform | 28,000 SF ground/parking; 24,000 SF office | S2 `Assumptions!B8`; S3 `Assumptions!D9–D11` (from S8 massing) | WA | M/M | **DUAL → OQ-14** | Root of the program conflict |
| PRG-02 | Stack, 6-story | L1 + 3 pkg + 2 office | L1 + 3 pkg + 2 office | S2 `Program!B5,B6`; S3 `Assumptions!D19,D20` | WA | H | YES (stack logic convergent) | Floors convergent; areas differ |
| PRG-03 | Stack, 8-story | L1 + 4 pkg + 3 office | L1 + 4 pkg + 3 office | S2 `Program!C5,C6`; S3 `Assumptions!E19,E20` | WA | H | YES (stack logic) | — |
| PRG-04 | Total GBA 6 / 8 | 210,000 / 280,000 SF | 160,000 / 208,000 SF | S2 `Program!B15,C15`; S3 `P&M!B17,D17` | MO | M | DUAL | — |
| PRG-05 | Office RSF 6 / 8 | 59,500 / 89,250 | 40,800 / 61,200 | S2 `Program!B14,C14`; S3 `P&M!B8,D8` | MO | M | DUAL | Both use 85% efficiency |
| PRG-06 | Office efficiency | 85% | 85% | S2 `Assumptions!B10`; S3 `Assumptions!D13` | WA | M | YES | Convergent |
| PRG-07 | Structured stalls 6 / 8 | 340 / 440 (incl. 40 ground) | 231 / 308 (+18 AV bays excluded) | S2 `Program!B18,C18`; S3 `P&M!B11,D11` | MO | M | DUAL | — |
| PRG-08 | SF per stall | 350 | 360 (vs 340 study figure) | S2 `Assumptions!B9`; S3 `Assumptions!D12`; S8 p.5 (340) | WA | M | DUAL | Test-fit resolves |
| PRG-09 | Parking ratio /1,000 RSF | 5.71 / 4.93 | ~4.5 / ~4.3 (incl. ground leasable in denominator) | S2 `Program!B19,C19`; S3 `P&M!B12,D12` | MO | M | DUAL | Both exceed 4.0 institutional MOB standard |
| PRG-10 | Ground floor program | Café 4,500 + AV 12,000 + lobby/BOH 4,500 + parking/DCFC 14,000 | 10,000 RSF leasable med-tail+café (café 2,500 within) + lobby/AV/loading/systems | S2 `Assumptions!B11–B13`, `Program!B8–B11`; S3 `Assumptions!D14,D15` | WA | M | DUAL | Owner directives embedded in both |
| PRG-11 | AV staging | 12,000 SF L1 zone, separated ingress/egress | 18 secure ground bays, separated lanes | S2 `Assumptions!B12`; S3 `Assumptions!D16` | WA (owner directive) | M | DUAL (representation) | Same intent, different quantification |
| PRG-12 | Edge compute space | 2,000 SF roof penthouse | 1,500 / 2,000 SF data room | S2 `Assumptions!B14`; S3 `Assumptions!D25` | WA | M | DUAL | "Not a hyperscale data center" (S3) |
| PRG-13 | Roof garden | 5,000 SF | 6,000 / 8,000 SF | S2 `Assumptions!B15`; S3 `Assumptions!D26` | WA (owner directive) | M | DUAL | — |
| PRG-14 | Program areas final? | No — planning placeholders | No — "sized during design, not before" | S4 Table 32; S5 Table 27 | VF (of status) | H | YES | Canonical: all areas TBD pending test-fit |
| PRG-15 | Rejected programs | 9-story rental hub ~575–600 stalls; ~43-unit residential; ~130-key hotel | S8 pp.5–6 | REJ | — | NO | Preserved as studied alternatives |

## 5. Construction cost inputs (planning allowances; GC validation pending)

| ID | Assumption | S2 value | S3 value | Source | Class | Conf | Canonical? |
|---|---|---|---|---|---|---|---|
| CST-01 | Demolition | $850K (incl. sitework) | $400K (demo only) | S2 `Assumptions!B19`; S3 `Assumptions!D29`; cf. S7 $350–430K | WA | L | DUAL — definitions differ |
| CST-02 | Flood/stormwater/sitework | (bundled above) | $1.25M / $1.45M | S3 `Assumptions!D30,E30` | WA | L | YES (explicit line preferred) |
| CST-03 | Ground podium shell | (within garage line) | $250/GSF | S3 `Assumptions!D31` | WA | M | DUAL |
| CST-04 | Garage structure | $105/SF (incl. +12% convertibility) | $115/GSF (WGI $98.75 + S FL/HVHZ premium) | S2 `Assumptions!B24`; S3 `Assumptions!D32` | WA | M | DUAL |
| CST-05 | Office shell & core | $310/SF | $290/GSF | S2 `Assumptions!B25`; S3 `Assumptions!D33` | WA | M | DUAL |
| CST-06 | Office/clinical TI | $75/RSF | $135/RSF | S2 `Assumptions!B26`; S3 `Assumptions!D34` | WA | M | DUAL — scope definitions differ; material |
| CST-07 | Retail/med-tail TI | $150/SF café premium | $106.25/RSF ground allowance | S2 `Assumptions!B27`; S3 `Assumptions!D35` | WA | M | DUAL |
| CST-08 | EV conduit rough-in | $400/stall × 100% of stalls | $1,250/port × (ready − installed) | S2 `Assumptions!B28`; S3 `Assumptions!D37` | WA | M | DUAL — different constructs |
| CST-09 | L2 charger installed | $8,000/port × 32 | $7,500/port × 40 | S2 `Assumptions!B29,B30`; S3 `Assumptions!D21,D36` | WA | M | DUAL → OQ-21 |
| CST-10 | DCFC | 8 × $130,000 installed | 0 installed; 4 stub-outs/pads only | S2 `Assumptions!B31,B32`; S3 `E&M!B19` | WA | M | DUAL → OQ-21 |
| CST-11 | Utility service/switchgear | $750K | $1.5M / $1.8M (high-uncertainty placeholder) | S2 `Assumptions!B33`; S3 `Assumptions!D38,E38` | WA | L | DUAL — material; MB-03 |
| CST-12 | AV staging fit-out | $600K | $1.25M / $1.4M | S2 `Assumptions!B34`; S3 `Assumptions!D39,E39` | WA (JUDGMENT-tagged in S2) | L | DUAL |
| CST-13 | Solar installed | 300/340 kW @ $2.60/W | 150/200 kW @ $2.40/W | S2 `Assumptions!B35–B37`; S3 `Assumptions!D23,D40` | WA | M | DUAL |
| CST-14 | Solar ITC | 30% captured | 0% underwritten (48E changed) | S2 `Assumptions!B38`; S3 `E&M!B21` | WA (conflicting) | — | **DUAL → OQ-17 (material)** |
| CST-15 | 30C charger credit | (not separated) | 0% — deadline 6/30/2026 | S3 `E&M!B20` + `Sources!A12` | SD | M | YES (S3 position, pending counsel) |
| CST-16 | BESS | 600 kWh @ $520/kWh | 500/1,000 kWh @ $600/$550 | S2 `Assumptions!B39,B40`; S3 `Assumptions!D24,D41` | WA | M | DUAL |
| CST-17 | Edge infrastructure | $450K shell (tenant fit-out) | $1.25M / $1.75M fitted | S2 `Assumptions!B41`; S3 `Assumptions!D42` | WA (JUDGMENT) | L | DUAL — scope differs |
| CST-18 | Roof garden cost | $175K | $90/SF ($540K / $720K) | S2 `Assumptions!B42`; S3 `Assumptions!D43` | WA (JUDGMENT) | L | DUAL |
| CST-19 | Soft costs | 18% of hard | 8% A&E + 5% permits + 4% owner = 17% + leasing $25/RSF | S2 `Assumptions!B45`; S3 `Assumptions!D45–D47,D49` | WA | M | DUAL |
| CST-20 | Contingency | 7.5% | 8% | S2 `Assumptions!B46`; S3 `Assumptions!D48` | WA | M | DUAL |
| CST-21 | Developer fee | 4% of hard+soft | (inside 4% owner-costs line) | S2 `Assumptions!B47`; S3 `Assumptions!D47` | WA | M | DUAL |
| CST-22 | Construction duration | 18 / 21 mo (construction) | 30 / 34 mo (build + lease-up) | S2 `Assumptions!B20,B21`; S3 `Assumptions!D27,E27` | WA | M | DUAL — different definitions |
| CST-23 | Convertibility premium | +12% inside $105/SF | (in $115 premium & flat-deck params) | S2 `Assumptions!E24`; S4 Table 34 (10–15% low-mid, up to ~32% full) | SD/WA | M | YES (accept low-mid premium — S4 JUDGMENT adopted as REC) |
| CST-24 | Structural system | CIP PT flat plates, external removable ramps, 12-ft F2F, 50–100 psf, universal grid | Same (S3/S4 convergent design principles) | S4 Ch.5/Table 33; S2 `Assumptions!E24`; S3 `P&M!F9` | REC (adopted design intent) | M | YES |

## 6. Financing

| ID | Assumption | S2 | S3 | Source | Class | Conf | Canonical? |
|---|---|---|---|---|---|---|---|
| FIN-01 | Construction LTC | 65% | 60% | S2 `Assumptions!B48`; S3 `Assumptions!D50` | WA | M | DUAL |
| FIN-02 | Loan rate | 7.5% | 8.0% | S2 `Assumptions!B49`; S3 `Assumptions!D51` | WA | M | DUAL |
| FIN-03 | Avg balance drawn | 55% | 55% | S2 `Assumptions!B50`; S3 `Assumptions!D52` | WA | M | YES (convergent) |
| FIN-04 | Financing fee | — | 1.5% of loan | S3 `Assumptions!D53` | WA | M | YES (S3 more complete) |
| FIN-05 | Capital-stack avenues | QOZ equity + construction debt; P3/MPO grants & TIF to test (not load-bearing); tax-exempt structures only with nonprofit partner | S4 §11.2 | REC | M | — | YES (as strategy to test) |

## 7. Revenue & operations

| ID | Assumption | S2 | S3 | Source | Class | Conf | Canonical? |
|---|---|---|---|---|---|---|---|
| REV-01 | Medical office rent (NNN) | $36/RSF ("FACT" — overclaim; reclassified SD) | $50/RSF (illustrative) | S2 `Assumptions!B53`; S3 `Assumptions!D55` | SD vs WA | L | **DUAL → OQ-15 (material)** |
| REV-02 | Office stabilized vacancy | 7% | 7% (93% occ.) | S2 `Assumptions!B54`; S3 `Assumptions!D56` | WA | M | YES |
| REV-03 | Retail/med-tail rent | $42/SF on 4,500 SF | $45/RSF on 10,000 RSF @ 95% occ. | S2 `Assumptions!B55`; S3 `Assumptions!D57,D58` | WA | M | DUAL |
| REV-04 | Parking revenue | $2,400/space/yr blended (all spaces); opex 30% | $275/stall/mo × 55% monetized; opex 35% pooled | S2 `Assumptions!B56,B57`; S3 `Assumptions!D60,D61,D65` | WA | L | DUAL; survey basis missing (MA-16); MB-09 |
| REV-05 | EV net income | $120,000/yr (JUDGMENT) | $250/port/mo × 40 = $120,000/yr | S2 `Assumptions!B58`; S3 `Assumptions!D62` | WA | M | YES ($120K/yr, utilization-sensitive) |
| REV-06 | AV staging revenue in base | $0 (toggle OFF; no LOI) | $194,400/yr included (18 × $900/mo) | S2 `Assumptions!B63`; S3 `Assumptions!D63` + `F&R!D11` | S2: governance-aligned; S3: WA in tension | — | **S2 treatment canonical → OQ-22**; S3 base NOI ex-AV ≈ $2.15M/$2.97M (recomputed, MO-REC) |
| REV-07 | AV lease rate (if signed) | $25/SF/yr × 12,000 SF = $300K/yr (FORECAST) | $900/bay/mo equivalent | S2 `Assumptions!B62`; S3 `Assumptions!D63` | FORECAST | L | CTX (upside only, never base) |
| REV-08 | Edge/data rent | $30K/yr allowance (FORECAST) | $55/SF/yr × 1,500–2,000 SF ≈ $77–102K EGI | S2 `Assumptions!B61`; S3 `Assumptions!D59`, `F&R!D8` | FORECAST/WA | L | DUAL |
| REV-09 | Solar value | 1,450 kWh/kW-yr × $0.13/kWh | 1,500 kWh/kW-yr factor | S2 `Assumptions!B59,B60`; S3 `E&M!B15` | WA | M | DUAL (minor) |
| REV-10 | Management fee | 3% of EGI | (within 25% office-opex ratio) | S2 `Assumptions!B64`; S3 `Assumptions!D64` | WA | M | DUAL (structure differs) |
| REV-11 | Non-recoverable opex | $1.50/SF GBA | 25% office/retail/data EGI; 35% parking/EV/AV EGI | S2 `Assumptions!B65`; S3 `Assumptions!D64,D65` | WA | M | DUAL |
| REV-12 | Shared-parking model | Medical by day / public+commuter off-peak; gateless LPR | S4 §H, Table 25 | REC | M | — | YES (operating concept) |
| REV-13 | Lease-up ramp | 50% Yr1 / 90% Yr2 / stabilized Yr3 | (30/34-mo build+lease-up period) | S2 `Assumptions!B72,B73`; S3 `Assumptions!D27` | WA | M | DUAL |

## 8. Exit, hold & returns

| ID | Assumption | S2 | S3 | Source | Class | Conf | Canonical? |
|---|---|---|---|---|---|---|---|
| EXT-01 | Exit cap rate | 6.25% | 7.25% | S2 `Assumptions!B69`; S3 `Assumptions!D67`; cf. S7 5.35%/7.5%; S6 market ~5.9–6.0% | WA | L | **DUAL → OQ-18 (material)** |
| EXT-02 | NOI growth | 2.5%/yr | — | S2 `Assumptions!B68` | WA | M | YES (working) |
| EXT-03 | Hold period | 10 yrs (QOZ-aligned) | — (implied) | S2 `Assumptions!B71`; S4/S5 (≥10 yrs) | WA | H | YES |
| EXT-04 | Target yield on cost | 150+ bps over 6.25% cap | 7.0% before tax incentives | S2 `Summary!D9`; S3 `Assumptions!D66` | WA | M | DUAL |
| EXT-05 | Cost of sale | 2% | — | S2 `Assumptions!B70` | WA | M | YES (working) |
| EXT-06 | **Feasibility outcome** | YoC 3.83%/4.02%; dev profit −$27.7M/−$33.9M; IRR 1.24%/1.85%; multiple 1.11×/1.16× | Core YoC 3.83%/4.07%; partner gap $1.89M/$2.23M core, $2.58M/$3.23M tenant-ready; value gap −$28.1M…−$47.7M | S2 `Returns!B13–B17,B27–B31`; S3 `F&R!D21–E28` | **MO — canonical convergent finding** | H (as model output) | **YES** — base program does not reach institutional yield without partner support/grants/above-market revenue |

## 9. Energy loads & infrastructure

| ID | Assumption | Value(s) | Source | Class | Conf | Canonical? |
|---|---|---|---|---|---|---|
| NRG-01 | L2 nameplate | 9.6 kW/port | S3 `Assumptions!D69` (via missing MA-11 load model) | SD | M | YES (working) |
| NRG-02 | Managed charging coincidence | 50% → 40-port peak ≈ 192 kW | S3 `Assumptions!D70`, `E&M!F7` | WA | M | YES (working) |
| NRG-03 | Office peak density | 5 W/GSF (excl. imaging/ASC/kitchens) | S3 `Assumptions!D71` | WA | M | YES (working) |
| NRG-04 | Ground-floor peak | 6 W/GSF | S3 `Assumptions!D72` | WA | M | YES (working) |
| NRG-05 | Garage ancillary peak | 0.5 W/GSF | S3 `Assumptions!D73` | WA | M | YES (working) |
| NRG-06 | Service headroom | 25% before future DCFC | S3 `Assumptions!D74` | WA | M | YES (working) |
| NRG-07 | Recommended service target | 1.5 MVA (6-story) / 2.0 MVA (8-story) — "preliminary target only; FPL and engineer must confirm" | S3 `Assumptions!D75,E75` | WA | L | YES (caveated; not an FPL load letter) |
| NRG-08 | EV-ready totals | 80 ports (6-story) / 120 (8-story); install 40 | S3 `Assumptions!D22,E22,D21` | WA (owner directive ~40) | M | YES (working) |
| NRG-09 | Battery role | Peak shaving + resilience, not primary power / not generator replacement | S3 `E&M!A2,G16` | REC | H | YES |
| NRG-10 | Grid-redundancy rationale | 2020 Sistrunk substation fire argues for on-site redundancy | S4 §3.3 | SD | M | CTX |

## 10. Healthcare demand & partnership (all partners prospective)

| ID | Assumption | Value(s) | Source | Class | Conf | Canonical? |
|---|---|---|---|---|---|---|
| HC-01 | Broward Health MOB | 188,000 SF, 8-story, adjacent campus, opening 2027 | S5 Table 19; S4 §1.2 | SD (via missing Market Study) | M | YES (caveated; MB-17) |
| HC-02 | GME program | 365 residents/fellows — largest class in system history | S5 Table 19 | SD | M | YES (caveated) |
| HC-03 | Physician shortage | 18,000+ FTE projected statewide | S5 Table 6 | SD | M | CTX |
| HC-04 | Consolidation spillover thesis | Hospital consolidation displaces independent/step-down practices needing nearby space | S4 §1/§7; S5 | SD/REC | M | YES (thesis) |
| HC-05 | MOB vacancy caveat | 10.4% county MOB vacancy — near-term softening | S4 §7 (Market Study cite) | SD | M | YES (must accompany demand claims) |
| HC-06 | Co-working anchor strategy | Master-lease upper floors to medical co-working operator (e.g., operators like "Lina" cited); LOI = OQ-08 | S4 §7 | REC | M | YES (strategy; operator unidentified) |
| HC-07 | Med-tail mix | Pharmacy, urgent care, DME, PT/rehab, wellness/medspa, F&B | S4 Table 37 | REC | M | YES |
| HC-08 | Demographics | Affluent 33316 catchment ($180k+ HHI cited) | S4 Table 37 | SD | L | CTX (verify in MB-07/MB-17) |
| HC-09 | Positioning | Complementary to Broward Health MOB (flexibility + parking surplus), not competitive shell space | S4 §7.2; S5 | REC | H | YES |
| HC-10 | Imaging gating | Imaging/diagnostics only after FPL capacity confirmed | S4 Table 37/§13J | REC | H | YES |
| HC-11 | Parking ratio for clinical | 4.0–5.0 spaces / 1,000 SF clinical | S4 Table 17 (benchmark ASSUMPTION); S2 `Program!D19` | WA | M | YES (target) |

## 11. Mobility & AV context

| ID | Assumption | Value(s) | Source | Class | Conf | Canonical? |
|---|---|---|---|---|---|---|
| MOB-01 | AV operators status | Waymo Miami/Orlando active; Zoox Miami; Tesla Robotaxi Miami; Freebee regional — "No partnership or site demand assumed" (all four) | S3 `Sources!A14–A17` | SD | M | YES (context-only rule) |
| MOB-02 | AV revenue rule | Never underwritten in base case; activation gated on signed operator/demand trigger | AGENTS.md; S2 toggle; S4 Decision-003 (as cited) | VF (governance) | H | YES |
| MOB-03 | Conduit strategy | Conduit to 100% of stalls in Phase 1; energize 10–20% initially (S4) / install 40 (owner directive) | S4 Ch.8/9; S2 `Assumptions!E28`; S3 `Assumptions!F22` | REC/WA | H | YES (conduit rule); charger count OQ-21 |
| MOB-04 | Ingress/egress principles | Andrews frontage pedestrian/retail; secondary streets for separated AV in/out; AV loop isolated before public ramp; FPL zone independently accessible | S3 `P&M!A33–A37`, `E&M!A24–A28`; S4 Ch.6 | REC | H | YES (design intent, subject to traffic study) |
| MOB-05 | Mobility-hub brief counts | 200 transient / 100 fleet / 50 EV | S7 `Assumptions!B36–B38` ("per brief") | SUP (superseded program brief) | L | NO — historical brief, not current program |

**Register totals:** 96 assumptions: 10 VF · 24 SD · 41 WA · 8 MO · 9 REC · 2 OQ-class · 1 SUP · 1 REJ (plus per-row DUAL flags). Every DUAL row traces to an escalation in [Open Questions](Open%20Questions.md).
