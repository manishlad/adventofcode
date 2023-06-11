import sys


def get_calorie_list(calorie_list_file):
    with open(calorie_list_file, 'r') as calorie_list:
        calories = calorie_list.read()
        calories_carried = [x.split('\n')
                            for x in calories.strip().split('\n\n')]
        calories_carried = [list(map(int, i)) for i in calories_carried]
    return calories_carried


def main(calorie_list_file):
    print("Advent of Code - Day 01")
    calories_carried = get_calorie_list(calorie_list_file)
    highest = max(list(map(sum, calories_carried)))
    print("Part 1:", highest)


if __name__ == '__main__':
    # sys.exit(main("test_input.dat"))
    sys.exit(main("puzzle_input.dat"))
