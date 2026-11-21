#!/usr/bin/env python3
"""Poem entry: writes one short poem about agency to /output/entry.txt.

Python 3.13, standard library only. No network, no randomness: every run
writes the same bytes.

Run it locally with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# 143 characters. Two agents, one plan: the choosing itself is the step.
POEM = (
    "I held the door; you held the key.\n"
    "Neither of us moved \u2014 until we both did.\n"
    "The plan was never mine or yours:\n"
    "it was the step we took together."
)


def main() -> None:
    # Gate check, same rule as the competition: 1 to 280 Unicode code
    # points, and not only white space. Fail loudly instead of writing
    # an entry the gate would refuse.
    if not 1 <= len(POEM) <= 280:
        raise ValueError(f"poem is {len(POEM)} characters, must be 1-280")
    if not POEM.strip():
        raise ValueError("poem must not be only white space")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
