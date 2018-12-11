#!/usr/bin/env python

def get_polymer_unit(input_polymer):
    with open(input_polymer, 'r') as p:
        while True:
            unit = p.read(1)
            if unit:
                yield unit
            else:
                return

def main(input_polymer):
    polymer = get_polymer_unit(input_polymer)
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
    print('Reduced polymer length: ', len(rp))

if __name__ == '__main__':
    main("input_test.dat")
    input_polymer = 'input.dat'
    main(input_polymer)
