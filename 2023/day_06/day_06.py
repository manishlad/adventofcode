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
    races = [re.split(r":", td)[1].split() for td in input.strip().split("\n")]
    races = [map(int, value) for value in races]
    return list(zip(races[0], races[1]))


def parse_input_kerned(input):
    races = [
        re.split(r":", td)[1].replace(" ", "")
        for td in input.strip().split("\n")
    ]
    races = tuple(map(int, races))
    return [races]


def push_ratios(time):
    ratios = zip(range(1, time + 1), reversed(range(0, time)))
    return ratios


def calculate_wins(ratios, record):
    times = [r[0] * r[1] for r in ratios]
    winners = [t for t in times if t > record]
    return winners


def calculate_wins2(ratios, record):
    winners = list(filter(lambda r: r[0] * r[1] > record, ratios))
    return winners
#     for r in ratios:
#         if r[0] * r[1] > record:
#             lower = r[0]
#             break
#     for r in reversed(ratios):
#         if r[0] * r[1] > record:
#             upper = r[0]
#             break
#     return (lower, upper)


def find_margins(races):
    margins = []
    for race in races:
        ratios = push_ratios(race[0])
        win_combos = calculate_wins(ratios, race[1])
        margins.append(len(win_combos))
    return margins


def find_margins2(races):
    for race in races:
        ratios = push_ratios(race[0])
        winners = calculate_wins2(ratios, race[1])
        lower, upper = winners[0]
    return (upper + 1) - lower


def main():
    if TEST:
        races = parse_input(TEST_INPUT)
    else:
        races = parse_input(PUZZLE_INPUT)
    margins = find_margins(races)
    margins_product = reduce(lambda x, y: x * y, margins)
    print("Part 1:", margins_product)

    if TEST:
        races = parse_input_kerned(TEST_INPUT)
    else:
        races = parse_input_kerned(PUZZLE_INPUT)
    margins = find_margins2(races)
    print("Part 2:", margins)

    # The original functions would have worked fine
    # I created the alternative functions because I missed the fact that
    # I was converting the zip object into a list instead of iterating
    # directly over the zip
    if TEST:
        races = parse_input_kerned(TEST_INPUT)
    else:
        races = parse_input_kerned(PUZZLE_INPUT)
    margins = find_margins(races)
    margins_product = reduce(lambda x, y: x * y, margins)
    print("Part 2:", margins_product)


if __name__ == "__main__":
    sys.exit(main())
