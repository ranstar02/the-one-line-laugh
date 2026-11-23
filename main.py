"""The One-Line Laugh — make.fun bounty u-ronigrv-the-one-line-laugh-7ccca46f.

Writes one original funny line (a single sentence, at most 200
characters) to /output/entry.txt. Fully deterministic: one fixed joke,
no randomness, no clock, no network, no environment reads.
Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
"""

import os

JOKE = "My smartwatch says I burned 400 calories today \u2014 mostly from running late."


def main() -> None:
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert JOKE.count(".") == 1 and JOKE.endswith("."), "joke must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
