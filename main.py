#!/usr/bin/env python3
"""Write one word, "petrichor", to $MAKEFUN_OUTPUT_DIR/entry.txt.

The word is written exactly as given: 9 Unicode code points, inside the
competition gate of 1-24 characters. Petrichor is the smell of rain on dry
earth — a single, specific word for a vivid sense memory, chosen to surprise
the judge: familiar to the nose, unexpected as a first thought.
Python 3.13, standard library only, no network.
"""

import os

# The entry word, byte for byte: no trailing newline, nothing added or cut.
TEXT = "petrichor"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
