# .sfi File Format Specification

**Version:** 1.0  
**Extension:** `.sfi`  
**MIME Type:** `chemical/x-selfies`  
**Encoding:** UTF-8  

## Overview

`.sfi` is the SELFIES equivalent of `.smi`. Same structure, same rules — just SELFIES strings instead of SMILES strings.

A SELFIES string is a sequence of bracket-enclosed tokens (e.g. `[C][C][O]`) as defined by the [selfies](https://github.com/aspuru-guzik-group/selfies) library.

## Format

Plain text, one molecule per line:

```
SELFIES<whitespace>name
```

- **Column 1** — SELFIES string (required). No spaces within the string.
- **Column 2** — Molecule name or ID (optional). Separated from column 1 by space or tab.

That's it. Identical to how `.smi` works.

## Example

```
[C][C][O]	ethanol
[C][=C][C][=C][C][=C][Ring1][=Branch1]	benzene
[C][=Branch1][C][=O][O]	acetic_acid
[C][C][C]
```

## License

AGPL-3.0 — https://github.com/morawskidotmy/.sfi
