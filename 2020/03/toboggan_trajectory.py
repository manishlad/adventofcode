#!/usr/bin/env python3

def main(map_file):
    position = 0
    path = []
    with open(map_file, 'r') as treemap:
        for line in treemap:
            path.append(line.strip()[position % len(line.strip())])
            print(line.strip()[position % len(line.strip())])
            position = position + 3
    num_trees = path.count('#')
    print('There are', num_trees, 'along the path')


if __name__ == '__main__':
    map_file = 'input.dat'
    main(map_file)
