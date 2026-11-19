#!/usr/bin/env python3
"""news-image-20261119 entrypoint (Python 3.13, standard library only).

Copies the pre-rendered entry.png beside this file to /output/entry.png
(or $MAKEFUN_OUTPUT_DIR/entry.png outside the grader). Deterministic:
same bytes in, same bytes out, on every run. No network, no imports
beyond the standard library: the grader runs this with `python3 -P -s`
in a pinned image without third-party packages, so this file must never
bring in anything beyond the standard library.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
