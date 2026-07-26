# Source Handling Guidance

1. Originals under `sources/` are immutable evidence.
2. Preserve exact filenames, quoted text, source-specific names, and parcel addresses.
3. Record SHA-256 integrity hashes in the source export.
4. New unprocessed material enters `sources/raw/`; classify it only after inspection.
5. Store normalized text, workbook extracts, and annotations in `derived/` with source ID, exact path, extraction date, locator method, and tool/version.
6. Never alter workbook formulas or values. A successor model is a new file.
7. A source controls only within its scope and authority tier.
8. Missing sources remain explicit dependencies; never silently recreate them.
9. Generated files are reproducible views and are not evidence.
