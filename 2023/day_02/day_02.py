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
    game_powers = []
    with open(input_file, 'r') as games:
        for game in games:
            gID, subsets = game.split(':')
            gameID = int(re.search(r'\d+$', gID).group())
            reds = re.findall(r'\d+ red', subsets)
            max_red = max(
                [int(re.search(r'\d+', x).group()) for x in reds])
            greens = re.findall(r'\d+ green', subsets)
            max_green = max(
                [int(re.search(r'\d+', x).group()) for x in greens])
            blues = re.findall(r'\d+ blue', subsets)
            max_blue = max(
                [int(re.search(r'\d+', x).group()) for x in blues])
            game_powers.append(max_red * max_green * max_blue)
            if (max_red <= MAX_CUBES['red']
                    and max_green <= MAX_CUBES['green']
                    and max_blue <= MAX_CUBES['blue']):
                possible_games.append(gameID)
    print("Sum of IDs of possible games:", sum(possible_games))
    print("Sum of IDs of power of game sets:", sum(game_powers))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(usage())
    sys.exit(main(sys.argv[1]))
