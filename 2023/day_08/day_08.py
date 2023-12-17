#!/usr/bin/env python
import functools
from math import lcm
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

        a_nodes = list(
            filter(lambda x: x[-1] == "A", mappings_dict.keys())
        )

        # First sttempt with iteration
        # rl_pos = 0
        # steps = 0
        # steps = follow_map(mappings_dict, rl, rl_pos, a_nodes)

        # Second attempt with generator
        # *_, steps = follow_map2(mappings_dict, rl)

        # Third attempt with actual mathematics
        atoz_lengths = [follow_map3(mappings_dict, p, rl) for p in a_nodes]
        steps = functools.reduce(lcm, atoz_lengths)
        print("Part 2 - steps =", steps)


# Third attempt - Ah yes, this is a maths problem... d'oh!
def follow_map3(mappings_dict, node, rl):
    current_node = node
    rl_pos = 0
    steps = 0
    while current_node[-1] != 'Z':
        current_node = mappings_dict[current_node].split(", ")[
            RL[rl[rl_pos % len(rl)]]
        ]
        rl_pos += 1
        steps += 1
    return steps


# Second attempt - Iterating over a generator isn't going to work
def follow_map2(mappings_dict, rl):
    current_nodes = list(
        filter(lambda x: x[-1] == "A", mappings_dict.keys())
    )
    rl_pos = 0
    steps = 1
    while not len(
        list(filter(lambda x: x[-1] == "Z", current_nodes))
    ) == len(current_nodes):
        yield steps
        current_nodes = list(
            map(
                lambda x: mappings_dict[x].split(", ")[
                    RL[rl[rl_pos % len(rl)]]
                ],
                current_nodes,
            )
        )
        rl_pos += 1
        steps += 1


# First attempt - recursion isn't going to work
def follow_map(mappings_dict, rl, rl_pos, current_nodes=[]):
    all_Z = len(
        list(filter(lambda x: x[-1] == "Z", current_nodes))
    ) == len(current_nodes)
    if all_Z:
        return 0
    next_nodes = list(
        map(
            lambda x: mappings_dict[x].split(", ")[
                RL[rl[rl_pos % len(rl)]]
            ],
            current_nodes,
        )
    )
    return 1 + follow_map(mappings_dict, rl, rl_pos + 1, next_nodes)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(usage())
    sys.exit(main(sys.argv[1]))
