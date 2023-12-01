import sys

SPELLED_OUT = {
    "twone": '21',
    "oneight": '18',
    "threeight": '38',
    "fiveight": '58',
    "eightwo": '82',
    "eighthree": '83',
    "sevenine": '79',
    "nineight": '98',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
}


def extract_digits(strval):
    return [i for i in strval if i.isdigit()]


def first_last_digit(digits):
    first_last = '0'
    if digits:
        first_last = ''.join([digits[0], digits[-1]])
    return int(first_last)


def parse_digit(strval):
    processed_strval = strval
    for key in list(SPELLED_OUT.keys()):
        processed_strval = processed_strval.replace(key, SPELLED_OUT[key])
    return processed_strval


def part_one(input_file):
    calibration_values = []
    with open(input_file, 'r') as data:
        for line in data:
            digits = extract_digits(line)
            value = first_last_digit(digits)
            calibration_values.append(value)
    return sum(calibration_values)


def part_two(input_file):
    calibration_values = []
    with open(input_file, 'r') as data:
        for line in data:
            parsed_line = parse_digit(line)
            digits = extract_digits(parsed_line)
            value = first_last_digit(digits)
            calibration_values.append(value)
    return sum(calibration_values)


def main(input_file):
    part1 = part_one(input_file)
    print("Part 1 = ", part1)
    part2 = part_two(input_file)
    print("Part 2 = ", part2)


if __name__ == "__main__":
    # sys.exit(main("test_input.dat"))
    # sys.exit(main("test_2_input.dat"))
    sys.exit(main("puzzle_input.dat"))
