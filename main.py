"""One-star review of Monday, written as if Monday were a restaurant.

Writes a single original one-line review to /output/entry.txt.
Deterministic: no clock, no randomness, no network, no model calls.

The line is a diner's complaint: Monday seats the reviewer by the
kitchen (the table), serves cold coffee (the dish gone wrong), and
The line is 101 characters, 19 words, one line, inside the 1-180 gate
and the 25-word cap (verified locally, deterministic across runs).
"""

from pathlib import Path

SETUP = "One star."
TABLE = "Monday seated me by the kitchen,"
DISH = "served cold coffee,"
BILL = "and charged me for the weekend it ate."


def build_review() -> str:
    """Assemble the single review line from its parts.

    Setup frames it as an actual one-star review; the table, the dish
    and the bill are concrete restaurant details rather than generic
    tiredness; the punch lands on the last few words, so the turn
    arrives fast and the line is one a reader would retype into the
    group chat without trimming a word.
    """
    return f"{SETUP} {TABLE} {DISH} {BILL}"


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = (output_dir / "entry.txt").resolve()
    # Refuse to write outside the intended output directory.
    if output_path.parent != output_dir.resolve():
        raise ValueError("unsafe output path")
    line = build_review()
    if not 1 <= len(line) <= 180:
        raise ValueError(f"review line is {len(line)} characters, must be 1-180")
    if len(line.split()) > 25:
        raise ValueError(f"review line is {len(line.split())} words, must be at most 25")
    if "\n" in line or "\r" in line:
        raise ValueError("review line must be a single line")
    # Write exactly the review line: no trailing newline, so the file
    # holds one line of 1-180 characters and nothing else.
    output_path.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
