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


def main(input_file):
    xmas_code = xmas(input_file)
    prev25 = []
    for item in xmas_code:
        c, n = item
        if c >= 25:
            valid = check(n, prev25)
            if valid:
                prev25 = prev25[1:] + [n]
            else:
                print('Invlid entry at', c+1, ':', n)
                return
        else:
            prev25.append(n)
    print('All valid')


if __name__ == '__main__':
    input_file = 'input.dat'
    main(input_file)
