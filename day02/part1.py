from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")

# A | X: Rock
# B | Y: Paper
# C | Z: Scissors

# Rock > Scissors
# Scissors > Paper
# Paper > Rock

# Win
# A Y
# C X
# B Z

# Lose
# B X
# C Y
# A Z

# Draw
# A X
# B Y
# C Z

# Rock: 1
# Paper: 2
# Scissors: 3

# Lose: 0
# Draw: 3
# Win: 6


def compute(s: str) -> int:
    lines = s.splitlines()
    outcome_score = {
        "A Y": 6,
        "C X": 6,
        "B Z": 6,
        "B X": 0,
        "C Y": 0,
        "A Z": 0,
        "A X": 3,
        "B Y": 3,
        "C Z": 3,
    }
    shape_score = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    total_score = 0
    for line in lines:
        round_score = outcome_score[line] + shape_score[line.split()[-1]]
        total_score += round_score

    return total_score


INPUT_S = """\
A Y
B X
C Z
"""
EXPECTED = 15


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", nargs="?", default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
