#!/usr/bin/env python

def incrementing(n):
    nl = list(map(int, list(str(n))))
    for i in range(len(nl)-1):
        if nl[i] > nl[i+1]:
            return False
    return True

def adjacent(n):
    nl = list(map(int, list(str(n))))
    for i in range(len(nl)-1):
        if nl[i] == nl[i+1]:
            return True
    return False

def main(input_range):
    p_list = []
    for i in range(input_range[0], input_range[1]):
        if incrementing(i) and adjacent(i):
            p_list.append(i)
    print(len(p_list))

def test():
    #n = [111111, 122345, 223450, 123789]
    assert (incrementing(111111) and adjacent(111111)) == True
    assert (incrementing(122345) and adjacent(122345)) == True
    assert (incrementing(223450) and adjacent(223450)) == False
    assert (incrementing(123789) and adjacent(123789)) == False

if __name__ == '__main__':
    input_range = (153517,630395)
    main(input_range)
    test()

