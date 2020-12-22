#!/usr/bin/env python3

from math import prod


slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]


def traverse(map_file, coords):
    position = 0
    down = 1
    path = []
    with open(map_file, 'r') as treemap:
        for line in treemap:
            if down > 1:
                down = down - 1
            else:
                path.append(line.strip()[position % len(line.strip())])
                position = position + coords[0]
                down = coords[1]
    num_trees = path.count('#')
    return num_trees


def main(map_file):
    part1 = traverse(map_file, (3, 1))
    print("There are", part1, "trees in slope 1")
    part2 = prod([traverse(map_file, coords) for coords in slopes])
    print("Product of number of trees encountered on each slope =", part2)

if __name__ == '__main__':
    map_file = 'input.dat'
    main(map_file)
