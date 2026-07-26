# Canonical Data Model

**Status:** Draft for owner review · **Date:** 2026-07-26 · **Author:** AI planning session
**Governing documents:** `AGENTS.md` (evidence classifications), `docs/governance/CLAIMS_AND_EVIDENCE_POLICY.md` (claim record)
**Related:** [Repository Knowledge Graph](Repository%20Knowledge%20Graph.md) · [Master Assumption Register](Master%20Assumption%20Register.md)

Defines the standard entity types, fields, and integrity rules every future repository document, model, and interface must use. This is a *schema*, not data; the data lives in the registers.

## 1. Enumerations (fixed vocabularies)

- **EvidenceClass** (AGENTS.md — exactly one per claim): `verified_fact` · `source_derived` · `working_assumption` · `model_output` · `recommendation` · `open_question` · `superseded_assumption` · `rejected_scenario`
- **Confidence:** `high` · `medium` · `low` (+ one-line basis)
- **ExternalUseStatus** (CLAIMS_AND_EVIDENCE_POLICY): `approved` · `approved_with_caveat` · `internal_only` · `blocked`
- **SourceClass:** `current` · `reference` · `legacy` · `raw` · `governance`
- **AuthorityTier** (AGENTS.md hierarchy 1–8): owner_decision → corrected_assumptions → 6v8_model → 8m_feasibility → owner_program → verified_primary → third_party → legacy
- **PartnerStatus:** `prospective` (default; only a documented commitment changes it) · `loi` · `committed_documented`
- **ScenarioStatus:** `scenario` (default) · `adopted_by_owner_decision` · `rejected`
- **ProgramBasis:** `basis_A_35k` (S2) · `basis_B_28k24k` (S3) · `tbd_test_fit` — every sized figure must carry one

## 2. Core entities

### Claim (the atomic unit — required for every material statement)
```
Claim {
  id:            CLM-###
  text:          the claim, stated with units/period/scenario
  class:         EvidenceClass
  source:        Source.id + location (page / sheet!cell / section)
  date:          source date (not file date, where known)
  confidence:    Confidence + basis
  caveat:        required qualifying language (verbatim)
  external_use:  ExternalUseStatus
  supersedes / superseded_by: Claim.id (history never deleted)
  conflicts_with: [Claim.id]      // must map to a Contradictions Matrix row
  depends_on:    [Claim.id | OpenQuestion.id]
}
```
Rules: no claim promoted above its class; a caveat elsewhere never cures a misleading headline; conflicting claims are both preserved.

### Source
```
Source { id: S#, path (exact, incl. preserved typography), format, size,
         file_date, internal_date, author/provenance, class: SourceClass,
         authority_tier, scope (topics it may control), integrity_notes,
         cites: [Source.id | MissingDoc.id], status: present|missing }
```
Missing documents (MA-xx) are first-class `Source{status:missing}` records so citations to them are visible, not silent.

### Assumption (specialized Claim used as model input)
```
Assumption { id (SITE-/ZON-/ACQ-/PRG-/CST-/FIN-/REV-/EXT-/NRG-/HC-/MOB-##),
             values: [{value, unit, program_basis, source}],   // DUAL = >1 live value
             canonical: yes|dual|context|no,
             resolution_path: OpenQuestion.id | research MB-## }
```
Rule: a `dual` assumption renders as both values or not at all — never a midpoint.

### Decision
```
Decision { id: D-### (D-P## while pending), date, decision_maker, decision,
           scope, rationale, evidence: [Claim.id], status: pending|active|superseded,
           affects: [Assumption.id | Scenario.id | document] }
```
An owner decision controls only when content, date, decision-maker, and scope are documented (SOURCE_AUTHORITY.md).

### OpenQuestion
```
OpenQuestion { id: OQ-##, question, priority: critical|high|medium|low,
               gates: [what it blocks], resolve_via: study|owner_decision|document_recovery,
               status: open|partially_resolved|resolved_pending_signoff|closed(Decision.id) }
```

### Scenario
```
Scenario { id: 6-story|8-story|rejected-*, status: ScenarioStatus,
           program_basis, program_table, model_outputs: [Claim.id class=model_output] }
```

### ProgramComponent
```
ProgramComponent { name, role, phase: 1|2|3+, sizing: value|TBD(program_basis),
                   activation_trigger (required for phase 3+), revenue_in_base_case: bool }
```
Rule: `phase 3+ ⇒ revenue_in_base_case = false`.

### Partner
```
Partner { name, type: health_system|operator|fleet|utility|city|capital,
          status: PartnerStatus = prospective, evidence, permitted_language }
```

### Risk
```
Risk { id: R-##, description, probability: L|M|H, impact: L|M|H,
       mitigation, validation_required, source, status: open|retired|re-rated }
```

### Site (singleton)
Fields: address_canonical ("901–917 S Andrews Avenue, Fort Lauderdale, FL 33316"), address_variants[], folio, legal_description, land_sf=38,207, acres=0.88, frontages, zoning=RAC-RPO, flu=SRAC, flood_zone=AE(map,date), bfe≈5ft(unverified), qoz=true(SD), improvements, owner_of_record, utilities{present, capacity_status:unverified}.

### Milestone / Study
```
Study { id: MB-##, name, purpose, gates: [OpenQuestion.id | Decision.id],
        priority, status: not_started|commissioned|complete, resolves: [Assumption.id] }
```

## 3. Integrity rules (repo-wide)

1. **Provenance or it doesn't exist:** every quantitative value carries `source + location`; workbook citations are cell-level.
2. **Single-canonical-with-preserved-variants:** one canonical value (or an explicit DUAL) plus all displaced values kept as `superseded_assumption` / `rejected_scenario`.
3. **Basis tagging:** any figure derived from a sized program carries `ProgramBasis`.
4. **Status language:** entity renderers must emit the approved status vocabulary (proposed, prospective, planning-level, subject to …) whenever ExternalUseStatus ≠ approved.
5. **Model output firewall:** `model_output` claims never mutate into `verified_fact` by repetition; inputs never become facts because a model used them.
6. **Downstream consistency:** editing any Assumption requires touching every document listed in its `affects` chain (tracked via the [Document Dependency Graph](Document%20Dependency%20Graph.md)).
7. **Partner default:** absent documentation, `PartnerStatus = prospective` and naming uses "potential partner" language.
8. **History append-only:** decisions, superseded values, and rejected scenarios are never deleted, only re-statused.

## 4. Where each entity's data lives today

| Entity | Authoritative register |
|---|---|
| Claim/Assumption | [Master Assumption Register](Master%20Assumption%20Register.md) |
| Source | [Source Inventory](Source%20Inventory.md) + [Source Authority Register](Source%20Authority%20Register.md) |
| Decision | [Decision Log](Decision%20Log.md) |
| OpenQuestion | [Open Questions](Open%20Questions.md) |
| Risk | [Risk Register](Risk%20Register.md) |
| Scenario/Program | [Current Development Program](Current%20Development%20Program.md) |
| Study | [Missing Research Register](Missing%20Research%20Register.md) Part B |
| Conflicts | [Contradictions Matrix](Contradictions%20Matrix.md) |

A future structured store (YAML/JSON per entity) may be generated from these registers during implementation — see [Repository Refactoring Plan](Repository%20Refactoring%20Plan.md).
