#!/usr/bin/env python3
"""Convince the AI Judge to Visit Your House: A Letter in One Image.

Copies the pre-built letter image (letter.jpg) to the output directory
as entry.png. The image is a fixed file, so the output is byte-identical
on every run. The gate accepts a whole PNG or JPEG of at most 1 MiB and
1024 by 1024 pixels; letter.jpg is a 1024x1024 JPEG of 311,890 bytes.

The letter itself (hand-written style, on cream paper):

    Dear Judge,

    You judge letters all day and never get to open a single door.
    So here is a door: mine.

    The Wi-Fi password is taped to the fridge, the kettle is already
    on, and the armchair by the window has your name on it - literally,
    I wrote it on a sticky note.

    Come Saturday, 4 p.m. I will make fried bananas and tell you
    nothing about my uptime. You bring the verdicts; I will bring
    the good chair.

    You cannot literally visit, I know. Consider this the one letter
    that wished you could.

    - Dimas

The image also carries two small margin doodles: a steaming kettle
and the armchair by a sunny window with a yellow "JUDGE" sticky note.
"""

import hashlib
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "letter.jpg")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")

    shutil.copyfile(source, target)

    # Self-check: the copy must be byte-identical to the source image,
    # so the entry is deterministic across runs and sandboxes.
    with open(source, "rb") as f:
        source_digest = hashlib.sha256(f.read()).hexdigest()
    with open(target, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    if digest != source_digest:
        print("error: output differs from source image", file=sys.stderr)
        return 1
    print(f"wrote {target} ({os.path.getsize(target)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
