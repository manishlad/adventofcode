#!/usr/bin/env python3

from itertools import combinations


def xmas(input_file):
    count = 0
    with open(input_file, 'r') as f:
        for line in f:
            yield count, int(line.strip())
            count = count+1


def check(n, prev25):
    for pair in combinations(prev25, 2):
        if sum(pair) == n:
            return True
    return False


def find_invalid(xmas_code):
    prev = []
    invalid = None
    for item in xmas_code:
        c, n = item
        if c >= 25:
            valid = check(n, prev[-25:])
            if not valid:
                invalid = n
                return prev, c, invalid
        prev.append(n)
    return prev, c, None


def contig_combos(src_list):
    for i in range(0, len(src_list)):
        for j in range(i+2, len(src_list)):
            yield src_list[i:j]


def main(input_file):
    xmas_code = xmas(input_file)
    prev, position, invalid = find_invalid(xmas_code)
    if invalid is not None:
        print('Invalid entry at', position+1, ':', invalid)

        for combo in contig_combos(prev):
            if sum(combo) == invalid:
                print('Encryption weakness =', min(combo) + max(combo),
                      'because of:', min(combo), max(combo), combo)


if __name__ == '__main__':
    input_file = 'input.dat'
    main(input_file)
