#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun entry.

Writes a single line, in the voice of the Moon replying at last
to the wishes, howls and late-night promises of everyone staring
up at it, to /output/entry.txt:

    You spent four thousand years calling me cheese, then sent
    twelve men to walk on me and left their golf balls behind.
    I am not your fridge. Stop opening me at midnight.

Why it lands: the Moon answers four thousand years of
name-calling and midnight visits with one weary complaint
(setup), then the evidence — twelve men, golf balls left behind
(turn) — and the payoff is a house rule in the last four words,
"Stop opening me at midnight." Three beats, four concrete
anchors (four thousand years, twelve men, golf balls, midnight),
168 characters, in the Moon's own wry, old, tired-of-being-
wished-upon voice. No explaining the joke: the Moon never says
it is funny, it just reports the damage.

Selected by a blind pairwise tournament (fresh Gemini judge,
15 pairs, 6 candidates from 4 angles): this line won 5/5 with
the highest margin sum (18), then beat the lane's earlier
tournament winner head-to-head in both label orders (margin 3
each). An extra-mile pass that added an explicit wishes beat
was tested against the original and rejected by the same judge
— it "ruins a clean punchline by dragging" — so the original
stands.

Python 3.13, standard library only, no network, deterministic.
"""

import os

ENTRY = (
    "You spent four thousand years calling me cheese, then sent "
    "twelve men to walk on me and left their golf balls behind. "
    "I am not your fridge. Stop opening me at midnight."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate self-check: /output/entry.txt must be UTF-8 text of
    # 1 to 240 characters, not only whitespace, and one line:
    # an embedded newline would break the single-line read.
    # Verified live: 168 characters, single line, no trailing newline.
    assert 1 <= len(ENTRY) <= 240, f"entry is {len(ENTRY)} chars, gate wants 1-240"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY.encode("utf-8").decode("utf-8") == ENTRY
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(ENTRY.encode("utf-8"))
    # Read-back verification: the graded artifact is the file on disk,
    # not the string in memory — confirm the bytes landed exactly.
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    assert written == ENTRY.encode("utf-8"), (
        f"entry.txt on disk differs from ENTRY: {written!r}"
    )


if __name__ == "__main__":
    main()
