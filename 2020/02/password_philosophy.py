#!/usr/bin/env python3

import re


def validate(password, policy):
    minimum, maximum, char = re.split(' |-', policy)
    if int(minimum) <= password.count(char) <= int(maximum):
        return True
    return False


def main(passwords_file):
    valid_passwords = []
    with open(passwords_file, 'r') as passwords:
        for p in passwords:
            pol, pwd = p.strip().split(': ')
            if validate(pwd, pol):
                valid_passwords.append(p)
    print(len(valid_passwords), 'valid passwords found')


if __name__ == '__main__':
    input_file = 'input.dat'
    main(input_file)

