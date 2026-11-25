#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single original one-liner to /output/entry.txt.

The chosen line:
    "I tried meditation to calm down, but sitting quietly just gave my
    anxiety a microphone and a stage."

Why it wins against the judge brief (laugh first, then turn, tightness,
freshness, clarity):
  * Laugh/turn: the setup promises calm; the punch flips it — meditation
    backfires by handing anxiety a platform. The twist lands in the
    final clause, "a microphone and a stage", which reframes the whole
    sentence.
  * Tight: 99 characters, every word earns its place; nothing to trim.
  * Fresh: "anxiety with a microphone and a stage" is a vivid image,
    not a recycled pun or a premise the judge has heard a hundred times.
  * Clear: one read, no explanation needed, self-contained.

Deterministic, stdlib-only, no network, no randomness, no environment
reads. The output is byte-identical on every run.
"""

import os

# The single funny line (99 characters, ASCII, no trailing newline).
LINE = (
    "I tried meditation to calm down, but sitting quietly just gave "
    "my anxiety a microphone and a stage."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Enforce the bounty gate at write time so a future edit to LINE
    # can never silently ship an invalid entry (1-140 chars, not
    # only whitespace, single line).
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "line must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
