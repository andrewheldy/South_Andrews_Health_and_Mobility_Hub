# Program and Scenario Reconciliation

**Status:** Current scenario comparison; **no scheme adopted** · **Prepared:** 2026-07-27
**External-use status:** internal_only
**Governing documents:** `AGENTS.md` (scenario discipline), [`docs/governance/SOURCE_AUTHORITY.md`](../governance/SOURCE_AUTHORITY.md)
**Related:** [Current Development Program](Current%20Development%20Program.md) · [Contradiction and Validation Register](Contradiction%20and%20Validation%20Register.md) · [Construction Budget Basis](../cost/Construction%20Budget%20Basis.md) · [Two-Site Operating Plan](../technical/Two-Site%20Operating%20Plan.md)

> **Stated modelling basis.** Scenarios SA-A through SA-D are built on **Basis B** — 28,000 GSF ground/parking plate, 24,000 GSF office plate, 360 GSF/stall, 85% office efficiency (S3 `Assumptions!D9:D12`, derived from S8's massing study). This is a **stated basis, not an adopted program.** OQ-14 remains unresolved. Basis A (S2, 35,000 SF uniform plate) would change every area, stall and dollar figure below. **The two bases are never mixed.** A Basis A restatement is a required output of the test-fit (MB-02).
>
> All areas, stall counts and diagrams here are **planning-level model outputs**, not architectural drawings. Nothing here is approved, permitted, or engineered.

---

## 1. Why gross stalls are not fleet capacity

Every scenario below reports a **stall waterfall** rather than a single stall count. The distinction is the difference between a defensible plan and a misleading one.

A structured stall is only available for fleet or public use after the building has satisfied its own parking obligation. The standard in evidence is **1 space per 250 SF GFA** for professional office, retail sales and retail service (S6 p.37, corroborated by S4 and S8). Applied to a scheme's own office and med-tail area, that obligation consumes stalls before any mobility function is served.

Further deductions then apply, none of which appear in either current model:

| Deduction | Basis | Typical magnitude |
|---|---|---|
| **Code-required parking** | 1 per 250 SF GFA on office + med-tail (S6 p.37) | The largest single deduction |
| **Secure-zone boundary loss** | Gating a fleet zone inside a public deck sterilises stalls at the boundary and at the control point | ~6% of each gated level |
| **Cleaning / turnaround equivalent** | Vehicles being wiped down, charged, staged or held occupy positions that cannot be simultaneously let | 4–12 stall-equivalents |
| **AV manoeuvring reserve** | Driverless circulation needs wider swept paths and queue relief than a code aisle provides | 4–10 stall-equivalents |
| **ADA** | Federal minimum; drawn from within the code allocation, not additive | 2% of gross above 100 stalls |

Ramps, cores, and structural circulation are already inside the 360 GSF/stall efficiency and are **not** deducted twice.

## 2. Scenario SA-A — Maximum-Fleet Healthcare Mobility Hub

**Concept.** Test whether South Andrews can carry the largest feasible controlled fleet while remaining healthcare-anchored: activated ground floor, five structured parking levels, two office/clinical floors, on-site depot functions, initial managed charging with DC fast-charge capacity.

### Vertical program (planning-level)

| Level | Use | Gross SF | Net usable | Stalls | Fleet-operational | Public/clinical | Charging | Notes |
|---|---|---|---|---|---|---|---|---|
| Roof | Solar 200 kW-DC · garden 8,000 SF · mechanical · BESS 2,000 kWh | — | — | — | — | — | — | Roof allocation unresolved; solar competes with garden and plant |
| L8 | Office / clinical | 24,000 | 20,400 RSF | — | — | — | — | Separate lobby and lift core from fleet operations |
| L7 | Office / clinical | 24,000 | 20,400 RSF | — | — | — | — | Imaging only if FPL capacity confirmed (HC-10) |
| L6 | Structured parking | 28,000 | — | 77 | 60 | 17 | 8 | Gated fleet zone |
| L5 | Structured parking | 28,000 | — | 77 | 62 | 15 | 8 | Gated fleet zone |
| L4 | Structured parking | 28,000 | — | 77 | — | 77 | 8 | Public / tenant |
| L3 | Structured parking | 28,000 | — | 77 | — | 77 | 8 | Public / tenant |
| L2 | Structured parking | 28,000 | — | 77 | — | 77 | 8 | Patient priority, nearest clinical lift |
| L1 | Med-tail 10,000 RSF · lobby · loading · AV staging 18 bays · DCFC cluster · systems | 28,000 | 10,000 RSF leasable | — | 18 bays | — | 8 DCFC | Andrews frontage active; fleet access on secondary edges |
| **Total** | | **216,000** | **40,800 + 10,000 RSF** | **385** | | | **40 L2 + 8 DCFC** | |

### Stall waterfall

| Step | Stalls |
|---|---|
| Gross structured stalls (5 levels × 77) | 385 |
| Less: City code requirement — office 48,000 GFA ÷ 250 | −192 |
| Less: City code requirement — med-tail 10,000 GFA ÷ 250 | −40 |
| Less: secure-zone boundary loss (2 gated levels × 6%) | −9 |
| Less: cleaning / turnaround equivalents | −12 |
| Less: AV manoeuvring reserve | −10 |
| **Net operational fleet stalls** | **122** |
| Plus: dedicated ground AV bays | +18 |
| **Total operational fleet or staging positions** | **140** |
| *Memo: ADA spaces within the code allocation* | *8* |
| *Memo: surplus over code requirement* | *+153* |

### Finding

**SA-A does not deliver 300–400 operational fleet spaces. It delivers approximately 140.**

Reaching 300 net fleet stalls would require roughly **570 gross stalls** — about 7.4 parking levels at 77 stalls per level. That is materially S8's Scenario A: a nine-storey, seven-parking-level structure with a single 24,000 SF office cap and ~575 stalls. That program is a rental-fleet hub with a retail liner, not a healthcare-anchored building, and it is a **rejected scenario** under the current thesis ([Contradictions Matrix](Contradictions%20Matrix.md) §A).

SA-A additionally fails on two independent grounds:

- **Entitlement.** 385 stalls against a 232-stall code requirement is a 1.66× accessory ratio. S8's 575-stall scheme is 4.3×. Neither ratio is supported by any cited ULDR provision (CVR-32 / OQ-27).
- **Electrical.** With on-site depot charging and eight DC fast chargers, the managed service basis computes to **3,208 kW**, which indicates **medium-voltage (13.2 kV) service** with owner-side transformers, a vault, and a utility allowance the uncontrolled electrical workbook puts at $3.5–5.0M. See [Electrical Basis of Design](../technical/Electrical%20Basis%20of%20Design.md).

## 3. Scenario SA-B — Balanced Clinical and Staging Hub (two-site)

**Concept.** The leading strategic hypothesis. Ground-floor med-tail and healthcare services, three structured parking levels, two flexible clinical/medical-office floors, ~40 managed Level 2 chargers, passenger transfer and short-duration staging on site — with overnight storage, bulk charging, cleaning and maintenance at a separate off-site depot.

This is geometrically identical to S3's 6-storey scheme, which allows direct reconciliation to the controlling workbook.

### Vertical program (planning-level)

| Level | Use | Gross SF | Net usable | Stalls | Fleet/staging | Public/clinical | Charging | Notes |
|---|---|---|---|---|---|---|---|---|
| Roof | Solar 150 kW-DC · garden 6,000 SF · mechanical · BESS 500 kWh | — | — | — | — | — | — | Roof study required |
| L6 | Office / clinical | 24,000 | 20,400 RSF | — | — | — | — | Separate lobby/lifts from mobility operations |
| L5 | Office / clinical | 24,000 | 20,400 RSF | — | — | — | — | Flexible outpatient / co-working concept |
| L4 | Structured parking | 28,000 | — | 77 | — | 77 | 14 | Convertible flat deck |
| L3 | Structured parking | 28,000 | — | 77 | — | 77 | 13 | Protected conduit spine |
| L2 | Structured parking | 28,000 | — | 77 | — | 77 | 13 | Patient priority, nearest clinical lift |
| L1 | Med-tail/café 10,000 RSF · lobby · loading · passenger transfer · staging bays · systems | 28,000 | 10,000 RSF leasable | — | up to 18 bays | — | — | Andrews frontage active |
| **Total** | | **160,000** | **40,800 + 10,000 RSF** | **231** | | | **40 L2** | |

### Stall waterfall

| Step | Stalls |
|---|---|
| Gross structured stalls (3 levels × 77) | 231 |
| Less: City code requirement — office 48,000 GFA ÷ 250 | −192 |
| Less: City code requirement — med-tail 10,000 GFA ÷ 250 | −40 |
| **Surplus over code requirement** | **−1 (deficit)** |
| Less: secure-zone boundary loss, turnaround, manoeuvring | −17 |
| **Net operational fleet stalls** | **0 (none available)** |
| Plus: dedicated ground staging bays | +18 |
| **Total operational staging positions** | **18 ground bays only** |

### Finding — this is the most consequential number in the package

**Under a literal application of the 1-per-250-GFA standard, SA-B has no surplus parking.** It is one stall short of its own requirement before a single fleet vehicle, public car, or monetised monthly contract is accommodated.

Two consequences follow:

1. **On-site vehicle staging in SA-B is limited to the 18 ground-level bays.** Structured decks cannot carry a fleet function without either reducing clinical area or obtaining a parking reduction.
2. **S3's $419,265/yr of parking revenue is in tension with the code requirement** (CVR-31 / OQ-26). This package therefore reports two parking constructs throughout:
   - **P1 (code-constrained)** — only genuine surplus is monetised. SA-B NOI **$1,879,069**, yield on cost **3.14%**.
   - **P2 (S3 construct)** — 55% of structured stalls monetised. SA-B NOI **$2,151,484**, yield on cost **3.59%**.

   Neither is adopted. The truth depends on whether the City accepts a shared-parking methodology — medical office peaks on weekday daytime; med-tail and public parking peak evenings and weekends, so a genuine shared-parking case exists. It has not been made to the City, and no utilisation study exists (MB-09).

**Reconciliation to S3.** Running SA-B on construct P2 with AV bay revenue re-added reproduces S3 `Financing & Returns!D17` ($2,277,951) to within $107. The governance-clean ex-AV figure reproduces the repository's independent OQ-22 recomputation ($2,151,591) to within $107. The derivation is faithful to the controlling workbook before any analyst judgment is applied.

### What must move off-site

Because SA-B has no structured surplus, the two-site split is not merely economical — it is **structurally required**:

| Function | On South Andrews | Off-site depot |
|---|---|---|
| Passenger pickup / drop-off | Yes — L1 transfer zone | No |
| Hospital and downtown staging | Yes — up to 18 ground bays | Overflow |
| Short-duration vehicle holding | Yes — ground bays, hours not overnight | — |
| Light turnaround / wipe-down | Limited — 1–2 positions | Primary |
| Dispatch, customer service, mobility reception | Yes — L1 | Secondary |
| Initial public EV charging (40 L2) | Yes — distributed on decks | — |
| Clinical and public parking | Yes — all 231 stalls | — |
| **Overnight fleet storage** | **No capacity** | **Required** |
| **Bulk / depot charging** | **No** | **Required** |
| **Cleaning, detailing, maintenance, tyres** | **No** | **Required** |
| **Vehicle receiving, de-fleeting, damage processing** | **No** | **Required** |
| **Employee parking for fleet operations** | **No capacity** | **Required** |
| Expansion to 250–400 vehicles | Not possible | Required |

## 4. Scenario SA-C — Minimum Viable Development

**Concept.** The least expensive defensible development that protects the land's strategic value, creates an approvable active frontage, supports near-term mobility implementation, avoids overbuilding speculative clinical or fleet capacity, can be expanded later, and has a credible income source.

**Design driver:** stay **below the six-storey enhanced-review threshold.** Four storeys is the largest scheme that avoids the discretionary Level III design review that governs floors 7–9 (S6 p.37; S8 p.4). This removes the single largest entitlement risk from the critical path.

### Vertical program (planning-level)

| Level | Use | Gross SF | Net usable | Stalls | Staging | Public/clinical | Notes |
|---|---|---|---|---|---|---|---|
| Roof | Solar 100 kW-DC · mechanical | — | — | — | — | — | Structure designed for two future levels |
| L4 | Clinical / medical office | 24,000 | 20,400 RSF | — | — | — | Single clinical floor; expandable |
| L3 | Structured parking | 28,000 | — | 77 | — | 77 | Convertible flat deck |
| L2 | Structured parking | 28,000 | — | 77 | — | 77 | Conduit spine, 40 L2 ports distributed |
| L1 | Med-tail 12,000 RSF · lobby · loading · passenger transfer · 10 staging bays · 15 at-grade stalls | 28,000 | 12,000 RSF | 15 | 10 bays | 15 | Andrews frontage active |
| **Total** | | **108,000** | **20,400 + 12,000 RSF** | **169** | | | |

### Stall waterfall

| Step | Stalls |
|---|---|
| Gross stalls (2 structured levels × 77, plus 15 at grade) | 169 |
| Less: City code requirement — office 24,000 GFA ÷ 250 | −96 |
| Less: City code requirement — med-tail 12,000 GFA ÷ 250 | −48 |
| **Surplus over code requirement** | **+25** |
| Less: turnaround and manoeuvring reserve | −8 |
| **Net operational fleet/public surplus stalls** | **17** |
| Plus: dedicated ground staging bays | +10 |
| **Total operational staging positions** | **27** |

**Accessory-parking ratio: 1.17×.** This is by a wide margin the most defensible parking ratio of any scheme tested — it is a building that parks itself with a modest surplus, not a garage with a liner.

### Expansion path

The structure is designed and permitted for vertical expansion to six storeys: transfer level and column loads sized for two additional levels, lift shafts and stair cores overbuilt, conduit and riser capacity provided. **No expansion is assumed in any economics.** Phase 1 must stand alone, and does.

## 5. Scenario SA-C0 — Implementation Staging Ground

**Concept.** The floor case: what does it cost to make South Andrews *function* as a healthcare-facing mobility and staging site without committing to a structured building at all?

- Demolish three 1959-era structures; remediate; elevate and drain to Zone AE standards
- Single-storey **14,000 GSF** med-tail / clinic building on the Andrews frontage, elevated above BFE
- ~70 surface parking spaces, 40 managed Level 2 chargers, 8 staging bays
- Passenger-transfer canopy, gates, licence-plate recognition, wayfinding, streetscape

Code requirement 56 stalls against 70 provided — compliant with a 14-space surplus, a **1.25× accessory ratio**, and no height review of any kind.

**Total: 14,000 GSF, 70 stalls, 16 operational staging positions, core all-in $20.4M including land.**

## 6. Site enablement package — the true minimum

Separately from any building, the minimum spend required to make the site operable as a staging and implementation ground is:

| Component | Allowance |
|---|---|
| Demolition and disposal | $400,000 |
| Environmental remediation allowance | $250,000 |
| Flood / stormwater / drainage / exfiltration | $900,000 |
| Paving, curb, striping, fencing, lighting | $650,000 |
| Electrical service, panel, distribution | $600,000 |
| 40 networked Level 2 chargers + conduit for 30 more | $337,500 |
| Passenger-transfer canopy, gates, LPR, wayfinding | $600,000 |
| Streetscape / landscape / screening (City frontage condition) | $350,000 |
| **Hard subtotal** | **$4,087,500** |
| Soft costs at 22% | $899,250 |
| **Total excluding land** | **$4,986,750** |

**Approximately $5.0M excluding land makes South Andrews functional as a staging and implementation site without any AV deployment.** This is the answer to "what is the minimum to make the site work," and it is the figure against which every larger commitment should be judged.

## 7. Scenario SA-D — Alternative-use and exit comparisons

Evaluated honestly as counterfactuals. None is recommended by default; none is dismissed by default.

| ID | Alternative | Program constraint | Honest assessment |
|---|---|---|---|
| **SA-D1** | Med-tail + residential | **50 du/net acre → ~43–44 units** on 0.88 acre (S6 p.37; S8 p.6) | The density cap is decisive. 43 units is not a tower; it is a small mid-rise. The appraisal's two highest comps were **RAC-CC tower sites** (381 and 316 units) whose value came from density this parcel cannot reach (CVR-53). Residential is not the hidden answer under current zoning. **Unless Live Local preempts the cap** — which is unverified and is now the single highest-value unexplored lever (OQ-30 / MB-18) |
| **SA-D2** | Med-tail + hotel / extended stay | ~130 keys over four parking levels (S8 p.6) | Hotel is an expressly permitted use and pairs naturally with airport and Brightline demand. But it is operator-dependent, cyclical, and abandons the healthcare thesis. It also does not solve the structured-parking cost problem. Worth pricing only if a branded operator or franchise agreement is genuinely available |
| **SA-D3** | Medical-office-dominant | Office-heavy stacks tested in S3 `Sensitivity!A21,A24` return parking ratios of **2.16 and 2.52 per 1,000 RSF** and are flagged "office-heavy; parking constraint" by the workbook's own logic | Self-defeating: more office demands more parking, and parking is the value-destroying component |
| **SA-D4** | Grocery / conventional retail | Single-storey, ~40,000 SF footprint, surface parking | Fits the site physically and is cheap to build. But it forecloses the healthcare and mobility thesis permanently, contributes nothing to Rent With Heldy operations, and — on the appraisal's own retail market data (4.4% availability, **−510,000 SF net absorption**, 1.5% rent growth, S6 p.16) — is entering a softening market |
| **SA-D5** | Bare parking garage / pure fleet depot | Not an enumerated principal use in RAC-RPO (S8 p.4) | **Not permittable as a standalone use.** Requires a principal use to ride on. Also the worst economics tested: structured parking returns roughly 2–3% on fully loaded cost |
| **SA-D6** | Sell the site / do not acquire | — | Zero capital at risk. Given CVR-50, this is a serious option and must be presented as one, not as a failure case |
| **SA-D7** | Land bank / interim operation | Acquire, demolish or retain, operate surface parking and staging, hold for entitlement or market change | Preserves optionality at the lowest capital. Still requires the land basis to be supportable, which is the binding constraint |
| **SA-D8** | Ground lease / partnership structure | Owner contributes land into a JV or ground-leases to a healthcare operator or developer | **The structurally most promising alternative.** It converts a negative-residual land position into an income position without requiring the owner to fund a project that does not clear its hurdle. Requires a counterparty; none is documented |

## 8. Side-by-side comparison

All figures are **model outputs** on the stated Basis B, governance-clean (AV revenue excluded), parking construct P1 (code-constrained) unless noted.

| Metric | SA-A | SA-B | SA-C | SA-C0 |
|---|---|---|---|---|
| Storeys | 8 | 6 | 4 | 1 |
| Total constructed GSF | 216,000 | 160,000 | 108,000 | 14,000 |
| Office / clinical RSF | 40,800 | 40,800 | 20,400 | — |
| Ground leasable RSF | 10,000 | 10,000 | 12,000 | 14,000 |
| Gross stalls | 385 | 231 | 169 | 70 |
| Code-required stalls | 232 | 232 | 144 | 56 |
| Surplus / (deficit) vs code | +153 | **(1)** | +25 | +14 |
| Accessory ratio | 1.66× | 1.00× | 1.17× | 1.25× |
| Operational fleet / staging positions | 140 | 18 | 27 | 16 |
| Core hard cost | $49,790,000 | $38,030,000 | $24,415,000 | $9,097,500 |
| Core all-in (incl. land) | $76,296,810 | $59,874,812 | $40,898,910 | $20,395,184 |
| Tenant-ready all-in | $86,303,671 | $69,800,422 | $46,763,515 | $22,336,743 |
| Core all-in $/GSF | $353 | $374 | $379 | $1,457 |
| Governance-clean NOI (P1) | $2,226,435 | $1,879,069 | $1,227,825 | $556,905 |
| NOI on S3 parking construct (P2) | $2,352,990 | $2,151,484 | $1,356,525 | $526,875 |
| Yield on cost — core, P1 | 2.92% | 3.14% | 3.00% | 2.73% |
| Yield on cost — core, P2 | 3.08% | 3.59% | 3.32% | 2.58% |
| Yield on cost — core, P2 + AV upside | 3.25% | 3.80% | 3.49% | 2.86% |
| Annual gap to 7% yield (core) | $3,114,342 | $2,312,168 | $1,635,099 | $870,758 |
| Break-even office rent for 7% | $159/RSF | $131/RSF | $165/RSF | n/a |
| **Max rational land price @ 7%** | **−$32.2M** | **−$22.1M** | **−$13.7M** | **−$3.7M** |
| **Max rational land price @ 5%** | **−$20.7M** | **−$12.3M** | **−$7.2M** | **−$0.7M** |
| **Max rational land price @ 4%** | **−$10.7M** | **−$3.8M** | **−$1.5M** | **+$1.9M** |
| Managed electrical service basis | 3,208 kW | 1,143 kW | 870 kW | 552 kW |
| Indicated service class | **Medium voltage** | 480 V secondary | 480 V secondary | 480 V secondary |

SA-C0's $1,457/GSF is not a building cost — it is total development cost spread over a small building on an expensive site, and it demonstrates precisely why land basis dominates every low-density option.

## 9. Circulation concepts (design intent, subject to traffic study — OQ-05)

Applies to SA-A, SA-B and SA-C. Adopted from S3 `P&M!A33:A37` and S4 Ch.6; unchanged in principle, tightened here.

| Movement | Route | Requirement |
|---|---|---|
| **Patient / visitor vehicles** | Secondary street edge → dedicated drop-off loop under cover → public ramp → decks nearest the clinical lift | Must never cross the secured staging loop. Drop-off must not queue into the travel lane |
| **Mobility fleet vehicles** | Separate controlled curb cut on a secondary edge → gated queue → ground staging | Independent gates, licence-plate recognition, bollards; separated **before the first decision point** |
| **Fleet egress** | Second secondary-street curb cut | Subject to traffic engineering and City curb-cut approval |
| **Deliveries and waste** | Rear/secondary service bay, screened | Must not use the Andrews frontage; must not block the staging loop |
| **Emergency access** | Fire lane per FFD review; standpipe and FDC locations | Solar, batteries and data rooms must not encroach on emergency access or FPL clearances |
| **Pedestrian access** | South Andrews Avenue frontage — active med-tail, café, lobby | Weather-protected paths; the Andrews frontage is **never** the fleet throat |
| **Staff / provider access** | Shared public ramp, dedicated deck zone | Separate from patient drop-off at peak |
| **FPL access** | Transformer / switchgear zone independently accessible | Must not require entering the secure loop |

## 10. Consultants required before any of this is more than a hypothesis

| Discipline | Question it must answer | Gates |
|---|---|---|
| **Architect** | Plate geometry, core placement, stall efficiency, ramp strategy, whether 77 stalls/level is achievable | Every area and stall figure (MB-02 / OQ-14) |
| **Land-use counsel** | Accessory-parking limits; height review level; Live Local applicability | CVR-32, OQ-27, OQ-30 |
| **Traffic engineer** | Curb cuts, trip generation, queue lengths, separated ingress/egress feasibility | Site plan (MB-04 / OQ-05) |
| **Civil engineer** | Zone AE elevation, stormwater retention, exfiltration | Entitlement (MB-05 / OQ-06) |
| **Parking consultant** | Shared-parking methodology, utilisation, pricing | CVR-31 / OQ-26 / MB-09 |
| **Electrical engineer** | Clinical load density, service size, EMS strategy | CVR-12 / OQ-24 / MB-03 |
| **Geotechnical engineer** | Foundation type and depth | MB-06 / OQ-07 |
| **Fire consultant** | Access, standpipes, garage ventilation, Li-battery provisions | Permit |
| **Environmental consultant** | Phase I/II findings and remediation exposure | CVR-44 / OQ-28 |

## 11. Rules for using this document

1. Every quantitative use must name its scenario ID **and** its parking construct (P1 or P2).
2. No figure here may be presented externally as final, approved, or engineered.
3. Basis A and Basis B must never be combined. A Basis A restatement is required at test-fit.
4. AV revenue never enters a base case. Where shown it is separately labelled upside.
5. Scenario SA-B's stall deficit must accompany any presentation of SA-B, including favourable ones.
