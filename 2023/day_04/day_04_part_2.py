#!/usr/bin/env python
import re
# import string
import sys


def usage():
    print("Usage: python day_03.py <input.dat>")


def main(input_file):
    with open(input_file, 'r') as f:
        cards = [line.strip().split(':') for line in f]
        carddict = dict(cards)
        for card in cards:
            numbers = card[1].split('|')
            winners = numbers[0].split()
            numbers_you_have = numbers[1].split()
            intersection = list(set(winners) & set(numbers_you_have))
            if intersection:
                card_id = int(re.search(r'\d+$', card[0]).group())
                for i in range(1, len(intersection) + 1):
                    card_id_str = str(card_id + i)
                    key = 'Card ' + f"{card_id_str:>3}"
                    cards.append([key, carddict[key]])
    print('Total cards =', len(cards))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(usage())
    sys.exit(main(sys.argv[1]))
