#!/usr/bin/env python3
"""Say what actually broke — a make.fun entry.

The program writes one line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt): a software error message that tells
the brutal truth about what actually broke, in plain words, and what
to do next. The line is 134 characters, inside the competition's
gate of 1 to 200 characters of UTF-8 text. Standard library only, no
network, and deterministic: the same bytes on every run.
"""

import os

LINE = "Error: the server is down because someone deployed on Friday at 4:58 p.m. Nothing you retry will fix this. Go home; we will email you."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The entry file holds exactly the one line: no trailing newline, so
    # the text the judge reads is the line itself, byte for byte — the
    # gate counts characters, and a trailing newline would spend one.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
