# Repository Automation

- `generate_exports.py`: generates the 11 canonical JSON views.
- `validate_repository.py`: validates exports, IDs, provenance, external-use dependencies, governance/status language, scenario discipline, links, and source hashes; also enforces the internal Institutional Investment Memorandum controls (canonical name/address, feasibility-finding presence, per-occurrence D-P1 land-basis qualification, prohibited promotional language, internal_only status).
- `verify_workbook_claims.py`: read-only display of key original-workbook values and formulas used by the canon’s feasibility finding.

None of these scripts modifies an original source.
