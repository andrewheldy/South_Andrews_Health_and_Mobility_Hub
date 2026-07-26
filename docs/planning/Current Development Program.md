# Current Development Program

**Status:** Draft for owner review · **Date:** 2026-07-26 · **Author:** AI planning session
**Governing documents:** `AGENTS.md` (scenario discipline), `docs/governance/SOURCE_AUTHORITY.md`
**Related:** [Current Project Scope](Current%20Project%20Scope.md) · [Master Assumption Register](Master%20Assumption%20Register.md) §4 · [Contradictions Matrix](Contradictions%20Matrix.md) §C

> **Canonical status statement:** Final program areas are **TBD — pending architect/parking test-fit** (consistent with ODP Table 32 and the legacy prospectus: "sized during design, not before"). Two competing sized program bases exist in the current models. They are presented side by side below and **must never be mixed**. Neither is adopted (OQ-14).

## 1. The two live program bases + rejected third-party program

| Metric | **Basis A — S2 (6v8 Model, 35,000 SF plate)** | **Basis B — S3 (8M Feasibility, 28k/24k plates)** | *Context only — S8 Scenario A (rejected rental program)* |
|---|---|---|---|
| 6-story GBA | 210,000 SF | 160,000 SF | — |
| 8-story GBA | 280,000 SF | 208,000 SF | 9-story ~229,500 SF |
| Office floors (6/8-story) | 2 / 3 | 2 / 3 | L9 office cap 24,000 SF |
| Office RSF (6/8) | 59,500 / 89,250 | 40,800 / 61,200 | — |
| Structured stalls (6/8) | 340 / 440 (incl. 40 at grade) | 231 / 308 (+18 AV bays separate) | ~575–600 |
| SF/stall | 350 | 360 | ~340 |
| Parking ratio /1,000 RSF | 5.71 / 4.93 | ~4.5 / ~4.3 | — |
| Ground floor | café 4,500 + AV zone 12,000 + lobby/BOH 4,500 + parking/DCFC 14,000 | 10,000 RSF med-tail+café leasable; AV bays; lobby/loading/systems | retail liner + rental counter 9,500 SF |
| Source cells | `Program!B4:D20` | `Program & Massing!A4:H37` | S8 pp.4–5 |

Convergent across both bases (adopted as working answers): **2 office floors on 6 stories / 3 on 8 stories**; L1 active frontage on Andrews; parking levels immediately above L1; office/clinical on top; roof = solar + garden + mechanical (+ penthouse in Basis A).

## 2. Floor-by-floor stacks (as modeled)

### Basis A (S2) — 35,000 SF plates
```
6-STORY                          8-STORY
L6  Office/clinical              L8  Office/clinical
L5  Office/clinical              L7  Office/clinical
L4  Parking                      L6  Office/clinical
L3  Parking                      L5  Parking
L2  Parking                      L4  Parking
L1  Café 4.5k | AV 12k |         L3  Parking
    Lobby/BOH 4.5k |             L2  Parking
    Parking/DCFC 14k             L1  (same as 6-story L1)
ROOF: solar 300kW + garden 5k SF + edge penthouse 2k SF     ROOF: solar 340kW + garden + penthouse
```

### Basis B (S3) — 28,000 SF ground/parking, 24,000 SF office
```
6-STORY                          8-STORY
L6  Office/clinical 24k          L8  Office/clinical 24k
L5  Office/clinical 24k          L7  Office/clinical 24k
L4  Parking 28k                  L6  Office/clinical 24k
L3  Parking 28k                  L5  Parking 28k
L2  Parking 28k                  L4  Parking 28k
L1  Med-tail/café/lobby/         L3  Parking 28k
    AV staging 28k               L2  Parking 28k
                                 L1  (same)
ROOF: solar 150kW + garden 6k SF + BESS 500kWh              ROOF: solar 200kW + garden 8k + BESS 1,000kWh
```
*(S3 `Program & Massing!A21:H29`; stack notes: patient/visitor parking closest to clinical elevator on L2; chargers distributed on L5 (8-story); clinical floors use separate lobby/elevators from fleet operations.)*

## 3. Site circulation & ingress/egress design principles (adopted design intent, subject to traffic study — OQ-05)

1. Keep **South Andrews Avenue** as the active pedestrian/medical-retail frontage — never the fleet curb cut. (S3 `P&M!A33`)
2. Use the **secondary street edges** for separated AV ingress and egress where traffic engineering and City review permit. (S3 `P&M!A34`)
3. Separate public/patient circulation from the secured AV staging loop **before the first decision point**. (S3 `P&M!A35`)
4. Give the AV zone independent gates, queuing, wash/light-service capability, secure pedestrian paths. (S3 `P&M!A36`)
5. Do not let solar/batteries/data rooms consume emergency access, FPL transformer clearances, or charger-expansion corridors. (S3 `P&M!A37`)
6. Dedicated ride-share/patient drop-off zone; weather-protected pedestrian paths; loading screened at rear. (ODP Ch.6)
7. FPL transformer/switchgear zone independently accessible without entering the secure AV loop. (S3 `E&M!A28`)

## 4. Program components and their roles (basis-independent)

| Component | Role | Status |
|---|---|---|
| Medical office / flexible outpatient (decoupled from inpatient code) | Primary revenue; anchor identity | Areas TBD |
| Medical co-working (turnkey HIPAA suites under master tenant) | Anchor leasing strategy; captures displaced independents | Operator unidentified (OQ-08) |
| Med-tail liner (pharmacy, urgent care, DME, wellness, F&B) | Street activation + post-discharge capture | Areas TBD |
| Convertible parking podium | Enabling infrastructure + early cash flow + future conversion | Count TBD (basis conflict) |
| AV staging ground zone/bays | Preserved capability; revenue only on signed operator | No LOI exists |
| EV charging (~40 initial; conduit to 100%) | Amenity + net income (~$120K/yr working) | Split unresolved (OQ-21) |
| Solar + BESS | Opex offset + resilience (peak-shave role) | Sizing unresolved |
| Edge/fleet data room | Optionality tenant space; teleops-scale | Scope dual-valued |
| Roof garden | Staff amenity | Scale unresolved |

## 5. Rules

1. Any quantitative use of this program must cite Basis A or Basis B explicitly.
2. No external document may present either basis as final ("subject to test fit" language required).
3. The test-fit brief (MB-02) should be scoped to decide: plate geometry, stall efficiency, AV zone form (12,000 SF zone vs 18 bays), ground-floor leasable split, and the resulting canonical program table that replaces §1 of this document.
