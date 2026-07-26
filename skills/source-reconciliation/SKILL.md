---
name: source-reconciliation
description: Reconcile conflicting project documents and claims using the repository's source authority, evidence classifications, and escalation rules. Use when inventorying sources, comparing old and current values, resolving narrative or model conflicts, building a conflict table, or selecting a defensible value for downstream work.
---

# Source Reconciliation

Read `AGENTS.md` and `docs/governance/SOURCE_AUTHORITY.md` before beginning.

## Procedure

1. **Create a source inventory.** Record each relevant file's exact path, document type, apparent date, provenance, current/reference/legacy/raw class, and intended scope. Do not infer content from the filename.
2. **Check date and authority.** Identify publication and revision dates where available. Assign the source-precedence tier and note scope limitations.
3. **Extract claims faithfully.** Capture each claim with its units, time period, scenario, caveats, and page, section, sheet, range, or formula. Do not normalize away meaningful differences.
4. **Classify each claim.** Distinguish factual, modeled, and assumed material using the evidence classifications in `AGENTS.md`.
5. **Apply the source hierarchy.** Compare authority, date, scope, and internal support. A higher-tier source controls only within its proper scope.
6. **Do not average.** Never average conflicting values unless an owner explicitly directs a separately labeled analytical calculation.
7. **Do not cherry-pick.** Never select a favorable value merely because it improves the project narrative, feasibility, returns, or appearance.
8. **Decide or escalate.** Adopt a value only when justified. Otherwise classify it as an open question and escalate the material conflict for owner review.
9. **Preserve history.** Retain displaced claims as superseded assumptions or rejected scenarios with their source and treatment.
10. **Check downstream consistency.** Find every affected narrative, table, model input, calculation, caption, rendering label, and interface. Update only within the authorized phase and record any blocked downstream work.

## Required output

Produce a conflict table using exactly these columns:

| Topic | Old value | Old source | Current value | Controlling source | Status | Treatment |
|---|---|---|---|---|---|---|

In **Status**, use the evidence classifications in `AGENTS.md`. In **Treatment**, state adopted, superseded, rejected, or unresolved/escalated and explain any required downstream correction or caveat.

Conclude with:

- adopted values and rationale
- unresolved conflicts and required owner decisions
- preserved superseded assumptions and rejected scenarios
- affected downstream artifacts
- source and scope limitations
