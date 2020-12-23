#!/usr/bin/env python3


def main(input_file):
    groups = []
    groups2 = []
    answers = []
    with open(input_file, 'r') as f:
        for line in f:
            if line.strip():
                answers.append(set(line.strip()))
            else:
                groups.append(set.union(*answers))
                groups2.append(set.intersection(*answers))
                answers = []
        groups.append(set.union(*answers))  # remember to add the last entries
        groups2.append(set.intersection(*answers))
    num_yes_per_group = [len(y) for y in groups]
    num_yes_per_group2 = [len(y) for y in groups2]
    print('Sum of union yes counts =', sum(num_yes_per_group))
    print('Sum of intersection yes counts =', sum(num_yes_per_group2))


if __name__ == '__main__':
    input_file = 'input.dat'
    main(input_file)
