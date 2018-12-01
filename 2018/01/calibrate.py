#!/usr/bin/env python

def calibrate(in_file, curr_freq=0):
    with open(in_file, 'r') as fin:
        for line in fin:
            freq_change = int(line)
            curr_freq += freq_change
    return curr_freq

def main():
    result = calibrate("input")
    print('Resulting Frequency = ', result)

if __name__ == '__main__':
    main()

