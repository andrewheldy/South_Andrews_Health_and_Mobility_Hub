# Canonical Financial Assumptions

**Status:** Current working assumptions; unresolved economics preserved · **Last reviewed:** 2026-07-26
**Governing documents:** `AGENTS.md`, `docs/governance/CLAIMS_AND_EVIDENCE_POLICY.md`
**Related:** [Master Assumption Register](Master%20Assumption%20Register.md) (full provenance) · [Contradictions Matrix](Contradictions%20Matrix.md) §§B, D, E · [Open Questions](Open%20Questions.md)

Canonical status per input: **ADOPTED** (single working value justified by hierarchy/convergence) or **UNRESOLVED — DUAL** (two live values; present both or omit; never mix, never average). Everything on this page is **planning-level** and **internal-only / blocked for external use** unless a row says otherwise. Model outputs are not verified facts.

## 1. Acquisition & land basis

| Input | Canonical treatment | Basis |
|---|---|---|
| Land opening offer | **ADOPTED STRATEGY INPUT: $8,000,000** ($209/SF), not proof of value or authority to submit an offer | Ratified D-P1; S2 `Assumptions!B18`; S3 `Assumptions!D7`; S8 p.7. Ceiling, walk-away, authority, and final conditions unresolved |
| Negotiation envelope | ADOPTED (working): room to ~$8.75M; defensible range $7.65–9.0M; stress case $9.5M | S8 p.7; S3 `Sensitivity!A13:A15` |
| Appraised value | CONTEXT ONLY: $11.1M (9/18/2025) — appraisal opinion, with standing comp critiques | S6 p.5; S1 §4; S8 p.7 |
| Analyst residual value | CONTEXT ONLY: $8.96M supported (different, multifamily program); hub-only ~$0.81M | S7 |
| Closing costs | ADOPTED (working): 2% of land | S3 `Assumptions!D8` (S2 omits — note in reconciliation) |

## 2. Revenue inputs

| Input | Canonical treatment | Basis |
|---|---|---|
| Medical office rent (NNN) | **UNRESOLVED — DUAL: $36/RSF (S2) vs $50/RSF (S3)** → OQ-15; needs MB-07 comps. S2's "FACT" tag is reclassified to *source-derived, not independently verified* | S2 `Assumptions!B53`; S3 `Assumptions!D55` |
| Office stabilized vacancy | **ADOPTED: 7%** (convergent) | S2 `B54`; S3 `D56` |
| Med-tail/café rent | UNRESOLVED — DUAL: $42/SF (S2, 4,500 SF) vs $45/RSF (S3, 10,000 RSF @95%) — entangled with program basis (OQ-14) | S2 `B55`; S3 `D57–D58` |
| Parking revenue | UNRESOLVED — DUAL: $2,400/space/yr all-space blended (S2) vs $275/stall/mo × 55% monetized share (S3); needs MB-09; underlying pricing survey not in repo | S2 `B56`; S3 `D60–D61` |
| Parking opex | UNRESOLVED — DUAL: 30% (S2) vs 35% pooled parking/EV/AV (S3) | S2 `B57`; S3 `D65` |
| EV charging net income | **ADOPTED: $120,000/yr** across ~40 units, utilization-sensitive (convergent: S2 lump = S3 $250/port/mo × 40) | S2 `B58`; S3 `D62` |
| AV staging revenue in base case | **ADOPTED RULE: $0 in every base case.** Upside only with a signed operator (S2: $300K/yr at $25/SF×12,000 SF; S3: $194.4K/yr at 18×$900/mo). S3's inclusion of AV-bay revenue in base NOI is flagged — OQ-22; governance-clean S3 NOI ex-AV ≈ $2.15M (6-st) / $2.97M (8-st) *(recomputed, recommendation only — workbook untouched)* | AGENTS.md; S2 `B63`; S3 `F&R!D11` |
| Edge/data lease | UNRESOLVED — DUAL: $30K/yr allowance (S2, FORECAST) vs $55/SF/yr on 1,500–2,000 SF (S3) | S2 `B61`; S3 `D59` |
| Solar energy value | UNRESOLVED — DUAL (minor): 1,450 kWh/kW-yr × $0.13/kWh vs 1,500 kWh/kW-yr factor | S2 `B59–B60`; S3 `E&M!B15` |
| Management fee / non-recoverables | DUAL structures: 3% EGI + $1.50/SF GBA (S2) vs 25% office-EGI & 35% mobility-EGI opex ratios (S3) | S2 `B64–B65`; S3 `D64–D65` |
| Lease-up ramp | ADOPTED (working): 50% Yr1 / 90% Yr2 / stabilized Yr3 post-CO | S2 `B72–B73` (S3 embeds in 30/34-mo period) |

## 3. Financing

| Input | Canonical treatment | Basis |
|---|---|---|
| Construction LTC | UNRESOLVED — DUAL: 65% (S2) vs 60% (S3); lender term sheet decides | S2 `B48`; S3 `D50` |
| Loan rate | UNRESOLVED — DUAL: 7.5% vs 8.0% | S2 `B49`; S3 `D51` |
| Average drawn balance | **ADOPTED: 55%** (convergent) | S2 `B50`; S3 `D52` |
| Financing fee | ADOPTED (working): 1.5% of loan (S3 models it; S2 omits) | S3 `D53` |
| Capital stack strategy | ADOPTED (to test, not commitments): QOZ equity + construction debt; P3/MPO grants & TIF explored but never load-bearing; tax-exempt structures only with a qualifying nonprofit/health-system partner | ODP §11.2 |

## 4. Tax positions

| Input | Canonical treatment | Basis |
|---|---|---|
| Solar/storage ITC (§48E) | **UNRESOLVED — DUAL, material (OQ-17): 30% captured (S2) vs 0% underwritten (S3, citing 2025–2026 law changes).** Prudent interim rule: **external and lender materials underwrite $0 credits** until tax counsel opines (MB-13) | S2 `Assumptions!B38`; S3 `E&M!B21` + `Sources!A13` |
| §30C charger credit | ADOPTED (S3 position, pending counsel): $0 — placed-in-service deadline 6/30/2026 likely missed | S3 `E&M!B20` + `Sources!A12` |
| QOZ treatment | ADOPTED (strategy): ≥10-yr hold aligned to QOZ basis step-up; structuring by tax counsel pending | S2 `B71`; ODP Ch.11 |

## 5. Exit & hurdles

| Input | Canonical treatment | Basis |
|---|---|---|
| Exit cap rate | **UNRESOLVED — DUAL, material (OQ-18): 6.25% (S2, institutional MOB/mixed) vs 7.25% (S3, specialty/parking-heavy).** The choice is really an asset-classification question. Context: S6 market cap ~5.9–6.0% retail; S7 5.35% multifamily / 7.5% hub | S2 `B69`; S3 `D67` |
| NOI growth | ADOPTED (working): 2.5%/yr | S2 `B68` |
| Cost of sale | ADOPTED (working): 2% | S2 `B70` |
| Hold period | ADOPTED: 10 years (QOZ-aligned) | S2 `B71`; ODP |
| Hurdle metric | DUAL until Underwriting Standards exist (MA-06): 150+ bps spread over exit cap (S2) and/or 7.0% YoC before incentives (S3) — report both | S2 `Summary!D9`; S3 `D66` |

## 6. Canonical model outputs (class: model output — never facts)

| Output | 6-story | 8-story | Source |
|---|---|---|---|
| TDC (Basis A) | $71.52M | $94.97M | S2 `Budget!B24,C24` |
| Stabilized NOI (Basis A) | $2.738M | $3.820M | S2 `Operating!B15,C15` |
| Yield on cost (Basis A) | 3.83% | 4.02% | S2 `Returns!B13,B27` |
| Development profit (Basis A) | **−$27.71M** | **−$33.86M** | S2 `Returns!B15,B29` |
| Unlevered 10-yr IRR (Basis A) | 1.24% | 1.85% | S2 `Returns!B16,B30` |
| Core all-in cost (Basis B) | $59.54M | $76.19M | S3 `Construction Budget!D56,E56` |
| Tenant-ready all-in (Basis B) | $69.46M | $90.48M | S3 `D57,E57` |
| Stabilized NOI (Basis B, incl. AV bays — see OQ-22) | $2.278M | $3.099M | S3 `F&R!D17,E17` |
| Core yield on cost (Basis B) | 3.83% | 4.07% | S3 `F&R!D21,E21` |
| Annual partner gap — core (Basis B) | **$1.890M** | **$2.234M** | S3 `F&R!D25,E25` |
| Annual partner gap — tenant-ready (Basis B) | **$2.585M** | **$3.234M** | S3 `F&R!D26,E26` |

**Canonical feasibility statement:** Both bases converge: at $8.0M land with base revenue, the program yields ≈3.8–4.1% on cost versus 6.25–7.0% requirements. **The project does not currently pencil without partner support, grants, above-market revenue, or a materially changed program.** This statement is mandatory in internal decision documents and may not be omitted from lender-facing materials.

## 7. External-use rules for this page

- Every number above is planning-level; external use requires the CLAIMS_AND_EVIDENCE_POLICY claim record and approved status language.
- DUAL rows are **blocked** for external use until resolved.
- The §6 outputs may be shown externally only with both scenarios' bases identified and the feasibility statement intact.
