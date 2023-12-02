#!/usr/bin/env python
import re
import sys


MAX_CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def usage():
    print("Usage: python day_02.py <input.dat>")


def main(input_file):
    possible_games = []
    with open(input_file, 'r') as games:
        for game in games:
            gID, subsets = game.split(':')
            gameID = int(re.search(r'\d+$', gID).group())
            reds = re.findall(r'\d+ red', subsets)
            max_red = max(
                [int(re.search(r'\d+', x).group()) for x in reds])
            blues = re.findall(r'\d+ blue', subsets)
            max_blue = max(
                [int(re.search(r'\d+', x).group()) for x in blues])
            greens = re.findall(r'\d+ green', subsets)
            max_green = max(
                [int(re.search(r'\d+', x).group()) for x in greens])
            if (max_red <= MAX_CUBES['red']
                    and max_blue <= MAX_CUBES['blue']
                    and max_green <= MAX_CUBES['green']):
                possible_games.append(gameID)
    print("Sum of IDs of possible games:", sum(possible_games))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(usage())
    sys.exit(main(sys.argv[1]))
