import sys


def extract_digits(strval):
    return [i for i in strval if i.isdigit()]


def first_last_digit(digits):
    first_last = ''.join([digits[0], digits[-1]])
    return int(first_last)


def main(input_file):
    calibration_values = []
    with open(input_file, 'r') as data:
        for line in data:
            digits = extract_digits(line)
            value = first_last_digit(digits)
            calibration_values.append(value)

    part1 = sum(calibration_values)
    print("Part 1 = ", part1)


if __name__ == "__main__":
    # sys.exit(main("test_input.dat"))
    sys.exit(main("puzzle_input.dat"))
