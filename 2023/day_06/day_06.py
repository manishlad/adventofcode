#!/usr/bin/env python
from functools import reduce
import re
import sys


TEST = 0

TEST_INPUT = """
Time:      7  15   30
Distance:  9  40  200
"""

PUZZLE_INPUT = """
Time:        46     82     84     79
Distance:   347   1522   1406   1471
"""


def parse_input(input):
    races = [re.split(r':', td)[1].split() for td in input.strip().split('\n')]
    races = [map(int, value) for value in races]
    return list(zip(races[0], races[1]))


def push_ratios(time):
    ratios = list(zip(range(1, time + 1), reversed(range(0, time))))
    return ratios


def calculate_wins(ratios, record):
    times = [r[0] * r[1] for r in ratios]
    winners = [t for t in times if t > record]
    return winners


def main():
    margins = []
    if TEST:
        races = parse_input(TEST_INPUT)
    else:
        races = parse_input(PUZZLE_INPUT)
    for race in races:
        ratios = push_ratios(race[0])
        win_combos = calculate_wins(ratios, race[1])
        margins.append(len(win_combos))

    margins_product = reduce(lambda x, y: x * y, margins)
    print("Part 1:", margins_product)


if __name__ == "__main__":
    sys.exit(main())
