# Canonical Construction Assumptions

**Status:** Current working assumptions; unresolved values preserved · **Last reviewed:** 2026-07-26
**Governing documents:** `AGENTS.md`, `skills/financial-model-audit/SKILL.md` (classification discipline)
**Related:** [Master Assumption Register](Master%20Assumption%20Register.md) §5 · [Contradictions Matrix](Contradictions%20Matrix.md) §D · [Current Development Program](Current%20Development%20Program.md)

All values are **planning allowances pending architect, contractor, FPL, and operator pricing** (S3's own framing, adopted repo-wide). ADOPTED = single working value; DUAL = two live values (never mix bases, never average).

## 1. Structural & design principles — ADOPTED (design intent)

From ODP Ch.5/Table 33 (uncontested across sources; benchmark citations sit in the missing research library):

- Cast-in-place concrete, **flat plates** at ~1–2% drainage gradient (no parked-on sloped ramps)
- **External / independently demolishable speed ramps**
- **Universal structural grid** serving both parking bays and clinical layouts (no transfer structures)
- **12 ft minimum floor-to-floor** on convertible levels
- **50–100 psf design live load** on convertible levels; 100 psf where conversion intended
- Oversized vertical utility chases for medical retrofit; roof designed for PV + mechanical + future equipment
- SEOR hold-points on every grouted base / welded connection + independent third-party special inspections (CHOP failure lesson)
- Mass timber: evaluate for upper floors only (≈14–19% premium, 6-story code ceiling for parking, flood/durability review) — JUDGMENT, not adopted
- **Convertibility premium: accept the low-to-mid range (≈10–15%), not full convertibility (~32%)** — ODP recommendation adopted; final premium priced by GC (OQ-10)
- Just-in-time logistics; no laydown yard on the 0.88-ac site; hold-point inspection regime

## 2. Sitework & resilience

| Item | Treatment | Values | Source |
|---|---|---|---|
| Demolition | DUAL — definitions differ (S2 bundles sitework) | $850K (S2) vs $400K (S3); $350–430K (S7) | S2 `B19`; S3 `D29` |
| Flood/stormwater/resilient sitework | ADOPTED as explicit line (Zone AE entitlement-critical) | $1.25M (6-st) / $1.45M (8-st) | S3 `D30,E30` |
| Flood design basis | ADOPTED: entire site Zone AE; critical MEP above BFE (≈5 ft, unverified); retention vaults + exfiltration per City resilient plan | — | S6 p.28 (VF); ODP §3.3 |
| Geotech | Open: soils "typical/adequate" is appraisal-level only; borings required | — | S6 p.28; MB-06 |

## 3. Vertical construction unit costs — ALL DUAL pending GC pricing (MB-16)

| Item | Basis A (S2) | Basis B (S3) | Notes |
|---|---|---|---|
| Garage/podium structure | $105/SF blended L1+garage (incl. +12% convertibility) | $115/GSF parking + $250/GSF ground podium | S3 anchored to WGI 2026 median $98.75/SF + S FL/HVHZ premium |
| Office/medical shell & core | $310/SF | $290/GSF | HVHZ shell, elevated MEP backbone |
| Office/clinical TI | $75/RSF (spec suites) | $135/RSF ("moderate medical"; imaging/ASC materially higher) | **Material** — likely scope-definition difference; clarify before escalating further |
| Med-tail/café TI | $150/SF café premium | $106.25/RSF ground allowance | Different constructs |
| AV staging fit-out | $600K (JUDGMENT) | $1.25M / $1.4M | Gates, LPR, bollards, canopy, comms, secured loop |
| Roof garden | $175K on 5,000 SF | $90/SF on 6,000/8,000 SF | Amenity-scale decision |

## 4. Energy & mobility infrastructure

| Item | Treatment | Values | Source |
|---|---|---|---|
| EV conduit strategy | **ADOPTED RULE: run conduit/pathways to 100% of stalls during construction** (≈10× cheaper than retrofit); energize a subset day-one | $400/stall × all stalls (S2) vs $1,250/port × ready-minus-installed (S3) — constructs differ | S2 `B28/E28`; S3 `D37`; ODP Ch.8/9 |
| Initial chargers | DUAL → OQ-21 | 32 L2 ($8K/port) + 8 DCFC ($130K/unit) vs 40 L2 ($7.5K/port) + 4 DCFC stub-outs, hardware deferred to operator commitment | S2 `B29–B32`; S3 `D21,D36`, `E&M!B19` |
| Utility service / switchgear | DUAL — **material**; only FPL study resolves (MB-03) | $750K (S2) vs $1.5M/$1.8M "high-uncertainty placeholder" (S3) | S2 `B33`; S3 `D38,E38` |
| Solar | DUAL | 300/340 kW @ $2.60/W (S2) vs 150/200 kW @ $2.40/W (S3) | Roof-allocation dependent |
| BESS | DUAL | 600 kWh @ $520 (S2) vs 500/1,000 kWh @ $600/$550 (S3) | Peak-shave + resilience role (adopted) |
| Tax credits on the above | Interim rule: underwrite **$0** externally until counsel (OQ-17/MB-13) | 30% ITC (S2) vs 0% (S3) | See Canonical Financial Assumptions §4 |
| Edge/data infrastructure | DUAL — scope differs (shell vs fitted) | $450K penthouse shell (S2) vs $1.25M/$1.75M fitted teleops room (S3) | Align scope first |

## 5. Soft costs, contingency, schedule

| Item | Basis A (S2) | Basis B (S3) | Treatment |
|---|---|---|---|
| Soft costs | 18% of hard | A&E 8% + permits/impact 5% + developer/legal/insurance 4% (=17%) + leasing $25/RSF | DUAL — structures differ |
| Contingency | 7.5% | 8% ("should not be reduced before contractor validation" — adopted as a rule) | DUAL (values), ADOPTED (no-reduction rule) |
| Developer fee | 4% of hard+soft | inside the 4% owner-cost line | DUAL |
| Duration | 18 mo (6-st) / 21 mo (8-st) construction-only | 30 / 34 mo build **+ initial lease-up** | DUAL — different definitions; normalize before comparing interest carry |

## 6. Benchmark hygiene

- WGI 2026 Parking Cost Outlook ($33,300/space, $98.75/SF national medians) — benchmark only; obtain local GC/CIP bids (S3 `Sources!A9`).
- DOE AFDC EV benchmarks — utility upgrades can dominate cost (S3 `Sources!A10`).
- Solar cost framework citation in S3 ("NLR"/nlr.gov) appears to be a mis-typed NREL reference — do not rely on that URL; re-source at model reconciliation.
- No workbook total may be called "audited": per the financial-model-audit skill, this session traced formulas and verified internal consistency of S2/S3 but did not independently re-derive every input — outputs remain **unverified model outputs** until a formal audit pass.
