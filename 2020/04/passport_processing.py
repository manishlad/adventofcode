#!/usr/bin/env python3

import re


p_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


def in_range(value, minimum, maximum):
    if minimum <= value <= maximum:
        return True
    return False


def validate_byr(value):
    return in_range(int(value), 1920, 2002)


def validate_iyr(value):
    return in_range(int(value), 2010, 2020)


def validate_eyr(value):
    return in_range(int(value), 2020, 2030)


def validate_hgt(value):
    if value[-2:] == 'cm':
        return in_range(int(value[:-2]), 150, 193)
    elif value[-2:] == 'in':
        return in_range(int(value[:-2]), 59, 76)
    return False


def validate_hcl(value):
    if re.fullmatch("#[0-9a-z]{6}", value):
        return True


def validate_ecl(value):
    return value in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def validate_pid(value):
    return len(value) == 9 and value.isdigit()


def validate_fields(passport):
    if (
        validate_byr(passport['byr']) and
        validate_iyr(passport['iyr']) and
        validate_eyr(passport['eyr']) and
        validate_hgt(passport['hgt']) and
        validate_hcl(passport['hcl']) and
        validate_ecl(passport['ecl']) and
        validate_pid(passport['pid'])
    ):
        return True
    return False


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
    valid_passports = validate(passports)
    print('There are', len(valid_passports), 'supposedly valid passports')

    valid_passports = [item
                       for item in valid_passports if validate_fields(item)]
    print('There are', len(valid_passports), 'actually valid passports')


if __name__ == '__main__':
    input_file = 'input.dat'
    main(input_file)
