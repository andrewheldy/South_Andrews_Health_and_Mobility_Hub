# Document Update Order

**Status:** Draft for owner review · **Date:** 2026-07-26 · **Author:** AI planning session
**Governing rule:** flow is one-way (see [Document Dependency Graph](Document%20Dependency%20Graph.md)); **no downstream document is updated before its upstream is ratified.** Skipping a gate reintroduces exactly the contradictions this planning set just mapped.

## The ordered chain

| Step | What is updated | Precondition (gate) | Output |
|---|---|---|---|
| 0 | Governance fixes (if any) — e.g., D-P9 governance-succession note added to AGENTS.md/SOURCE_AUTHORITY.md | Owner decision D-P9 | One constitution, cleanly declared |
| 1 | **Project Canon ratification** — owner reviews/edits/ratifies [Project Canon](Project%20Canon.md); D-P2 (thesis), D-P1 (offer mandate), D-P8, D-P12 recorded | Owner review session | `status: ratified` canon; Decision Log entries D-001+ |
| 2 | **Register adoption** — [Master Assumption Register](Master%20Assumption%20Register.md), [Contradictions Matrix](Contradictions%20Matrix.md), [Open Questions](Open%20Questions.md), [Risk Register](Risk%20Register.md) accepted as the working evidence layer | Step 1 | Frozen baseline for all downstream work |
| 3 | **Repository refactor phase 1** — README, `.gitignore`, `derived/` extractions, `docs/decisions/` | D-P11 | Navigable repo; provenance-stamped derived data |
| 4 | **Evidence recovery & studies round 1** — MA-document recovery; commission MB-01 (zoning), MB-02 (test-fit), MB-03 (FPL), MB-04/05 (traffic/stormwater), MB-07 (rent comps), MB-13 (tax counsel) | Steps 1–2 (budget authorization) | Inputs to resolve OQ-14/15/17/03/04 |
| 5 | **Model reconciliation (model vNext)** — new workbook built from ratified register values on the decided program basis; S3's AV-revenue base corrected (OQ-22); both hurdle metrics reported; formal financial-model audit per skill | D-P5, D-P6, D-P7 + study results | Single canonical model; S2/S3 frozen as historical |
| 6 | **Canonical strategy docs refreshed** — Financial/Construction/Healthcare/Mobility/Infrastructure canonical docs updated from model vNext; DUAL rows collapsed to adopted values with supersession records | Step 5 | Registers with few/no DUALs |
| 7 | **ODP v2** — regenerated under the current project name from the ratified canon + model vNext; v1 reclassified to legacy | Steps 5–6; D-P10 (scenario) ideally decided | Governing program manual, internally consistent |
| 8 | **Prospectus vNext** — per `skills/institutional-prospectus/SKILL.md`; requires completed source reconciliation + model audit; every claim carries the policy claim record | Step 7 + independent audit (Workflow Phase 5) | External-ready narrative |
| 9 | **Design/communications surface (frontend)** — only after Phase 6 corrections; then the Workflow Phase 7 Design-Intelligence connection test | Step 8 + owner approval | Governed external surface |

## Blocking rules

1. **Nothing external before Step 8's audit gate.** External use blocked while any material claim lacks a traceable source or carries an unresolved conflict (CLAIMS_AND_EVIDENCE_POLICY review rule).
2. **No prospectus work before model reconciliation** — the prospectus skill itself orders a stop if unresolved conflicts would change thesis, program, cost, or disclosure. Today OQ-14/15/17/18 all would.
3. **No schematic design authorization before** D-P2 + test-fit + zoning verification + gating studies (ODP's own gate, carried forward).
4. Steps 4's studies can and should run in parallel; the *document* chain stays serial.
5. Any mid-chain owner decision restarts the chain from the step it touches (see dependency table in the [Document Dependency Graph](Document%20Dependency%20Graph.md)).

## What may be updated at any time (no gate)

- [Open Questions](Open%20Questions.md) statuses, [Risk Register](Risk%20Register.md) ratings, [Missing Research Register](Missing%20Research%20Register.md) recoveries, [Decision Log](Decision%20Log.md) entries — these are the live registers; keeping them current is the maintenance duty of every future session.
