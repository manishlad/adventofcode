#!/usr/bin/env python3


def breakpoint(instruction, visited):
    if instruction in visited:
        return True
    return False


def fix_instruction(instruction):
    op, arg = instruction
    if op == 'jmp':
        return ('nop', arg)
    elif op == 'nop':
        return ('jmp', arg)
    else:
        return instruction


def run_prog(instructions, start=0):
    accumulator = 0
    ip = start
    visited = []
    while ip < len(instructions):
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
    return accumulator, ip == len(instructions), visited


def main(input_file):
    with open(input_file, 'r') as f:
        instructions = [(op, int(arg))
                        for op, arg in (i.strip().split()
                                        for i in f)]

    accumulator, completed, visited = run_prog(instructions)
    print('Latest accumulator value:', accumulator)

    if not completed:
        for i in range(len(visited)-1, -1, -1):
            f_i = fix_instruction(instructions[visited[i]])
            if f_i != instructions[visited[i]]:
                fixed_instructions = instructions
                fixed_instructions[visited[i]] = f_i
                accumulator, completed, _ = run_prog(fixed_instructions)
                if completed:
                    break
    print('Latest accumulator value:', accumulator)


if __name__ == '__main__':
    input_file = 'input.dat'
    main(input_file)
