from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")

# A | X: Rock
# B | Y: Paper
# C | Z: Scissors

# X: Lose
# Y: Draw
# Z: Win
def calc_resp(instruction):

    draws = dict(A="X", B="Y", C="Z")
    wins = dict(A="Y", B="Z", C="X")
    loses = dict(A="Z", B="X", C="Y")
    responses = dict(X=loses, Y=draws, Z=wins)

    them, outcome = instruction.split()
    return responses[outcome][them]


def compute(s: str) -> int:
    lines = s.splitlines()
    outcome_score = {
        "X": 0,
        "Y": 3,
        "Z": 6,
    }
    shape_score = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    total_score = 0
    for line in lines:
        resp = calc_resp(line)
        round_score = shape_score[resp] + outcome_score[line.split()[-1]]
        total_score += round_score

    return total_score


INPUT_S = """\
A Y
B X
C Z
"""
EXPECTED = 12


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
