#!/usr/bin/env python

import numpy
import re

def get_slice(in_file):
    with open(in_file, 'r') as fin:
        for line in fin:
            yield re.match("#(.*) @ (.*),(.*): (.*)x(.*)", line).groups()

def allocate_claims(claims_list, fabric):
    for claim in get_slice(claims_list):
        for i in range(int(claim[1]), int(claim[1])+int(claim[3])):
            for j in range(int(claim[2]), int(claim[2])+int(claim[4])):
                fabric[i][j] += 1
    return fabric

def find_overlaps(marked_fabric):
    counter = 0
    for i in range(0, 1000):
        for j in range(0, 1000):
            if marked_fabric[i][j] > 1:
                counter += 1
    return counter

def main(claims_list):
    fabric = numpy.zeros((1000,1000))
    marked_fabric = allocate_claims(claims_list, fabric)
    overlapping = find_overlaps(marked_fabric)
    print("Number of overlapping square inches: ", overlapping)

if __name__ == '__main__':
    input_file = "input.txt"
    main(input_file)

