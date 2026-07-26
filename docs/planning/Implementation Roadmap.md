# Implementation Roadmap

**Status:** Draft for owner review · **Date:** 2026-07-26 · **Author:** AI planning session
**Governing documents:** `docs/governance/WORKFLOW.md` (phases 3–7 mapped below)
**Related:** [Document Update Order](Document%20Update%20Order.md) (the document chain) · [Open Questions](Open%20Questions.md) (decision queue)

Two tracks, kept deliberately separate:
- **Track R (Repository modernization)** — turning this planning layer into the governed single source of truth.
- **Track P (Project execution)** — the real-world development steps (studies, negotiations, partners). Track P items are recommendations from the sources (mainly the ODP's 90-day plan), restated for the owner; they spend real money and are entirely owner-gated.

## Track R — Repository modernization (maps to WORKFLOW.md)

### R-Phase 3: Owner review (the immediate next step — this session ends here)
- Owner reads [Executive Planning Summary](Executive%20Planning%20Summary.md) → full planning set as needed.
- Owner rules on the quick ratifications: **D-P2 (thesis), D-P1 (offer mandate), D-P8 (OQ-12), D-P9 (governance succession), D-P12 (address string)** and authorizes **D-P11** (refactor phase 1) if desired.
- Gate honored: **no implementation on unresolved material conflicts** — OQ-14/15/17/18 stay open past this meeting; they gate the *model*, not the review.

### R-Phase 4: Implementation (after decisions)
1. Refactor phase 1 (README, `.gitignore`, `derived/` extractions, `docs/decisions/`) — per [Repository Refactoring Plan](Repository%20Refactoring%20Plan.md).
2. Claim records: generate `docs/claims/` from the [Master Assumption Register](Master%20Assumption%20Register.md) for every externally-relevant claim.
3. Document recovery sweep (MA-01…MA-18): request from owner's files/brokers/appraiser; register recoveries in the [Source Inventory](Source%20Inventory.md).
4. Model vNext build per [Document Update Order](Document%20Update%20Order.md) step 5 — only after D-P5/6/7.
5. ODP v2 → Prospectus vNext per steps 7–8.

### R-Phase 5: Independent audit
- Formal financial-model audit of model vNext per `skills/financial-model-audit/SKILL.md` (independent of the builder; cell-level citations; fit-for-use ruling per output).
- Claim-to-source audit of ODP v2 / prospectus per the claims policy; findings logged by severity.

### R-Phase 6: Corrections
- Resolve audit findings without obscuring prior assumptions; re-obtain owner review where a correction changes a material representation.
- **Gate:** external use only after material findings resolved or expressly accepted with disclosure.

### R-Phase 7: Design-Intelligence connection
- Only once a real design/communications surface exists: test that structured claims, citations, status labels, and rendering disclaimers propagate correctly; re-run affected audits.

## Track P — Project execution (owner-gated; from ODP 90-day plan + this session's findings)

| Window | Actions | Source / gate |
|---|---|---|
| Days 0–30 | Written thesis ratification (D-P2) · negotiation mandate (D-P1) · retain land-use counsel; request Zoning Verification Letter (MB-01) · engage architect + parking consultant for test-fit (MB-02) — **scoped to also resolve the plate conflict (OQ-14) and roof allocation** · commission traffic + civil/stormwater (MB-04/05) | ODP 90-day plan, amended by this session |
| Days 31–60 | City pre-application/DRC · FPL load study (MB-03) · geotech + Phase I ESA (MB-06/11; recover existing Phase I/II first — MA-13) · co-working operator LOI outreach (MB-08) · **MOB rent-comp study (MB-07)** · **tax counsel on QOZ + §48E/30C (MB-13)** | ODP plan + session additions (bold) |
| Days 61–90 | Integrate test-fit + studies into a validated program (closes OQ-14) · price convertibility premium (OQ-10) · build model vNext to (recreated) Underwriting Standards · **decide height scenario inside the model (D-P10/OQ-11)** · reconvene IC; authorize Schematic Design only if the yield gap has a credible closure path | ODP plan; gate per ODP §Gate to Schematic Design |
| Continuous | Grant/TIF/MPO scan (MB-14) · insurance quotes (MB-12) · health-system conversations (prospective, disclosed as such) · AV-operator soundings (MB-15, context only) · negotiation per D-P1 mandate | Session additions |

## The strategic sequencing insight (from the models — restated so it drives the roadmap)

The canonical finding (yield gap; see [Project Canon](Project%20Canon.md) §3) means the roadmap's **critical path to a viable project is not design — it is evidence and partners**: rent validation (MB-07), a co-working/health-system anchor (MB-08+), grants (MB-14), and land basis discipline (D-P1). Design spend ahead of those items buys risk, not progress. Track P is sequenced accordingly; the ODP's own gate ("no Schematic Design until OQ-01 + test-fit + zoning + gating studies") is preserved and extended with the feasibility-closure condition.

## Success criteria for the roadmap
1. Every future document generated from ratified registers — zero orphan values.
2. All eight OQ-critical/high conflicts closed by decision or study, with supersession records.
3. An audited model vNext whose feasibility statement the owner can defend to a lender.
4. A repository where a new AI session can reconstruct project intent from `docs/planning/` alone (the stated success criterion of this engagement).
