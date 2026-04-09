# .sfi File Format Specification

**Version:** 1.0  
**Extension:** `.sfi`  
**MIME Type:** `chemical/x-selfies`  
**Encoding:** UTF-8  

## Overview

`.sfi` is the SELFIES equivalent of `.smi`. Same structure, same rules — SELFIES strings replace SMILES strings.

A SELFIES string is a sequence of bracket-enclosed tokens (e.g. `[C][C][O]`) as defined by the [selfies](https://github.com/aspuru-guzik-group/selfies) library.

## Format

Plain text, one molecule per line:

```
SELFIES<whitespace>name
```

- **Column 1** — SELFIES string (required). No whitespace inside the SELFIES string.
- **Column 2** — Molecule name or ID (optional). Separated from column 1 by one or more spaces or a tab. Names must not contain tabs or newlines. Spaces in names are permitted but not recommended; prefer underscores or use a separate metadata file if names require arbitrary whitespace or quoting.
- Lines beginning with `#` are comments and MUST be ignored by readers.
- Empty or whitespace-only lines MUST be ignored.
- Leading and trailing whitespace around the whole line SHOULD be trimmed before parsing.
- Tabs and spaces may be used interchangeably as the column separator; internal SELFIES tokens must not contain whitespace.

## Character encoding and normalization

- Files are UTF-8 encoded. Readers SHOULD expect and correctly handle UTF-8.
- SELFIES tokens consist of ASCII bracketed tokens as defined by the selfies specification; readers MUST reject lines where the SELFIES column contains whitespace characters.
- Name fields may contain UTF-8 characters; readers SHOULD preserve and output them verbatim.

## Error handling and interoperability

- On malformed lines (invalid SELFIES, unbalanced brackets, or SELFIES containing whitespace), readers SHOULD report a warning including the line number and either:
  - skip the line and continue (recommended for bulk processing), or
  - fail the conversion with a clear error (recommended for strict validation tools).
- Implementations SHOULD provide an option to be strict (fail on first error) or permissive (skip and log).
- When converting from `.smi` to `.sfi`, tools SHOULD validate input SMILES before encoding to SELFIES and emit warnings for any conversion failures.

## Name field details

- Names are optional. If present, the first contiguous whitespace separates the SELFIES string from the name; the remainder of the line is the name.
- Because the separator is whitespace, names containing leading/trailing whitespace will be trimmed by most readers. To include spaces in a name reliably, use underscores or keep a separate mapping file (e.g., TSV/CSV) referenced alongside the `.sfi` file.
- Names MUST not contain tabs or newlines.

## Recommended machine-readable grammar

A permissive regex for validating a simple line (readers may implement stricter checks):

```
^\s*((\[[^\]\[]+\])+)\s*(?:\s+(.+?))?\s*$
```

Captures:
- Group 1: full SELFIES string (one or more bracket-enclosed tokens)
- Group 3: optional name (rest of the line after separation)

## Examples and edge cases

Valid:
```
[C][C][O]	ethanol
[C][=C][C][=C][C][=C][Ring1][=Branch1] benzene
[C][C][C]
# comment: this is ignored
```

Invalid / should be rejected or warned:
```
[C] [C][O]    # contains whitespace inside SELFIES
[C][C][O]ethanol  # no separator between columns
[C][C         # unbalanced bracket
```

## Versioning and stability

- This document describes `.sfi` format v1.0. Future revisions SHOULD increment the version and document changes in the repository.

## License

AGPL-3.0 — https://github.com/morawskidotmy/.sfi

---
