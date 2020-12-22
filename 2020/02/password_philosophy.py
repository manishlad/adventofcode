#!/usr/bin/env python3

import re


def validate(password, policy):
    minimum, maximum, char = re.split(' |-', policy)
    if int(minimum) <= password.count(char) <= int(maximum):
        return True
    return False

def validate2(password, policy):
    p1, p2, char = re.split(' |-', policy)
    positions = password[int(p1)-1] + password[int(p2)-1]
    if positions.count(char) == 1:
        return True
    return False


def main(passwords_file):
    valid_passwords = []
    valid_passwords2 = []
    with open(passwords_file, 'r') as passwords:
        for p in passwords:
            pol, pwd = p.strip().split(': ')
            if validate(pwd, pol):
                valid_passwords.append(p)
            if validate2(pwd, pol):
                valid_passwords2.append(p)
    print(len(valid_passwords), 'valid passwords found')
    print(len(valid_passwords2), 'valid passwords found')


if __name__ == '__main__':
    input_file = 'input.dat'
    main(input_file)

