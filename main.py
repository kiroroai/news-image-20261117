#!/usr/bin/env python3
"""news-image-20261117 entry runner.

Copies the pre-composed front-page image (entry.png, next to this script)
to the output directory given by MAKEFUN_OUTPUT_DIR (default /output).
Standard library only. Deterministic: the output is a byte-for-byte copy
of entry.png, so repeated runs always produce identical bytes.
No network access, no randomness.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
DEFAULT_OUTPUT_DIR = Path("/output")
OUTPUT_NAME = "entry.png"


def main() -> int:
    if not SOURCE.is_file():
        print(f"error: {SOURCE} not found next to main.py", file=sys.stderr)
        return 1
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", str(DEFAULT_OUTPUT_DIR)))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / OUTPUT_NAME
    shutil.copyfile(SOURCE, output_path)
    if output_path.stat().st_size != SOURCE.stat().st_size:
        print(f"error: copied size mismatch for {output_path}", file=sys.stderr)
        return 1
    print(f"Wrote {output_path} ({output_path.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
