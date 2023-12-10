#!/usr/bin/env python
# import re
# import string
import sys


myDict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def usage():
    print("Usage: python day_03.py <input.dat>")


def compare(item1, item2):
    pairs = zip(item1, item2)
    print(list(pairs))
    return 1


def main(input_file):
    with open(input_file, "r") as f:
        hands = [line.strip().split(" ") for line in f]
    # hands = [[h[0], int(h[1])] for h in hands]
    print(hands)
    # hands = map(lambda h: {h[0]: int(h[1])}, hands)
    hands = {k: int(v) for k, v in hands}
    print(hands)
    hands_by_type = {}
    for hand in hands.keys():
        strength = len(set(hand))
        hands_by_type.setdefault(strength, []).append({hand: hands[hand]})
    for hbt in hands_by_type.keys():
        hands_by_type[hbt] = {
            k: v for h in hands_by_type[hbt] for k, v in h.items()
        }
    print(hands, "\n\n", hands_by_type)
    # high_card = sorted(hands_by_type[0], key=lambda h: rank_hands(h))
    # print(high_card)
    compare(list(hands_by_type[3].keys())[0], list(hands_by_type[3].keys())[1])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(usage())
    sys.exit(main(sys.argv[1]))
