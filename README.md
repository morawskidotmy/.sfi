# .sfi — SELFIES File Format

The `.smi` format, but for [SELFIES](https://github.com/aspuru-guzik-group/selfies) instead of SMILES.

```
[C][C][O]	ethanol
[C][=C][C][=C][C][=C][Ring1][=Branch1]	benzene
```

One molecule per line. SELFIES string first, optional name after whitespace. Drop-in replacement for `.smi` in any pipeline — just swap the notation.

See [SPECIFICATION.md](SPECIFICATION.md) for the full spec.

## Convert .smi → .sfi

```python
#!/usr/bin/env python3
"""Convert .smi to .sfi"""

import sys
import selfies as sf

for line in open(sys.argv[1]):
    line = line.strip()
    if not line:
        continue
    parts = line.split(None, 1)
    smiles = parts[0]
    name = parts[1] if len(parts) > 1 else ""
    try:
        selfies = sf.encoder(smiles)
    except Exception:
        print(f"# failed: {smiles}", file=sys.stderr)
        continue
    if name:
        print(f"{selfies}\t{name}")
    else:
        print(selfies)
```

```bash
python smi2sfi.py input.smi > output.sfi
```

## License

AGPL-3.0
