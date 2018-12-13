#!/usr/bin/env python

import string

def get_polymer_unit(input_polymer):
    with open(input_polymer, 'r') as p:
        while True:
            unit = p.read(1)
            if unit:
                yield unit
            else:
                return

def collapse_polymer(polymer):
    reduced = []
    for unit in polymer:
        if reduced:
            if unit.islower():
                if reduced[-1] == unit.upper():
                    reduced = reduced[:-1]
                    continue
            elif unit.isupper():
                if reduced[-1] == unit.lower():
                    reduced = reduced[:-1]
                    continue
        reduced.append(unit)
    rp = ''.join(reduced).strip()
    return rp

def shortest_polymer(input_polymer):
    letters = list(zip(string.ascii_uppercase, string.ascii_lowercase))
    shortest_polymer = input_polymer
    for l in letters:
        p = [u for u in input_polymer if u not in l]
        rp = collapse_polymer(p)
        if len(rp) < len(shortest_polymer):
            shortest_polymer = rp
    return shortest_polymer

def main(input_polymer):
    polymer = get_polymer_unit(input_polymer)
    rp = collapse_polymer(polymer)
    print('Reduced polymer length: ', len(rp))

    sp = shortest_polymer(rp)
    print('Shortest polymer length: ', len(sp))


if __name__ == '__main__':
    main("input_test.dat")
    input_polymer = 'input.dat'
    main(input_polymer)
