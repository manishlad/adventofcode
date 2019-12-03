#!/usr/bin/env python

import sys

def read_prog(input_file):
    with open(input_file, 'r') as f:
        intcode = f.read().split(",")
        intcode = list(map(int, intcode))
    return intcode

def run_prog(intcode):
    mem = intcode.copy()
    i_ptr = 0
    i_incr = 4
    while(i_ptr < len(mem)-i_incr):
        opcode = mem[i_ptr]
        param1 = mem[i_ptr + 1]
        param2 = mem[i_ptr + 2]
        param3 = mem[i_ptr + 3]
        if opcode == 99:
            break
        elif opcode == 1:
            mem[param3] = mem[param1] + mem[param2]
        elif opcode == 2:
            mem[param3] = mem[param1] * mem[param2]
        else:
            print("ERROR: Unknown Opcode at address:", i_ptr)
            sys.exit(1)
        i_ptr += i_incr
    return mem


def part_one(ga_prog):
    ga_prog[1] = 12
    ga_prog[2] = 2
    output = run_prog(ga_prog)
    print(output[0])

def part_two(ga_prog):
    for i in range(100):
        for j in range(100):
            gp = ga_prog.copy()
            gp[1] = i
            gp[2] = j
            output = run_prog(gp)
            if output[0] == 19690720:
                print("Noun:", i, "Verb:", j)
                print("100 * Noun + Verb =", 100 * i + j)
                return



def main(input_file):
    ga_prog = read_prog(input_file)
    part_one(ga_prog)
    part_two(ga_prog)


if __name__ == '__main__':
    input_file = "input.dat"
    main(input_file)
