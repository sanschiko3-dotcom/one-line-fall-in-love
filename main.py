#!/usr/bin/env python3
"""Make the Judge Fall in Love in One Line.

Writes one line of at most 240 characters to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (``/output/entry.txt`` in the grader).

The line is the whole entry: a single sentence that tries to make the
reader fall in love with a machine -- a grandmother's radio that keeps
humming for half a second after it is switched off, as if it were
finishing a sentence it started in 1962.

Deterministic: no input, no network, no randomness, no clock. The same
bytes are written on every run.
"""

import os

LINE = (
    "My grandmother's radio still hums for half a second after I switch "
    "it off, as if it's finishing a sentence it started in 1962."
)

assert 1 <= len(LINE) <= 240, "line must be 1-240 characters"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file holds exactly the line, 126 chars.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
