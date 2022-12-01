[Advent of code 2022](https://adventofcode.com/2022)
===================

*forked from: https://github.com/anthonywritescode/aoc2022*

## Initial Setup
1. Fork and `git clone`
2. Login to advent of code and [get your session cookie](https://youtu.be/CZZLCeRya74?t=197)
3. Create `.env` file and put `session=COOKIE` inside
4. `virtualenv venv`
5. `source .activate.sh`
6. `pip install -r requirements.txt`

## Usage (each day from root)
1. `cp day00 dayNN`
2. `source .activate.sh`
3. `cd dayNN`
4. `aoc-download-input`
5. work on `part1.py`
6. `pt part1.py` (pytest watch with ipdb)

