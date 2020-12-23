#!/usr/bin/env python3

p_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


def validate(passports):
    valid_passports = []
    for p in passports:
        fields = set(p.keys())
        fields.discard('cid')
        if fields == p_keys:
            valid_passports.append(p)
    return valid_passports


def main(input_file):
    passports = []
    d = {}
    with open(input_file, 'r') as f:
        for line in f:
            if line.strip():
                for kv in line.strip().split(' '):
                    d[kv.split(':')[0]] = kv.split(':')[1]
            else:
                passports.append(d)
                d = {}
        passports.append(d)  # remember to add the last entry
    print(len(passports))
    valid_passports = validate(passports)
    print('There are', len(valid_passports), 'valid passports')


if __name__ == '__main__':
    input_file = 'input.dat'
    main(input_file)
