# South Andrews Healthcare and Mobility Hub

Canonical repository for evidence-based planning and implementation of a **proposed** healthcare-anchored, mixed-use institutional project at **901–917 South Andrews Avenue, Fort Lauderdale, Florida**.

**Property status: Prospective acquisition. The sponsor does not currently own the property.**

Both current financial models independently indicate that the base project, as presently modeled at an $8,000,000 land basis, does not satisfy the modeled institutional return requirements. This is a planning-level model conclusion, not a prediction or guarantee.

## Governing reading order

1. [`AGENTS.md`](AGENTS.md)
2. [`docs/governance/SOURCE_AUTHORITY.md`](docs/governance/SOURCE_AUTHORITY.md)
3. [`docs/governance/PROJECT_GLOSSARY.md`](docs/governance/PROJECT_GLOSSARY.md)
4. [`docs/governance/CLAIMS_AND_EVIDENCE_POLICY.md`](docs/governance/CLAIMS_AND_EVIDENCE_POLICY.md)
5. [`docs/governance/WORKFLOW.md`](docs/governance/WORKFLOW.md)
6. [Ratified Project Canon](docs/planning/Project%20Canon.md)
7. [Decision Log](docs/planning/Decision%20Log.md) and [individual decisions](docs/decisions/)
8. [Executive Planning Summary](docs/planning/Executive%20Planning%20Summary.md) and the remaining planning/register set

`AGENTS.md` and the current governance set are operative. A recovered prior Constitution or Decision Log is historical evidence pending reconciliation; it does not automatically govern.

## Repository boundaries

- `sources/`: immutable original evidence, preserving exact filenames and source-specific language.
- `docs/planning/`: ratified canon plus the human-reviewed planning/evidence layer.
- `docs/decisions/`: individual ratified owner decisions.
- `docs/registers/`: register navigation; governing human registers remain linked to planning documents.
- `docs/standards/`: metadata, source handling, export, and validation guidance.
- `docs/external/`: external-publication gate; no marketing approval is implied.
- `derived/`: reproducible extractions or normalized analysis, never original evidence.
- `schemas/`: machine-readable contracts.
- `exports/`: generated JSON views; never a parallel source of truth.
- `models/`: boundaries for future current/working/archived models and model-input exports.
- `scripts/`: readable generation and validation tools.

## Current decision state

Ratified on 2026-07-26: D-P1, D-P2, D-P8, D-P9, D-P11, D-P12.
Ratified on 2026-07-29: **D-P13** (acquisition negotiation basis), **D-P14** (advisor research source classification).

D-P13 sets the current **nonbinding working opening-offer basis at $7,500,000** — a tactical negotiation figure, not an economically supported land value, and not authority to submit an offer. It supersedes only D-P1's $8,000,000 figure; **the modeled land basis remains $8,000,000** and the two are never blended. The feasibility conclusion is unchanged.

Pending: D-P5 program/floor plate, D-P6 rent basis, D-P7 tax treatment, D-P10 final story selection, D-P15 counsel engagement and disclosure authority, D-P16 transaction authority and price limits, and all other unresolved economic, partner, entitlement, utility, and transaction-authority questions in the canon.

## Validation

Run:

```sh
python3 scripts/generate_exports.py
python3 scripts/validate_repository.py
```

See [validation instructions](docs/standards/VALIDATION.md). Original source files must never be edited by these commands.
