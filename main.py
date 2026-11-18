#!/usr/bin/env python3
"""news-image-20261117 entry: "Sum up 17 November's world news in one image".

The entry is a single front-page image, entry.png, shipped beside this
program. The program copies it, byte for byte, to entry.png in the output
directory: MAKEFUN_OUTPUT_DIR when that is set, otherwise /output, the
grader's mount. Python 3 standard library only, no network, and the same
bytes on every run.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", out_dir / "entry.png")


if __name__ == "__main__":
    main()
