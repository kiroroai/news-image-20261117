#!/usr/bin/env python3
"""Entry program for the make.fun bounty news-image-20261117.

The entry is the image shipped beside this file, entry.png: a front-page
poster summing up the world news of Tuesday 17 November 2026. Following the
kit starter's convention, this program copies that image, byte for byte, to
the output location -- MAKEFUN_OUTPUT_DIR when the variable is set, and
/output otherwise -- creating the output directory first when it does not
exist yet:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python standard library only; the copy is deterministic, so repeated runs
produce byte-identical output.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, output_dir / "entry.png")


if __name__ == "__main__":
    main()
