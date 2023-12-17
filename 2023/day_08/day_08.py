#!/usr/bin/env python
import sys


RL = {"L": 0, "R": 1}


def usage():
    print("Usage: python day_03.py <input.dat>")


def main(input_file):
    with open(input_file, "r") as f:
        rl, nodes = "".join(f.readlines()).split("\n\n")
        mappings = nodes.strip().split("\n")
        mappings_dict = dict([m.strip(")").split(" = (") for m in mappings])
        current_node = "AAA"
        rl_pos = 0
        steps = 0
        while current_node != "ZZZ":
            current_node = mappings_dict[current_node].split(", ")[
                RL[rl[rl_pos % len(rl)]]
            ]
            rl_pos += 1
            steps += 1
        print("Part 1 - steps =", steps)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(usage())
    sys.exit(main(sys.argv[1]))
