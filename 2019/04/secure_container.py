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

def adjacent2(n):
    nl = list(map(int, list(str(n))))
    nd = {i:1 for i in nl}
    for i in range(len(nl)-1):
        if nl[i] == nl[i+1]:
            nd[nl[i]] = nd[nl[i]] + 1
    return 2 in nd.values()

def main(input_range):
    p1_list = []
    p2_list = []
    for i in range(input_range[0], input_range[1]):
        if incrementing(i) and adjacent(i):
            p1_list.append(i)
        if incrementing(i) and adjacent2(i):
            p2_list.append(i)
    print(len(p1_list), len(p2_list))

def test():
    assert (incrementing(111111) and adjacent(111111)) == True
    assert (incrementing(122345) and adjacent(122345)) == True
    assert (incrementing(223450) and adjacent(223450)) == False
    assert (incrementing(123789) and adjacent(123789)) == False

    assert (incrementing(112233) and adjacent2(112233)) == True
    assert (incrementing(123444) and adjacent2(123444)) == False
    assert (incrementing(111122) and adjacent2(111122)) == True

if __name__ == '__main__':
    input_range = (153517,630395)
    main(input_range)
    test()

