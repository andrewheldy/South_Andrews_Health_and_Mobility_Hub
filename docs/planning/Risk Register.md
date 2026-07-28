# Risk Register

**Status:** Current operative risk register · **Last reviewed:** 2026-07-26
**Governing documents:** `AGENTS.md` (status discipline)
**Related:** [Open Questions](Open%20Questions.md) · [Missing Research Register](Missing%20Research%20Register.md)

Consolidates the ODP risk register (R-1…R-12, carried with original IDs) and adds risks surfaced by this session's model and source analysis (R-13…R-20). Ratings are Probability × Impact (L/M/H), professional judgment pending specialist confirmation. This register should become a live log reviewed at every milestone.

## Part 1 — Carried from ODP (S4 Table 44)

| ID | Risk | P | I | Mitigation | Validation required | Status |
|---|---|---|---|---|---|---|
| R-1 | Flood / storm surge (Zone AE, SLR) | H | H | Elevate critical MEP above BFE; retention/exfiltration; harden envelope per FTL Resiliency Plan | Civil/hydrology design; City stormwater review (MB-05) | Open |
| R-2 | FPL transformer capacity shortfall | M | H | Early will-serve study; central plant/redundancy; oversized switchgear room | FPL capacity study (MB-03 / OQ-04) | Open |
| R-3 | Medical-office supply glut (10.4% vacancy cited) | M | M | Differentiate via co-working + parking surplus; avoid generic shell | Updated absorption at lease-up (MB-07) | Open |
| R-4 | Construction cost / interest-rate escalation | H | H | Value-engineer convertibility premium; JIT logistics; stress-test model | GC pricing; sensitivity (MB-16) | Open |
| R-5 | Entitlement / Live Local volatility | M | M | Land-use counsel now; lock vested rights via permits | City determination; counsel (MB-01/MB-18) | Open |
| R-6 | Precast/structural connection failure | L | H | SEOR hold-points; third-party special inspections (CHOP lesson) | Inspection protocol in CDs | Open |
| R-7 | Parking demand erosion from AV adoption | L | M | Convertible structure enables reuse; trigger-based phasing | Demand monitoring; activation triggers | Open |
| R-8 | Telehealth shrinks clinical footprint | M | M | Smaller flexible sound-proofed suites; co-working flexibility | Tenant demand signals | Open |
| R-9 | Site logistics (no laydown yard) | H | M | CM-led just-in-time delivery/staging plan | CM logistics plan pre-GMP | Open |
| R-10 | Geotechnical / foundation surprises | M | M | Borings; deep-compaction precedent (SoLé Mia) | Geotech report (MB-06) | Open |
| R-11 | Title / easement defects | L | M | Updated title commitment; survey reconciliation | Title work (MB-10 / OQ-09) | Open |
| R-12 | Project-thesis ambiguity (Nexus vs clinical) | M | H | Preserve D-P2 thesis and rejected-scenario lineage | Owner ruling (OQ-01 / D-P2) | **Mitigated at strategy level by D-P2**; program/economic validation remains open |

## Part 2 — Added by this session (model- and source-derived)

| ID | Risk | P | I | Evidence | Mitigation | Validation required |
|---|---|---|---|---|---|---|
| R-13 | **Base-case infeasibility (yield gap).** Project yields 3.8–4.1% on cost vs 6.25–7.0% requirements; partner gap $1.9–3.2M/yr; development profit −$27.7M to −$33.9M | H (as modeled) | H | S2 `Returns`; S3 `Financing & Returns` — convergent model output | Health-system anchor / master lease / capital contribution / grants; program redesign; rent validation; do not proceed to design spend on base economics alone | MB-07/08/14; owner strategy decision |
| R-14 | **Tax-credit expiry/eligibility.** 30C dead after 6/30/2026; §48E changed — S2 still nets 30% ITC from solar cost | M | M | S3 `E&M!B20–B21` + IRS citations vs S2 `Assumptions!B38` | Underwrite $0 credits until counsel; re-run S2-basis totals ex-ITC | Tax counsel (MB-13 / OQ-17) |
| R-15 | **Program-basis error propagation.** Two irreconcilable plate/stall bases; mixing them silently corrupts any derived document | M | H | Contradictions Matrix §C | DUAL discipline (never mix); test-fit resolution | MB-02 / OQ-14 |
| R-16 | **Acquisition negotiation risk.** Seller anchored at $11.1M appraisal / $12M prior list vs the $8.0M working opening input; deal may not close at an evidence-supported basis | M | H | S6; S8 p.7; S7 waterfall; D-P1 | Complete diligence and obtain explicit negotiating authority, ceiling, and walk-away decision; third-party ranges are not adopted limits | OQ-20; later owner decision |
| R-17 | **Evidence-base fragility.** Core demand and zoning claims trace to a research library absent from the repo; ODP FACTs are one-remove citations | M | M | Missing Research Register Part A | Recover documents or re-source claims; downgrade classifications until then | MA-01…MA-17 recovery |
| R-18 | **Insurance cost severity (flood + HVHZ + coastal).** Flagged "High" by analyst scorecard but never quantified anywhere | M | M | S7 `Constraint Scorecard`; S1 §7 | Obtain quotes early; carry explicit opex line in model vNext | MB-12 |
| R-19 | **AV-revenue leakage into base case.** S3 base NOI includes $194K/yr AV-bay revenue despite governance prohibition — feasibility slightly overstated on Basis B | M | L→M | S3 `F&R!D11` vs AGENTS.md | Recompute ex-AV (≈$2.15M/$2.97M NOI); correct in model vNext | OQ-22 |
| R-20 | **Single-source workbook risk.** Both current models are unaudited (formulas traced this session, but inputs not independently re-derived); no derived-data layer exists | M | M | financial-model-audit skill requirements | Formal audit pass (Workflow Phase 5); create `derived/` extracts with provenance | Audit scheduled in [Implementation Roadmap](Implementation%20Roadmap.md) |

## Part 3 — Added by the integrated development pass (2026-07-27)

| ID | Risk | P | I | Evidence | Mitigation | Validation required |
|---|---|---|---|---|---|---|
| R-21 | **Land basis is unsupportable by the program at any price.** Residual land value is negative under every tested scenario at institutional yields; at a **zero** land basis no scheme exceeds 4.49% yield on cost. Break-even office rent is ~$131/RSF against $50 modelled | H (as modelled) | H | Derived model `residual_land_value`; consistent with CAN-020/021/022 | Do not treat acquisition as the first step. Close the cheap gates first; test ground-lease, option, participation and JV structures that remove the fixed land obligation | MB-07 (rents), MB-16 (GC pricing), MB-14 (public capital), owner underwriting standard (MA-06) |
| R-22 | **Operational fleet capacity is roughly one third of the working hypothesis.** After code-required parking, secure-zone boundary loss, turnaround and manoeuvring reserve, the maximum-fleet scheme yields ~140 operational positions, not 300–400. The leading balanced scheme yields **18 ground bays and no structured surplus** | H | H | Derived model `stall_waterfall`; City standard at S6 p.37 | Adopt the two-site strategy as a design discipline; size the site as a transfer point, not a storage facility; never quote gross stalls as fleet capacity | MB-02 (test-fit), MB-01 (parking method) |
| R-23 | **Parking revenue may not exist.** S3 books $419,265/yr from 55% of 231 structured stalls while the City's 1-per-250-GFA standard consumes ~232 for the building's own uses | M | M | CVR-31; S3 `F&R!D9` vs S6 p.37 | Report both parking constructs (P1 code-constrained, P2 as-modelled) until a City determination exists; never present P2 alone | MB-01 + MB-09 (OQ-26) |
| R-24 | **Undisclosed environmental condition.** A Phase I **and a Phase II** ESA are listed among documents the appraiser reviewed; neither is in the repository and no findings are reported anywhere. A Phase II is normally commissioned only after a Phase I identifies a recognised environmental condition | M | H | S6 p.10 vs S6 p.28; S8 step 3 | Recover both reports before any offer becomes non-refundable. The $250K remediation allowance carried in the budget is a placeholder against an unknown | MA-13 recovery; MB-11 (OQ-28) |
| R-25 | **Ungoverned electrical model drives a $750K–$5.0M budget line.** The corrected load workbook sits outside the repository, has no established provenance, contains an 11,000 SF internal area inconsistency, models a program the project has not adopted, and subtracts battery capacity from the service size in a manner no engineer can stamp | M | H | CVR-01, CVR-10, CVR-13, CVR-16 | Method adopted where sound; conclusions rejected. Obtain an FPL will-serve study before any service-size commitment. Owner to rule on admitting the workbook to `sources/` | MB-03 (OQ-24, OQ-25, OQ-29) |

## Top-priority risks to actively manage from kickoff
Per ODP guidance plus prior sessions: **R-13 (yield gap)**, R-1 (flood), R-2/R-14 (FPL + tax), R-4 (cost/rate), and R-16 (negotiation) remain priority. R-12 is strategy-level closed by D-P2.

**Revised following the integrated development pass.** **R-21 supersedes R-13 as the governing economic risk** — R-13 identified the yield gap; R-21 establishes that it is not curable by land price and therefore changes the nature of the acquisition decision rather than its terms. **R-24 is the highest-priority near-term item** because it is the cheapest to close, the fastest, and the one most capable of stopping the transaction outright.
