#!/usr/bin/env python3

from itertools import combinations
from math import prod


def main(expense_report_file):
    with open(expense_report_file, 'r') as expense_report:
        entries = [int(entry) for entry in expense_report]
    for pair in combinations(entries, 2):
        if sum(pair) == 2020:
            print(prod(pair))


if __name__ == '__main__':
    input_file = "input.dat"
    main(input_file)
