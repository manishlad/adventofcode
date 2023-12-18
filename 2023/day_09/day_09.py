#!/usr/bin/env python
import operator
import sys


def usage():
    print("Usage: python day_03.py <input.dat>")


def get_differences(seq):
    diffs = list(map(operator.sub, seq[1:], seq[:-1]))
    return diffs


def predict(seq, forward):
    seq_set = set(seq)
    if len(seq_set) == 1 and 0 in seq_set:
        seq.append(0)
    else:
        diffs = get_differences(seq)
        if forward:
            seq.append(seq[-1] + predict(diffs, forward)[-1])
        else:
            seq.insert(0, seq[0] - predict(diffs, forward)[0])
    return seq


def main(input_file):
    with open(input_file, 'r') as f:
        sequences = [s.strip('\n').split() for s in f.readlines()]
    sequences = [list(map(int, s)) for s in sequences]
    sequences = [predict(seq, True) for seq in sequences]
    predictions = [s[-1] for s in sequences]
    print("Sum of forward predictions:", sum(predictions))
    sequences = [predict(seq, False) for seq in sequences]
    predictions = [s[0] for s in sequences]
    print("Sum of reverse predictions:", sum(predictions))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(usage())
    sys.exit(main(sys.argv[1]))
