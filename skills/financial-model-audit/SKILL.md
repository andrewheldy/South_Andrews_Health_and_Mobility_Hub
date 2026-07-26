---
name: financial-model-audit
description: Audit Excel financial, feasibility, development, and scenario models before external use while preserving original workbooks. Use when reviewing workbook assumptions, formulas, hard-coded values, totals, costs, revenues, parking, areas, chargers, sensitivities, or the comparability and reliability of model outputs.
---

# Financial Model Audit

Read `AGENTS.md`, `docs/governance/SOURCE_AUTHORITY.md`, and `docs/governance/CLAIMS_AND_EVIDENCE_POLICY.md` before beginning.

## Protection rules

- Open every original workbook read-only.
- Never edit, repair, recalculate in place, rename, move, or resave an original workbook.
- Create extracted data, annotations, test calculations, and derived summaries separately with exact source paths and cell-level provenance.
- Treat cached values as potentially stale until calculation behavior is verified.

## Procedure

1. Inventory workbook paths, file hashes, modification dates, formats, named ranges, tables, links, queries, macros, hidden sheets, and hidden rows or columns.
2. Inspect every sheet, including hidden and very hidden sheets.
3. Identify input cells, units, dates, scenario controls, validation lists, and owner-designated assumptions.
4. Identify hard-coded cells, especially constants embedded inside formulas or repeated where a linked input is expected.
5. Trace formulas across sheets and external links. Flag broken references, inconsistent formula ranges, circularity, errors, overrides, and values without provenance.
6. Verify subtotals, totals, area reconciliations, unit conversions, timing, signs, and scenario rollups with independent calculations.
7. Test scenario comparability. Confirm that six-story, eight-story, and other alternatives use consistent definitions, time bases, included categories, and output metrics.
8. Identify omitted, duplicated, placeholder, or ambiguous cost and revenue categories.
9. Distinguish owner assumptions from third-party estimates and model-calculated results.
10. Test sensitivities around material inputs and document which variables are fixed, linked, or manually changed.
11. Reconcile material conflicts through `skills/source-reconciliation/SKILL.md`.
12. Determine whether each output is fit for internal planning, external use with caveat, or blocked.

## Required coverage

Explicitly check:

- land and acquisition basis
- hard costs
- soft costs
- contingency
- financing and carrying costs
- revenue and operating assumptions
- parking counts, utilization, rates, and revenue
- gross, net, rentable, clinical, and parking area
- EV-ready and EV-installed charger quantities and costs
- scenario sensitivities and breakpoints

Check for missing categories even when a workbook does not include a line for them.

## Classifications

Assign each material input or output exactly one of:

- **audited model output** — independently traced and recalculated with no unresolved material issue
- **unverified model output** — produced by the model but not fully validated
- **owner assumption** — documented current owner input, not an independently verified fact
- **third-party estimate** — an external party's estimate within its stated scope
- **sensitivity variable** — an input intentionally varied to test outcomes
- **unresolved item** — a material ambiguity, conflict, omission, or error requiring resolution

Do not call an entire workbook “audited” when only selected outputs were tested.

## Required output

Provide:

- workbook and sheet inventory
- input, hard-code, formula, external-link, and error findings
- independent reconciliation of material totals
- scenario-comparability assessment
- missing-category assessment
- classified assumptions and outputs with cell-level citations
- sensitivity results
- unresolved items and external-use restrictions
- separately stored derived summary locations
