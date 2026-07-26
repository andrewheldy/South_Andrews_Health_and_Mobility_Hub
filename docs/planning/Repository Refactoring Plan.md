# Repository Refactoring Plan

**Status:** Draft for owner review — **recommendations only; nothing executed** (requires D-P11) · **Date:** 2026-07-26 · **Author:** AI planning session
**Standing constraints:** originals never edited/moved/renamed without owner instruction; derived work stored separately; protected filenames preserved until authorized.

## 1. Target folder architecture

```
/                           (repo root)
├── AGENTS.md               (operative constitution — unchanged)
├── CLAUDE.md
├── README.md               (NEW: index + document hierarchy + how to navigate)
├── docs/
│   ├── governance/         (unchanged, controlling)
│   ├── planning/           (this set — constitutional planning layer)
│   ├── decisions/          (NEW: one file per ratified decision, D-###.md)
│   ├── claims/             (NEW: claim records per CLAIMS_AND_EVIDENCE_POLICY,
│   │                        generated from the Master Assumption Register)
│   └── strategy/           (FUTURE: ODP v2 chapters once regenerated)
├── sources/
│   ├── current/  reference/  legacy/  raw/     (unchanged)
├── derived/                (NEW: read-only extractions & normalized data)
│   ├── workbooks/          (per-sheet CSV/MD extracts of S2/S3/S7 with
│   │                        cell-level provenance headers — satisfies the
│   │                        financial-model-audit "separately stored derived
│   │                        summaries" requirement)
│   └── documents/          (text extractions of S4/S5/S6/S8 with page/paragraph anchors)
└── skills/                 (unchanged)
```

Rationale: sources stay immutable; everything derivative gets a provenance-stamped home; decisions and claims become first-class records instead of living only inside prose.

## 2. Naming conventions (for NEW files only)

- ASCII, no trailing spaces, no smart quotes; words separated by spaces or hyphens consistently within a folder.
- Derived files: `derived/workbooks/S2_6v8_Assumptions.csv` — source ID prefix mandatory.
- Decisions: `docs/decisions/D-001 <slug>.md`.
- Existing source filenames **unchanged** until D-P11 explicitly authorizes: `Andrew’s Appraisal.pdf` (curly apostrophe), `Appraisal Valuation .xlsx` (trailing space), `NativeRealty_905 …` (address mismatch with content). If renamed later, update `docs/governance/SOURCE_AUTHORITY.md` in the same commit.

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
| `.DS_Store` (root, sources/) | Add `.gitignore` entry; `git rm --cached` |
| Empty `sources/raw/` | Keep; document intake convention in README |
| Workbook protection | Consider `chmod a-w` advisory note in README (originals are already treated read-only by governance) |

## 8. Knowledge-graph tooling (optional, later)

Once `docs/claims/` exists, a small script can emit the [Repository Knowledge Graph](Repository%20Knowledge%20Graph.md) mermaid from frontmatter — keeping graph and registers from drifting. Not required for the current phase.

## 9. Execution order (after D-P11)

1. Add README.md + `.gitignore` (no source impact).
2. Create `derived/` and generate provenance-stamped extractions of S2/S3/S7 (read-only pass).
3. Create `docs/decisions/` and migrate ratified decisions from the [Decision Log](Decision%20Log.md).
4. (Only if separately authorized) filename normalizations with same-commit governance-doc updates.
5. Regenerate the Document Dependency Graph from frontmatter.
