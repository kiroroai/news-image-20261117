#!/usr/bin/env python3
"""Entry program for the make.fun bounty news-image-20261117.

The entry image ships beside this file as entry.png. Running the program
copies it, byte for byte, to the output directory: MAKEFUN_OUTPUT_DIR when
that environment variable is set, otherwise /output. The output directory
is created when it does not exist yet.

Python standard library only; no network access.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
