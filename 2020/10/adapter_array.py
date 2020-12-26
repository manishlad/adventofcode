#!/usr/bin/env python3


def main(input_file):
    prev = 0
    distrib = []
    with open(input_file, 'r') as f:
        joltages = [int(j.strip()) for j in f]
        joltages.sort()
    for j in range(0, len(joltages)):
        jolt = joltages[j]
        diff = jolt - prev
        if diff in range(1, 4):
            distrib.append(diff)
            prev = jolt
        else:
            print('ERROR: diff, prev, jolt =', diff, prev, jolt)
            exit(1)
    distrib.append(3)  # highest adapter to device diff
    one_diffs = distrib.count(1)
    three_diffs = distrib.count(3)
    print('Distribution =', one_diffs*three_diffs)


if __name__ == '__main__':
    input_file = 'input.dat'
    main(input_file)
