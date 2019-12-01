#!/usr/bin/env python

def calculate_fuel_req(mass):
    return ((mass // 3) - 2)

def main(module_masses_file):
    with open(module_masses_file, 'r') as module_masses:
        fuel_reqs = [ calculate_fuel_req(int(mass)) for mass in module_masses ]
    total_fuel_req = sum(fuel_reqs)
    print("Total fuel required is:", total_fuel_req)


if __name__ == '__main__':
    input_file = "input.dat"
    main(input_file)
