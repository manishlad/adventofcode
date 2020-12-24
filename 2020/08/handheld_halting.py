#!/usr/bin/env python3


def breakpoint(instruction, visited):
    if instruction in visited:
        return True
    return False


def run_prog(instructions, start=0):
    accumulator = 0
    ip = start
    visited = []
    while ip is not None:
        if breakpoint(ip, visited):
            break
        visited.append(ip)
        op, arg = instructions[ip]
        if op == 'acc':
            accumulator = accumulator + arg
            ip = ip + 1
        elif op == 'jmp':
            ip = ip + arg
        elif op == 'nop':
            ip = ip + 1
        else:
            exit(1)
    return accumulator


def main(input_file):
    with open(input_file, 'r') as f:
        instructions = [(op, int(arg))
                        for op, arg in (i.strip().split()
                                        for i in f)]

    accumulator = run_prog(instructions)
    print('Latest accumulator value:', accumulator)


if __name__ == '__main__':
    input_file = 'input.dat'
    main(input_file)
