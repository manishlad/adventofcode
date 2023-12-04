#!/usr/bin/env python
# import re
# import string
import sys


def usage():
    print("Usage: python day_03.py <input.dat>")


def main(input_file):
    points = 0.0
    with open(input_file, 'r') as cards:
        for card in cards:
            c = card.strip()
            card_id, numbers = c.split(':')
            w, h = numbers.split('|')
            winners = w.split()
            numbers_you_have = h.split()
            intersection = list(set(winners) & set(numbers_you_have))
            if intersection:
                points = points + 2**(len(intersection) - 1)
    print('Total points =', int(points))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(usage())
    sys.exit(main(sys.argv[1]))
