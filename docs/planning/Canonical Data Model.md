# Canonical Data Model

**Status:** Ratified Phase 1 standard · **Date:** 2026-07-26
**Authority:** D-P8 records hygiene; D-P9 governance succession; D-P11 repository refactor Phase 1
**Implementations:** [`schemas/`](../../schemas/) · [`exports/`](../../exports/) · [`scripts/`](../../scripts/)

This standard separates statement type, evidence classification, lifecycle status, provenance, and external-use eligibility. Generated data is a derived view; the human-reviewed canon and registers govern.

## Fixed vocabularies

### Statement type

Every material statement uses one:

`verified_fact` · `corroborated_fact` · `source_derived_claim` · `model_output` · `owner_decision` · `adopted_strategy` · `working_assumption` · `scenario` · `recommendation` · `historical_claim` · `rejected_scenario` · `unresolved` · `missing_source_dependency`

### Evidence classification

Every material statement also uses exactly one evidence classification from `AGENTS.md`:

`verified_fact` · `source_derived_but_not_independently_verified` · `current_working_assumption` · `model_output` · `recommendation` · `open_question` · `superseded_assumption` · `rejected_scenario`

Statement type and evidence class are not interchangeable. `owner_decision` or `adopted_strategy` does not mean `verified_fact`.

### Records-hygiene statuses

The D-P8 vocabulary is implemented as separate dimensions so meanings are not blurred:

- `document_status`: `current` · `ratified` · `draft` · `superseded` · `archived`
- `scenario_status`: `current` · `historical` · `rejected_scenario`
- `source_provenance`: `seller_provided` · `third_party` · `owner_provided` · `repository_authored`
- `verification_status`: `verified` · `unverified` · `missing_source_dependency`
- `external_use_status`: `internal_only` · `external_eligible` · `approved_with_caveat` · `blocked_pending_resolution`

### Other vocabularies

- Confidence: `high`, `medium`, `low`
- Source class: `current`, `reference`, `legacy`, `raw`, `governance`
- Partner status: `prospective`, `loi_documented`, `committed_documented`
- Scenario association: `project_wide`, `6_story`, `8_story`, `basis_A_35k`, `basis_B_28k24k`, or a preserved historical/rejected scenario ID

## Material statement record

```text
Statement {
  statement_id
  statement_text
  statement_type
  evidence_class
  document_status
  source_or_decision_provenance[]
  source_location[]
  confidence { level, basis }
  external_use_status
  date_last_reviewed
  dependencies[]
  contradiction_status
  supersedes[]
  superseded_by[]
}
```

All fields are required except supersession arrays, which may be empty. A claim with an unresolved dependency cannot be `external_eligible`.

## Decision

```text
Decision {
  decision_id
  title
  exact_decision_statement
  status: ratified | pending | superseded
  decision_date
  decision_maker
  evidence_or_rationale[]
  affected_documents[]
  superseded_decisions[]
  review_trigger
}
```

## Assumption and model input

```text
Assumption {
  assumption_id
  value_or_range
  unit
  category
  evidence_class
  status
  model_usage[]
  scenario_association[]
  source[]
  external_use_restriction
  owner_decision_requirement
  sensitivity_importance
}
```

Dual values remain separate scenario-associated records. They are never averaged or combined.

## Source

```text
Source {
  source_id
  exact_path
  format
  source_class
  provenance
  authority_tier
  scope
  integrity_sha256
  status
  dependencies[]
}
```

Original sources are immutable. Source-specific filenames and address strings are preserved.

## Scenario

```text
Scenario {
  scenario_id
  title
  scenario_status
  program_basis
  thesis
  source[]
  incompatibilities[]
  adoption_decision
  external_use_status
}
```

No scenario becomes adopted without an explicit owner decision. `6_story` and `8_story` remain active scenarios; neither is adopted.

## Project manifest

The singleton project record contains canonical identity, property/ownership status, adopted thesis, feasibility flag, adopted and pending decisions, pending studies, external restrictions, address aliases, and source-of-truth links. Unsupported model inputs do not enter it as project facts.

## Integrity rules

1. Provenance is required for material claims and quantitative values.
2. Source/decision location must be as precise as available.
3. Program-dependent values carry a scenario/program-basis association.
4. Model outputs stay model outputs.
5. Partner status defaults to `prospective`.
6. Optional Phase 3+ revenue is excluded from a governance-clean base case unless contractually supported and later approved.
7. Historical claims, superseded assumptions, and rejected scenarios are append-only.
8. External eligibility requires the publication gate in `docs/external/EXTERNAL_PUBLICATION_CHECKLIST.md`.
9. Human-reviewed canon/registers govern; exports declare their governing source and generation metadata.
