#!/usr/bin/env python

def has_duplicate_chars(box_id, occurrences):
    dups = [c for c in box_id if box_id.count(c) == occurrences]
    if dups:
        return True
    return False

def calculate_checksum(in_file):
    doubles = triples = 0
    with open(in_file, 'r') as file:
        for line in file:
            if has_duplicate_chars(line, 2):
                doubles += 1
            if has_duplicate_chars(line, 3):
                triples += 1
    checksum = doubles * triples
    return checksum

def main(box_id_list):
    checksum = calculate_checksum(box_id_list)
    print("Checksum = ", checksum)

if __name__ == '__main__':
    input_file = "input.txt"
    main(input_file)

