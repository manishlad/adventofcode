#!/usr/bin/env python
import operator
import sys


def usage():
    print("Usage: python day_03.py <input.dat>")


def get_differences(seq):
    diffs = list(map(operator.sub, seq[1:], seq[:-1]))
    return diffs


def predict(seq):
    seq_set = set(seq)
    if len(seq_set) == 1 and 0 in seq_set:
        seq.append(0)
    else:
        diffs = get_differences(seq)
        seq.append(seq[-1] + predict(diffs)[-1])
    return seq


def main(input_file):
    with open(input_file, 'r') as f:
        sequences = [s.strip('\n').split() for s in f.readlines()]
    sequences = [list(map(int, s)) for s in sequences]
    sequences = [predict(seq) for seq in sequences]
    predictions = [s[-1] for s in sequences]
    print("Sum of predictions:", sum(predictions))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(usage())
    sys.exit(main(sys.argv[1]))
