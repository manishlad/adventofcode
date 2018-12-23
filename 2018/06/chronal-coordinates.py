#!/usr/bin/env python

from scipy.spatial import distance

def get_coord_list(coords_file):
    coords_list = []
    with open(coords_file, 'r') as cf:
        for coord in cf:
            x, y = coord.split(',')
            coords_list.append((int(x), int(y)))
    return coords_list

def get_grid_range(coords):
    minx = maxx = miny = maxy = 0
    for c in coords:
        minx = min(minx, c[0])
        maxx = max(maxx, c[1])
        miny = min(miny, c[0])
        maxy = max(maxy, c[1])
    return minx, maxx, miny, maxy

def largest_area(coords):
    largest = 0
    minx, maxx, miny, maxy = get_grid_range(coords)
    out = distance.cdist(coords, (coords[i], coords[j]), metric='cityblock')
    #for c in coords:
    #    for i in range(minx, maxx):
    #        for j in range(miny, maxy):
    #            largest = max(largest, distance.cdist(c, (coords[i], coords[j]), metric='cityblock'))
    return largest

def main(coords_file):
    coords = get_coord_list(coords_file)
    largest = largest_area(coords)
    print(largest)

if __name__ == '__main__':
    coords_file = 'input.dat'
    main(coords_file)
