from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


MATCH_LEN = 14


def is_valid(buffer):
    if len(buffer) == len(set(buffer)) == MATCH_LEN:
        return True
    return False


def update_buffer(buffer):
    """Discard the first item in a buffer in preparation for a later append"""
    if len(buffer) < MATCH_LEN:
        return buffer
    _ = buffer.pop(0)
    return buffer


def compute(s: str) -> int:
    s = s.splitlines()[0]

    buffer = []
    for i, character in enumerate(s):
        buffer.append(character)
        if is_valid(buffer):
            return i + 1
        buffer = update_buffer(buffer)

    return s


INPUT_S = """\
nppdvjthqldpwncqszvftbrmjlhg
"""
EXPECTED = 23


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
