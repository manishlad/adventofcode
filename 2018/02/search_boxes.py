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

def get_common_chars(in_file):
    checksum_list = open(in_file, 'r').readlines()
    checksum_length = len(checksum_list[0])
    checksum_pairs = [(checksum_list[i], checksum_list[j])
                      for i in range(len(checksum_list))
                      for j in range(i+1, len(checksum_list))
                      if i != j]
    for pair in checksum_pairs:
        match_chars = [i for i, j in zip(pair[0], pair[1]) if i == j]
        if len(match_chars) == checksum_length - 1:
            return ''.join(match_chars)


def main(box_id_list):
    checksum = calculate_checksum(box_id_list)
    print("Checksum = ", checksum)

    common_chars = get_common_chars(box_id_list)
    print("Common characters are ", common_chars)

if __name__ == '__main__':
    input_file = "input.txt"
    main(input_file)

