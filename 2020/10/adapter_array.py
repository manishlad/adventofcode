#!/usr/bin/env python3


def alternatives(joltages, base):
    for j in range(0, len(joltages)):
        jolt = joltages[j]
        new_base = base
        if jolt - base[-1] in range(1,4):
            new_base = base+[jolt]
            yield from alternatives(joltages[j+1:], new_base)
        else:
            yield new_base


def main(input_file):
    prev = 0
    distrib = []
    with open(input_file, 'r') as f:
        joltages = [int(j.strip()) for j in f]
        joltages.sort()
        joltages.append(max(joltages) + 3) # highest adapter to device diff

    for j in range(0, len(joltages)):
        jolt = joltages[j]
        diff = jolt - prev
        if diff in range(1, 4):
            distrib.append(diff)
            prev = jolt
        else:
            print('ERROR: diff, prev, jolt =', diff, prev, jolt)
            exit(1)
    one_diffs = distrib.count(1)
    three_diffs = distrib.count(3)
    print('Distribution =', one_diffs*three_diffs)

    distinct_arrangements = sum(1 for a in alternatives(joltages, [0]))
    print('Distinct ways =', distinct_arrangements)


if __name__ == '__main__':
    input_file = 'input.dat'
    main(input_file)
