'''
Advent of Code
Year 2021
Day 02
https://adventofcode.com/2021/day/2
'''

import math
import pandas as pd
import itertools as it
import numpy as np
from functools import reduce
import re


# PART 1
def part_01(puzzle_input):
    return True


# PART 2
def part_02(puzzle_input):
    return True


# Get Input
if __name__ == "__main__":
    file = r"C:\Users\BBREWER2\Documents\MyDirectory\AdventOfCode\inputs\2021\aoc202102.txt"
    puzzle_input = open(file, 'r').read().split('\n')
    puzzle_input = list(map(int, puzzle_input))
    
    solution = part_01(puzzle_input)
    print(solution)
    
    solution = part_02(puzzle_input)
    print(solution)
