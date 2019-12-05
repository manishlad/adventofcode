#!/usr/bin/env python

import re

directions = {
    "U": (0,1),
    "R": (1,0),
    "D": (0,-1),
    "L": (-1,0)
}

def read_wire_path(input_file):
    with open(input_file, 'r') as f:
        wire1 = f.readline().split()[0].split(",")
        wire2 = f.readline().split()[0].split(",")
    return wire1, wire2

def read_path_segment(path_segment):
    m = re.match(r"([URDL])([0-999]*)", path_segment)
    return m.groups()

def get_adjacent_coord(direction, prev_coord):
    c = (prev_coord[0]+directions[direction][0],
         prev_coord[1]+directions[direction][1])
    return c

def trace_wire_path(wire):
    c_ptr = (0,0)
    coords = []
    for segment in wire:
        path_segment = read_path_segment(segment)
        for i in range(int(path_segment[1])):
            adjacent = get_adjacent_coord(path_segment[0], c_ptr)
            coords.append(adjacent)
            c_ptr = adjacent
    return coords

def get_manhattan_distance(crossings):
    centre = (0,0)
    d = {(abs(centre[0] - c[0]) + abs(centre[1] - c[1])):c for c in crossings}
    k = list(d.keys())
    k.sort()
    return k[0]

def test1():
    path1 = trace_wire_path(["R75","D30","R83","U83","L12","D49","R71","U7","L72"])
    path2 = trace_wire_path(["U62","R66","U55","R34","D71","R55","D58","R83"])
    #crossings = list(set(path1) & set(path2))
    crossings = list(set(path1).intersection(path2))
    md = get_manhattan_distances(crossings)
    print(md)

def test2():
    path1 = trace_wire_path(["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"])
    path2 = trace_wire_path(["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"])
    crossings = list(set(path1).intersection(set(path2)))
    md = get_manhattan_distances(crossings)
    print(md)

def main(input_file):
    wire1, wire2 = read_wire_path(input_file)
    path1 = trace_wire_path(wire1)
    path2 = trace_wire_path(wire2)
    crossings = list(set(path1).intersection(set(path2)))
    md = get_manhattan_distance(crossings)
    print(md)

if __name__ == '__main__':
    input_file = "input.dat"
    main(input_file)
    #test1()
    #test2()
