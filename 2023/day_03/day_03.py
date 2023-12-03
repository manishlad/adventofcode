#!/usr/bin/env python
from functools import reduce
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


def check_asterisk(schematic, grid_ref):
    if schematic[grid_ref[0]][grid_ref[1]] == '*':
        return True
    return False


# Used this function for part 1
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


# Used this function for part 2
def check_symbols2(schematic, row, span, part_number, gears):
    scan_range = list(span)
    row_len = len(schematic[row])
    grid_refs = []
    if scan_range[0] > 0:
        scan_range[0] = scan_range[0] - 1
        grid_refs.append((row, scan_range[0]))
    if scan_range[1] < row_len - 1:
        scan_range[1] = scan_range[1] + 1
        grid_refs.append((row, scan_range[1] - 1))
    for i in range(scan_range[0], scan_range[1]):
        if row > 0:
            grid_refs.append((row - 1, i))
        if row < len(schematic) - 1:
            grid_refs.append((row + 1, i))
    for g in grid_refs:
        if match_symbol(schematic, g):
            if check_asterisk(schematic, g):
                gears.setdefault(g, []).append(part_number)
            return True
    return False


def main(input_file):
    valid_parts = []
    gears = {}
    with open(input_file, 'r') as f:
        schematic = [line.strip() for line in f]
        schematic_parts = extract_part_numbers(schematic)
        for line in range(0, len(schematic_parts)):
            for part in schematic_parts[line]:
                valid_part_number = check_symbols2(
                    schematic, line, part[1], part[0], gears)
                if valid_part_number:
                    valid_parts.append(part[0])
    print('Sum of valid part numbers =', sum(valid_parts))
    gear_ratios = []
    for k in gears.keys():
        if len(gears[k]) > 1:
            gear_ratios.append(reduce(lambda x, y: x*y, gears[k]))
    print('Sum of all gear ratios =', sum(gear_ratios))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(usage())
    sys.exit(main(sys.argv[1]))
