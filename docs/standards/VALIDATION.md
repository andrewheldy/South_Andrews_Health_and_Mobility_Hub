# Validation Instructions

Run from repository root:

```sh
python3 scripts/generate_exports.py
python3 scripts/validate_repository.py
```

Validation checks JSON/schema shape, decision/assumption IDs, duplicate IDs, claim provenance, unresolved external dependencies, speculative AV base-case treatment, missing governance references, ownership language, inconsistent identity names/addresses, incompatible scenario mixing, source hashes, and internal Markdown links.

The validator is conservative. A flagged phrase is a review cue, not automatic proof of a misleading claim. Correct the record or add an explicit allowlisted historical/source context in the validator.
