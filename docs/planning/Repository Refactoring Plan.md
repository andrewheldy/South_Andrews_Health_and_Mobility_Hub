# Repository Refactoring Plan

**Status:** Phase 1 authorized by D-P11 and implemented on 2026-07-26 · **Date:** 2026-07-26
**Standing constraints:** originals never edited/moved/renamed without owner instruction; derived work stored separately; protected filenames preserved until authorized.

## 1. Implemented Phase 1 architecture

```
/                           (repo root)
├── AGENTS.md               (operative constitution — unchanged)
├── CLAUDE.md
├── README.md               (NEW: index + document hierarchy + how to navigate)
├── docs/
│   ├── governance/         (unchanged, controlling)
│   ├── planning/           (this set — constitutional planning layer)
│   ├── decisions/          (NEW: one file per ratified decision, D-###.md)
│   ├── canon/              (index to ratified canon; source remains in planning for link stability)
│   ├── decisions/          (one file per ratified owner decision)
│   ├── registers/          (human-readable register index)
│   ├── research/ technical/ financial/ program/ partnerships/
│   ├── external/           (publication gate; no marketing material)
│   ├── archive/            (archive/supersession map)
│   └── standards/          (metadata, source handling, export guidance)
├── sources/
│   ├── current/  reference/  legacy/  raw/     (unchanged)
├── derived/                (generated or normalized work; never a source of truth)
│   ├── workbooks/          (per-sheet CSV/MD extracts of S2/S3/S7 with
│   │                        cell-level provenance headers — satisfies the
│   │                        financial-model-audit "separately stored derived
│   │                        summaries" requirement)
│   └── documents/          (text extractions of S4/S5/S6/S8 with page/paragraph anchors)
├── schemas/ scripts/ templates/
├── models/current/ working/ archived/ exports/
└── exports/                (generated JSON views with validation metadata)
```

Rationale: sources stay immutable; everything derivative gets a provenance-stamped home; decisions and claims become first-class records instead of living only inside prose.

## 2. Naming conventions (for NEW files only)

- ASCII, no trailing spaces, no smart quotes; words separated by spaces or hyphens consistently within a folder.
- Derived files: `derived/workbooks/S2_6v8_Assumptions.csv` — source ID prefix mandatory.
- Decisions: `docs/decisions/D-001 <slug>.md`.
- Existing source filenames remain **unchanged**. D-P11 authorizes Phase 1 repository-authored structure, not original-source renames: `Andrew’s Appraisal.pdf`, `Appraisal Valuation .xlsx`, and `NativeRealty_905 …` are preserved. Any future source rename requires separate explicit owner instruction and atomic reference updates.

## 3. Metadata standard (frontmatter for all new docs)

```yaml
---
title:            <document title>
status:           draft | owner-review | ratified | superseded
date:             YYYY-MM-DD
author:           <person or session>
depends_on:       [list of documents/registers]
sources_cited:    [S1..S8, MA-xx]
evidence_note:    "classifications per AGENTS.md; no claim above its class"
supersedes:       <doc or "">
---
```
Purpose: lets the [Document Dependency Graph](Document%20Dependency%20Graph.md) be regenerated mechanically and makes supersession explicit.

## 4. Index & navigation

- **README.md (new):** project one-paragraph (canon-consistent), document hierarchy (AGENTS.md → governance → planning → decisions → strategy), reading order for new collaborators/AI sessions, and the property-status line verbatim.
- **docs/planning/ index:** the [Executive Planning Summary](Executive%20Planning%20Summary.md) doubles as the entry point; every planning doc cross-links its relatives in the header.

## 5. Versioning & supersession

- Git history is the version record; no `v2_final_FINAL` filenames.
- A document is superseded by a successor that names it in `supersedes:`; the old file gains a one-line banner ("Superseded by X on DATE") — content otherwise untouched.
- Workbooks: never versioned in place. A successor model is a **new file** (e.g., `South_Andrews_Model_v2.xlsx`) built from ratified register values; S2/S3 remain frozen originals.
- Owner decisions are the only mechanism that flips `status: ratified`.

## 6. Cross-reference style

- Relative markdown links; cite sources as `S# (sheet!cell)` or `S# p.N`.
- Citations to missing documents always via "as cited by Sx" (never bare).
- Every quantitative claim carries its evidence class inline or in an adjacent table column.

## 7. Hygiene items

| Item | Action (when authorized) |
|---|---|
| `.DS_Store` (root, sources/) | `.gitignore` added; tracked artifact removed from the repository index |
| Empty `sources/raw/` | Keep; document intake convention in README |
| Workbook protection | Consider `chmod a-w` advisory note in README (originals are already treated read-only by governance) |

## 8. Knowledge-graph tooling (optional, later)

Once `docs/claims/` exists, a small script can emit the [Repository Knowledge Graph](Repository%20Knowledge%20Graph.md) mermaid from frontmatter — keeping graph and registers from drifting. Not required for the current phase.

## 9. Phase 1 execution record

1. README, `.gitignore`, navigation indexes, and generated-output boundaries added.
2. Decision records, schemas, structured exports, external-use controls, archive map, templates, and validation added.
3. Source hashes recorded; original sources and protected filenames unchanged.
4. No source filename normalization or source-file move was performed.
5. Model-vNext, ODP v2, prospectus, and frontend remain later gated work.
