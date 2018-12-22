#!/usr/bin/env python

from collections import defaultdict
from functools import reduce

TEST_INPUT = defaultdict(list, {
    'c': ['a', 'f'],
    'a': ['b', 'd'],
    'b': ['e'],
    'd': ['e'],
    'f': ['e'],
})


REAL_INPUT = defaultdict(list, {
    'Z': ['V', 'H', 'L', 'E', 'D', 'Y'],
    'V': ['K', 'S', 'P'],
    'M': ['Q', 'B', 'I', 'N', 'D', 'A', 'O', 'G'],
    'E': ['X', 'H', 'W'],
    'J': ['W', 'I', 'R', 'C', 'A', 'N', 'S'],
    'L': ['O', 'W', 'T', 'X'],
    'Q': ['T', 'S', 'G'],
    'Y': ['P', 'X', 'C', 'D'],
    'X': ['R', 'T', 'A', 'F', 'S'],
    'T': ['U', 'H', 'C', 'I', 'R', 'S', 'P'],
    'I': ['O', 'G', 'S', 'P', 'F'],
    'P': ['H', 'N', 'R', 'W'],
    'G': ['A', 'R', 'N', 'S', 'F'],
    'N': ['A', 'R', 'W', 'O', 'K'],
    'H': ['B', 'C', 'F', 'S'],
    'F': ['D', 'A', 'C', 'W'],
    'S': ['O', 'K', 'B'],
    'O': ['W', 'B', 'A', 'D'],
    'D': ['U', 'K', 'R', 'B', 'W'],
    'W': ['B', 'C'],
    'A': ['K', 'U', 'B'],
    'B': ['R', 'C'],
    'K': ['C', 'U'],
    'R': ['C', 'U'],
    'U': ['C'],
})

def parse_instructions(instructions):
    input_list = defaultdict(list)
    with open(instructions, 'r') as rules:
        for rule in rules:
            r = rule.split()
            input_list[r[1]].append(r[7])
    return input_list

def find_start_points(input_list):
    start_points = []
    for i in list(input_list.keys()):
        s = list(map(lambda x: i in x, list(input_list.values())))
        r = reduce((lambda x, y: x or y), s)
        if not r:
            start_points.append(i)
    start_points.sort()
    return start_points

def has_no_deps(node, graph):
    collapsed = reduce(lambda x,y: x+y, list(graph.values()), [])
    if node not in reduce(lambda x,y: x+y, list(graph.values()), []):
        return True
    return False

def traverse_graph(start_points, graph):
    start_point = start_points.pop(0)
    path = [start_point]
    next_points = start_points
    next_points += graph.pop(start_point, [])
    while next_points:
        next_points = list(filter(lambda x: has_no_deps(x, graph), next_points))
        next_points.sort()
        if next_points:
            p = next_points.pop(0)
            path.append(p)
            n = graph.pop(p, [])
            if n:
                next_points += n
        sps = find_start_points(graph)
        if sps:
            next_points = list(set(next_points + sps))
    return path

def main(input_list):
    start_points = find_start_points(input_list)
    if start_points:
        path = traverse_graph(start_points, input_list)
        print('Path = ', ''.join(path))

if __name__ == '__main__':
    instructions = 'input.dat'
    input_list = parse_instructions(instructions)
    main(TEST_INPUT)
    main(input_list)
