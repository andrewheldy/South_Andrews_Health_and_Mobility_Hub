---
title: D-P8 Records hygiene
document_status: ratified
decision_date: 2026-07-26
decision_maker: Owner
external_use_status: internal_only
---

# D-P8 — Records hygiene

**Decision.** Repository materials may carry one or more controlled status dimensions using: `current`, `ratified`, `draft`, `superseded`, `historical`, `rejected_scenario`, `seller_provided`, `third_party`, `unverified`, `missing_source_dependency`, `internal_only`, `external_eligible`, and `archived`.

Document lifecycle, provenance, scenario treatment, verification, and external-use eligibility are separate dimensions; a single undifferentiated status must not blur them.

Historical claims, rejected scenarios, superseded assumptions, and unfavorable evidence are preserved with provenance and supersession links. Generated exports are derived and never become a parallel source of truth.

**Affected:** metadata schema, registers, archive map, source handling, exports, validation.

**Review trigger:** Status vocabulary or retention-policy amendment.
