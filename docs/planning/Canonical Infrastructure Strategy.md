# Canonical Infrastructure Strategy

**Status:** Current working strategy; sizing unresolved · **Last reviewed:** 2026-07-26
**Governing documents:** `AGENTS.md`, `PROJECT_GLOSSARY.md` (EV-ready / EV-installed discipline)
**Related:** [Canonical Mobility Strategy](Canonical%20Mobility%20Strategy.md) · [Canonical Construction Assumptions](Canonical%20Construction%20Assumptions.md) · [Missing Research Register](Missing%20Research%20Register.md) (MB-03, MB-05, MA-11)

## 1. Electrical power (the gating infrastructure)

**Planning loads (Basis B, S3 `Energy & Mobility` — working values; "Not an FPL load letter"):**

| Load component | 6-story | 8-story | Basis |
|---|---|---|---|
| Managed EV peak (40 ports × 9.6 kW × 50% coincidence) | 192 kW | 192 kW | Via missing load model (MA-11) |
| Office peak (5 W/GSF, excl. imaging/ASC/kitchens) | 240 kW | 360 kW | Engineer must refine |
| Ground floor (6 W/GSF) | 168 kW | 168 kW | Engineer must refine |
| Garage ancillary (0.5 W/GSF) | 42 kW | 56 kW | — |
| **Planning peak before headroom** | **~642 kW** | **~776 kW** | S3 `E&M!B11,D11` |
| Calculated service w/ 25% headroom | ~0.80 MVA | ~0.97 MVA | Before future DCFC/imaging |
| **Recommended service target** | **1.5 MVA** | **2.0 MVA** | "Preliminary target only; FPL and engineer must confirm" |

- **FPL status: unverified.** Transformer capacity for medical imaging + dense EV is an assumption; will-serve/load study (MB-03, OQ-04) gates imaging tenancy, DCFC expansion, and MEP design. Allowance conflict: $750K (S2) vs $1.5–1.8M (S3) — unresolved.
- **Redundancy rationale:** historical grid vulnerability (2020 Sistrunk substation fire) argues for on-site redundancy for clinical continuity (ODP §3.3 — SD).
- **Hard gates (adopted):** no imaging commitments and no dense-DCFC commitments before FPL confirmation; switchgear room and risers sized above base load for future EV/AV/edge (readiness is cheap now, coring is not).
- **Recover `South_Andrews_Electrical_Load_Model.xlsx` (MA-11)** — the cited base plan for these figures is not in the repo.

## 2. Solar + battery

- **Role (adopted):** peak shaving, demand-charge management (DCFC-relevant), resilience ride-through, solar capture. **Not** primary building power, **not** an emergency-generator replacement (S3 `E&M!A2,G16`).
- **Sizing — DUAL (unresolved):** 300/340 kW + 600 kWh (S2) vs 150/200 kW + 500/1,000 kWh (S3). Driver: roof-allocation assumptions. Battery duration at managed EV peak ≈ 2.6–5.2 h (S3 calc) — shows BESS trims demand but cannot carry the site.
- **Tax treatment:** underwrite $0 credits externally until counsel (OQ-17); S2's 30%-ITC netting flagged wherever cited.
- **Placement rules (adopted):** prioritize standard rooftop arrays; canopy only where it also provides shade value; never consume emergency access, FPL clearances, or charger-expansion corridors.

## 3. Roof allocation (a real design tension — surface it, don't hide it)

Competing claims on one roof: solar array · staff garden (5,000 vs 6,000–8,000 SF) · edge penthouse (2,000 SF, Basis A) · mechanical · future equipment. The 2× solar-sizing gap between models is largely this allocation. **Action:** roof-allocation study inside the test-fit (MB-02) before either solar number is used externally.

## 4. Edge / data infrastructure

- **Scope (adopted language):** a 1,500–2,000 SF **edge/fleet data room** for teleoperations, building analytics, fleet dispatch, limited inference — "avoid calling this a data center until power and cooling scope is defined" (S3 `E&M!G18`).
- Cost/scope DUAL: $450K shell + tenant fit-out (S2) vs $1.25–1.75M fitted (S3). Revenue FORECAST-class only ($30K/yr allowance vs $55/SF/yr).
- Fiber: Tier-1 redundant entries (Hotwire 10 Gbps symmetrical, AT&T, Lumen, Crown Castle cited) — low-marginal-cost readiness, adopted (SD via ODP §3.3).

## 5. Water, sewer, stormwater

- Potable/sanitary: City service reported adequate for typical mixed-use; connection sizing at SD (SD).
- **Stormwater is on the critical path** (adopted): entire site Zone AE; on-site retention vaults, exfiltration trenches, conformance with the City resilient stormwater master plan are non-negotiable entitlement requirements; start hydrology early (ODP §3.3/§10.2; MB-05). Explicit allowance $1.25–1.45M (Basis B).
- Landscape doubles as stormwater management where possible (ODP §13E).

## 6. Resilience & envelope

Hurricane/HVHZ baseline design; marine-grade durable envelope; critical MEP above BFE; energy redundancy for clinical continuity; longevity-as-sustainability (lifecycle cost over first cost). *(ODP Ch.13B/G — adopted design intent.)*

## 7. Readiness-vs-activation table (the phase-innovation rule applied to infrastructure)

| Domain | Build now (cheap readiness) | Activate when |
|---|---|---|
| EV | Conduit to 100% of stalls; panel capacity; ~40 chargers | Installed-charger utilization > target AND FPL confirmed |
| Power headroom | Switchgear room + risers above base load | Imaging tenant, EV expansion, or AV/edge load materializes |
| DCFC | 4 stub-outs/equipment pads | Operator commitment (master lease / minimum-use) |
| Fiber/digital | Redundant entries + smart-building backbone | Tenant need |
| Structure | Flat plates, 12-ft F2F, 100 psf bays | Parking demand falls → convert levels |
| AV operations | Access/structural/power readiness only | Demonstrated demand or signed partner + logged decision |

*(ODP Table 39, adopted; every activation requires an explicit owner-approved trigger.)*
