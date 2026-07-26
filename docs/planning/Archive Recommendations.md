# Archive Recommendations

**Status:** Current archive and supersession guidance · **Last reviewed:** 2026-07-26
**Standing constraint:** D-P11 authorizes Phase 1 records hygiene but does not authorize altering original sources. No source was moved, renamed, rewritten, or archived. History is preserved.

## 1. Concept dispositions

| Concept | Where it lives | Recommendation | Rationale |
|---|---|---|---|
| "Agora Mediterranean Market" retail/restaurant center | S6 (appraisal branding & improvements narrative) | **Keep — historical context inside S6 only.** Never referenced as a project concept | Seller's own concept for the property; explains the appraisal branding (OQ-12); zero relevance to buyer program |
| Car-rental fleet "Mobility Hub" (9-story, ~600 stalls) | S8 (entire framing) | **Keep S8 as reference; classify the program as rejected scenario.** Use S8 only for zoning process, massing arithmetic, and valuation/negotiation logic | Buyer-representation study for a different client thesis; AGENTS.md: not rental-car-led |
| "Andrews Mobility Nexus" as primary thesis | S2 governance note; MA-12 (missing context file) | **Rejected scenario — archive the narrative when MA-12 is recovered** | Rejected per Decision-001 (as cited); AGENTS.md bars AV-revenue dependence |
| Residential scheme (~43 units) & hotel scheme (~130 keys) | S8 Scenarios B/C | **Keep as studied alternatives (rejected-for-now)** | Relevant to HBU context and exit optionality; excluded by current scope |
| "South Andrews Clinical & Mobility Center" name | S4, S5 | **Historical name — retain in those documents unaltered; never propagate** | Glossary rule |
| $12.0M listing / $11.1M appraisal as value anchors | S6 | **Keep; always pair with the standing comp critiques (S1 §4, S8 p.7)** | Appraisal opinion ≠ buyer's price |
| ODP v1.0 (S4) | sources/current | **Keep in current class until ODP v2 exists**, then reclassify to legacy | It remains the best program-logic record; superseded only by a ratified successor |
| Legacy Prospectus Vol 0 (S5) | sources/legacy | **Keep exactly where it is** | Already correctly classed; structure/tone reference only |
| Mobility-hub brief counts (200/100/50) | S7 `Assumptions!B36–B38` | **Superseded assumption** — never quote as current program | Traces to an unidentified earlier "project brief" |
| 30%-ITC-netted solar costs | S2 `Budget!B15` | **Flag wherever cited; supersede after tax counsel (D-P7)** | S3's newer sourced position says $0 |

## 2. Deferred original-source actions (not authorized by D-P11)

| Action (proposed) | Target | Notes |
|---|---|---|
| None — no moves/renames/deletions proposed for any source file at this time | — | All eight sources are in their correct class folders already |
| Rename (optional, low priority) | `Andrew’s Appraisal.pdf` → ASCII name; `Appraisal Valuation .xlsx` → remove trailing space; `NativeRealty_905…` → correct address | **Explicitly deferred**: SOURCE_AUTHORITY.md orders these preserved until owner authorizes; if renamed, update SOURCE_AUTHORITY.md references atomically |
| Add `.gitignore` for `.DS_Store` | repo root | Cosmetic hygiene; part of refactoring plan |
| Reclassify | S4 → `sources/legacy/` **only after** ODP v2 is ratified | Not before |

## 3. What must never be archived

- Superseded assumptions and rejected scenarios (they are the audit trail — AGENTS.md requires preserving provenance and superseded assumptions).
- The feasibility yield-gap finding, even if later models improve it (supersede with provenance, don't delete).
- Any source cited by an external representation that has already been shared.

## 4. Archive mechanics (when authorized)

Recommended pattern (see [Repository Refactoring Plan](Repository%20Refactoring%20Plan.md)): an `sources/archive/` class is **not** created; instead, superseded *documents* keep their folder and gain a one-line supersession note in the Source Inventory, while superseded *concepts* are tracked in the [Master Assumption Register](Master%20Assumption%20Register.md) with `SUP`/`REJ` classes. This keeps files stable (no link rot) while the registers carry status — consistent with "record derived work separately from source material."
