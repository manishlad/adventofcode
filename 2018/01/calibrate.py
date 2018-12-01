#!/usr/bin/env python

def get_freq(in_file):
    while True:
        with open(in_file, 'r') as fin:
            for line in fin:
                yield int(line)

def find_first_repeat(in_file, curr_freq=0):
    freqs = set()
    freqs.add(curr_freq)
    for item in get_freq(in_file):
        curr_freq += item
        if curr_freq in freqs:
            return curr_freq
        else:
            freqs.add(curr_freq)

def calibrate_first_pass(in_file, curr_freq=0):
    with open(in_file, 'r') as fin:
        for line in fin:
            freq_change = int(line)
            curr_freq += freq_change
    return curr_freq

def main():
    result = calibrate_first_pass("input")
    print('Resulting frequency on first pass = ', result)

    first_repeat = find_first_repeat("input")
    print('First repeated frequency = ', first_repeat)

if __name__ == '__main__':
    main()

