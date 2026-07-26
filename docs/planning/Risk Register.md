# Risk Register

**Status:** Draft for owner review · **Date:** 2026-07-26 · **Author:** AI planning session
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
| R-12 | Project-thesis ambiguity (Nexus vs clinical) | M | H | Ratify thesis before design spend | Owner ruling (OQ-01 / D-P2) | **Partially mitigated** — AGENTS.md fixes scope at governance level; formal ratification pending |

## Part 2 — Added by this session (model- and source-derived)

| ID | Risk | P | I | Evidence | Mitigation | Validation required |
|---|---|---|---|---|---|---|
| R-13 | **Base-case infeasibility (yield gap).** Project yields 3.8–4.1% on cost vs 6.25–7.0% requirements; partner gap $1.9–3.2M/yr; development profit −$27.7M to −$33.9M | H (as modeled) | H | S2 `Returns`; S3 `Financing & Returns` — convergent model output | Health-system anchor / master lease / capital contribution / grants; program redesign; rent validation; do not proceed to design spend on base economics alone | MB-07/08/14; owner strategy decision |
| R-14 | **Tax-credit expiry/eligibility.** 30C dead after 6/30/2026; §48E changed — S2 still nets 30% ITC from solar cost | M | M | S3 `E&M!B20–B21` + IRS citations vs S2 `Assumptions!B38` | Underwrite $0 credits until counsel; re-run S2-basis totals ex-ITC | Tax counsel (MB-13 / OQ-17) |
| R-15 | **Program-basis error propagation.** Two irreconcilable plate/stall bases; mixing them silently corrupts any derived document | M | H | Contradictions Matrix §C | DUAL discipline (never mix); test-fit resolution | MB-02 / OQ-14 |
| R-16 | **Acquisition negotiation risk.** Seller anchored at $11.1M appraisal / $12M prior list vs $8.0M disciplined entry; deal may not close in the defensible range | M | H | S6; S8 p.7; S7 waterfall | Anchor to comps/program (S8 logic); walk-away discipline at range top ($9.0M defensible / $9.5M stress) | Owner negotiation mandate (D-P1) |
| R-17 | **Evidence-base fragility.** Core demand and zoning claims trace to a research library absent from the repo; ODP FACTs are one-remove citations | M | M | Missing Research Register Part A | Recover documents or re-source claims; downgrade classifications until then | MA-01…MA-17 recovery |
| R-18 | **Insurance cost severity (flood + HVHZ + coastal).** Flagged "High" by analyst scorecard but never quantified anywhere | M | M | S7 `Constraint Scorecard`; S1 §7 | Obtain quotes early; carry explicit opex line in model vNext | MB-12 |
| R-19 | **AV-revenue leakage into base case.** S3 base NOI includes $194K/yr AV-bay revenue despite governance prohibition — feasibility slightly overstated on Basis B | M | L→M | S3 `F&R!D11` vs AGENTS.md | Recompute ex-AV (≈$2.15M/$2.97M NOI); correct in model vNext | OQ-22 |
| R-20 | **Single-source workbook risk.** Both current models are unaudited (formulas traced this session, but inputs not independently re-derived); no derived-data layer exists | M | M | financial-model-audit skill requirements | Formal audit pass (Workflow Phase 5); create `derived/` extracts with provenance | Audit scheduled in [Implementation Roadmap](Implementation%20Roadmap.md) |

## Top-priority risks to actively manage from kickoff
Per ODP guidance plus this session: **R-13 (yield gap)**, R-1 (flood), R-2/R-14 (FPL + tax), R-4 (cost/rate), R-16 (negotiation), R-12→closure via D-P2.
