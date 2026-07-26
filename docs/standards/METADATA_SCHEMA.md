# Repository Metadata Standard

**Status:** ratified Phase 1 standard · **Authority:** D-P8 and D-P11

New human-authored Markdown documents should include YAML front matter or a visible metadata block with:

```yaml
title: Document title
document_status: current | ratified | draft | superseded | archived
scenario_status: current | historical | rejected_scenario
source_provenance: seller_provided | third_party | owner_provided | repository_authored
verification_status: verified | unverified | missing_source_dependency
external_use_status: internal_only | external_eligible | approved_with_caveat | blocked_pending_resolution
date_last_reviewed: YYYY-MM-DD
governing_sources: []
dependencies: []
supersedes: []
superseded_by: []
```

Use only applicable fields; do not collapse the dimensions into one ambiguous status. Material claims additionally follow the canonical data model and claims policy.
