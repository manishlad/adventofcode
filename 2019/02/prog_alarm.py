#!/usr/bin/env python

import sys

def read_prog(input):
    with open(input, 'r') as f:
        intcode = f.read().split(",")
        intcode = list(map(int, intcode))
    return intcode

def run_prog(intcode):
    ptr = 0
    while(ptr < len(intcode)):
        if intcode[ptr] == 99:
            break
        elif intcode[ptr] == 1:
            intcode[intcode[ptr+3]] = intcode[intcode[ptr+1]] + intcode[intcode[ptr+2]]
        elif intcode[ptr] == 2:
            intcode[intcode[ptr+3]] = intcode[intcode[ptr+1]] * intcode[intcode[ptr+2]]
        else:
            print("ERROR")
            sys.exit(1)
        ptr+=4
    return intcode

def part_one(ga_prog):
    ga_prog[1] = 12
    ga_prog[2] = 2
    output = run_prog(ga_prog)
    print(output)


def main(input):
    ga_prog = read_prog(input)
    part_one(ga_prog)


if __name__ == '__main__':
    input_file = "input.dat"
    main(input_file)
