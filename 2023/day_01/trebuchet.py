#!/usr/bin/env python3
# Advent of Code 2023 - Day 1: Trebuchet?!

import os

# Get cleaned data list from input file 
input_file = open("input.txt")
input_data = input_file.readlines()
input_file.close()
data = []
for line in input_data:
    data.append(line.strip())
    

values = 0
for line in data:
    # Finds first number in string
    for char in line:
        if char.isdigit():
            val1 = char
            break 
    # Finds last number in string
    for char in line:
        if char.isdigit():
            val2 = char
    # Combine first and last numbers and adds to total values
    value = (val1 + val2)
    values += int(value)

print("Part 1:", values)

