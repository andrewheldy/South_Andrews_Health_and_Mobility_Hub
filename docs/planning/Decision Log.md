# Decision Log

**Status:** Draft for owner review · **Date:** 2026-07-26 · **Author:** AI planning session
**Governing rule (SOURCE_AUTHORITY.md):** an explicit current owner decision controls only when its **content, date, decision-maker, and scope** are documented. This log is the repository's instrument for that documentation.
**Related:** [Open Questions](Open%20Questions.md) · [Project Canon](Project%20Canon.md)

Record format: `D-###` (active) / `D-P#` (pending owner) / `D-H#` (historical, reconstructed). Nothing in this session creates a new owner decision; all substantive entries below are either **reconstructions of cited decisions** (flagged as such) or **pending items awaiting the owner**.

---

## Part 1 — Standing governance decisions (evidenced in-repo)

| ID | Date | Decision-maker | Decision | Scope | Evidence | Status |
|---|---|---|---|---|---|---|
| D-G1 | on/before 2026-07-26 | Owner (via repository governance) | Project name is **South Andrews Healthcare and Mobility Hub**; older names historical only | Naming, all documents | AGENTS.md; PROJECT_GLOSSARY.md | **Active** |
| D-G2 | on/before 2026-07-26 | Owner (via governance) | Healthcare is the anchor; mobility/energy systems are enabling infrastructure; project is not residential-, hotel-, or rental-car-led and not dependent on speculative AV revenue | Thesis & scope | AGENTS.md §Current project scope | **Active** |
| D-G3 | on/before 2026-07-26 | Owner (via governance) | Property status language: prospective acquisition; sponsor does not own the property | All status representations | AGENTS.md; glossary | **Active** |
| D-G4 | on/before 2026-07-26 | Owner (via governance) | 6-story and 8-story schemes remain **scenarios** until an explicit owner decision adopts one | Program | AGENTS.md | **Active** |
| D-G5 | on/before 2026-07-26 | Owner (via governance) | Source-precedence hierarchy and original-workbook protection rules | Evidence handling | AGENTS.md; SOURCE_AUTHORITY.md | **Active** |

## Part 2 — Historical decisions cited but not present in repo (reconstructed; require re-ratification)

> The ODP cites "Project Decision Log Decisions 001–003." The log itself is missing (MA-02). The content below is **reconstructed from citations** — classification: *source-derived, record incomplete*. Re-ratification converts each to an active D-### with proper date/decision-maker.

| ID | Reconstructed content | Cited by | Status |
|---|---|---|---|
| D-H1 (Decision-001) | Adopt the mixed-use clinical & mobility concept as the governing development program; "Pure Mobility Nexus" was among alternatives **considered and rejected** | ODP §1.1 Close-Out, Table 24 | Cited; text not in repo → re-ratify as part of D-P2 |
| D-H2 (Decision-002) | Adopt convertible structured parking (flat plates, external removable ramps, universal grid, 12-ft F2F, selective 100 psf) | ODP Ch.5 | Cited; text not in repo → re-ratify via D-P3 |
| D-H3 (Decision-003) | No speculative AV/edge revenue underwritten as day-one income; technology activations demand- or partner-gated | ODP Ch.9, Table 40 | Cited; text not in repo → re-ratify via D-P4 (content already enforced by AGENTS.md) |

## Part 3 — Pending owner decisions (queued by this planning session)

| ID | Decision required | Options / recommendation | Feeds | Blocks |
|---|---|---|---|---|
| **D-P1** | Ratify acquisition mandate: $8.0M opening offer; ceiling; walk-away | Recommendation: open $8.0M; ceiling $8.75M; walk-away at $9.0M absent new evidence (S8 range; S3 stress case $9.5M) | OQ-20 | Negotiation; all acquisition-basis modeling stays "working assumption" until signed |
| **D-P2** | Formally ratify the healthcare-anchored thesis (closes OQ-01; absorbs D-H1) | Recommendation: ratify as already encoded in AGENTS.md | Canon §1–2 | ODP's own rule: no design spend before this |
| **D-P3** | Re-ratify convertible-structure strategy incl. low-to-mid convertibility premium (~10–15%) | Recommendation: ratify; price premium at GC stage (OQ-10) | Construction Assumptions §1 | Structural engineering brief |
| **D-P4** | Re-ratify no-speculative-AV/edge-revenue rule; order the S3 base-NOI correction (OQ-22) | Recommendation: ratify; authorize model vNext to exclude AV bay revenue from base | Financial Assumptions §2 | Model vNext |
| **D-P5** | Adopt canonical program basis after test-fit (closes OQ-14) | Held until MB-02 delivers | Development Program | Everything sized |
| **D-P6** | Adopt office rent basis (closes OQ-15) | Held until MB-07 comps | Financial Assumptions | NOI/yield credibility |
| **D-P7** | Adopt tax-credit underwriting position (closes OQ-17) | Interim: $0 credits externally; final per counsel MB-13 | Financial Assumptions §4 | Solar/BESS net economics |
| **D-P8** | Sign off OQ-12 closure (appraisal branding = seller's "Agora" concept; same property per folio/legal) | Recommendation: sign off | Source Inventory S6 | Records hygiene |
| **D-P9** | Governance succession: declare AGENTS.md + docs/governance the operative constitution, superseding the missing Constitution/README hierarchy (or direct recovery effort instead) | Recommendation: declare succession; still attempt recovery for the historical record (closes OQ-19) | Whole document layer | Citation hygiene |
| **D-P10** | Adopt scenario (6- vs 8-story) — the height decision | Held until D-P5/D-P6/OQ-18 and model vNext (closes OQ-11) | Canon §7 | Schematic design |
| **D-P11** | Authorize repository refactoring steps (folders, renames incl. the two protected filenames, .gitignore) | Per [Repository Refactoring Plan](Repository%20Refactoring%20Plan.md) | Repo structure | File moves/renames are barred without this |
| **D-P12** | Adopt canonical address string "901–917 S Andrews Avenue" (closes OQ-23) | Recommendation: adopt, pending title confirmation | All documents | Cosmetic but pervasive |

## Part 4 — Log discipline

1. One entry per decision; append-only; superseding decisions reference the superseded ID.
2. No document may cite a D-P# as authority — pending is not decided.
3. Each ratification must state: decision-maker, date, exact scope, and the evidence reviewed.
4. After any ratification batch, re-run the affected rows of the [Contradictions Matrix](Contradictions%20Matrix.md) and the update chain in the [Document Dependency Graph](Document%20Dependency%20Graph.md).
