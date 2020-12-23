#!/usr/bin/env python3

rows = [i for i in range(128)]
cols = [i for i in range(8)]


def find_row(seat):
    r = rows
    for char in seat:
        if char == 'F':
            r = r[:len(r)//2]
        elif char == 'B':
            r = r[len(r)//2:]
    return r


def find_col(seat):
    c = cols
    for char in seat:
        if char == 'L':
            c = c[:len(c)//2]
        elif char == 'R':
            c = c[len(c)//2:]
    return c


def main(input_file):
    seat_list = []
    with open(input_file, 'r') as seats:
        for seat in seats:
            row = find_row(seat[:7])
            col = find_col(seat[7:])
            seat_list.append(row[0]*8 + col[0])
    print('Sanity check - highest seat ID =', max(seat_list))

if __name__ == '__main__':
    input_file = 'input.dat'
    main(input_file)
