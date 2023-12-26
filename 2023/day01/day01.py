import re

def parse_line(line):
    first_digit = int(line[0])
    last_digit = int(line[-1])
    return first_digit * 10 + last_digit

def sum_calibration_values(text):
    lines = text.splitlines()
    calibration_values = []
    for line in lines:
        calibration_values.append(parse_line(line))
    return sum(calibration_values)

with open('input.txt', 'r') as f:
    text = f.read()

print(sum_calibration_values(text))