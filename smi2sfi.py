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
