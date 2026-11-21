#!/usr/bin/env python3
"""Entry program for the-joke-the-reviewer-laughs-at-20261121-0329.

Writes one one-line joke about working beside an AI coding agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt if unset), UTF-8,
deterministically: both runs write identical bytes.
"""
import os

JOKE = ("My coding agent reviewed its own pull request, approved it "
        "instantly, and left a comment calling the author a genius.")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print("wrote", path, len(JOKE), "characters")


if __name__ == "__main__":
    main()
