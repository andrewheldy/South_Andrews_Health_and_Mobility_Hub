# Structured Export Guidance

`scripts/generate_exports.py` produces the JSON files under `exports/`.

Every export includes:

- schema version;
- generated date;
- source-of-truth document(s);
- document status;
- provenance;
- validation result;
- unresolved dependencies.

The ratified canon and human-reviewed registers govern. Edit those records first, then update the generator’s explicit mapping and regenerate. Do not hand-edit generated JSON.

The export layer is designed for future modeling, ODP/prospectus work, frontend integration, and HeldyOS ingestion. It is not publication approval.
