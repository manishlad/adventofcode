#!/usr/bin/env python3


def main(input_file):
    groups = []
    answers = ''
    with open(input_file, 'r') as f:
        for line in f:
            if line.strip():
                answers = answers + line.strip()
            else:
                groups.append(set(answers))
                answers = ''
        groups.append(set(answers))  # remember to add the last entry
    num_yes_per_group = [len(y) for y in groups]
    print(num_yes_per_group)
    print('Sum of yes counts =', sum(num_yes_per_group))


if __name__ == '__main__':
    input_file = 'input.dat'
    main(input_file)
