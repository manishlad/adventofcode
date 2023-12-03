#!/usr/bin/env python
import re
import string
import sys


SYMBOLS = list(string.punctuation.replace('.', ''))


def usage():
    print("Usage: python day_03.py <input.dat>")


def extract_part_numbers(schematic):
    schematic_parts = []
    for line in schematic:
        iter = re.finditer(r'\d+', line)
        part_numbers = [[int(n.group()), n.span()] for n in iter]
        schematic_parts.append(part_numbers)
    return schematic_parts


def match_symbol(schematic, grid_ref):
    if schematic[grid_ref[0]][grid_ref[1]] in SYMBOLS:
        return True
    return False


def check_symbols(schematic, row, span):
    scan_range = list(span)
    row_len = len(schematic[row])
    if scan_range[0] > 0:
        scan_range[0] = scan_range[0] - 1
        if match_symbol(schematic, (row, scan_range[0])):
            return True
    if scan_range[1] < row_len - 1:
        scan_range[1] = scan_range[1] + 1
        if match_symbol(schematic, (row, scan_range[1] - 1)):
            return True
    for i in range(scan_range[0], scan_range[1]):
        if row > 0 and match_symbol(schematic, (row - 1, i)):
            return True
        if row < len(schematic) - 1 and match_symbol(schematic, (row + 1, i)):
            return True
    return False


def main(input_file):
    valid_parts = []
    with open(input_file, 'r') as f:
        schematic = [line.strip() for line in f]
        schematic_parts = extract_part_numbers(schematic)
        for line in range(0, len(schematic_parts)):
            for part in schematic_parts[line]:
                valid_part_number = check_symbols(schematic, line, part[1])
                if valid_part_number:
                    valid_parts.append(part[0])
    print('Sum of valid part numbers =', sum(valid_parts))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(usage())
    sys.exit(main(sys.argv[1]))
