'''
Advent of Code
Year 2021
Day 01
https://adventofcode.com/2021/day/1
'''

# PART 1
def part_01(puzzle_input):
    number_of_increases = -1
    current = 0

    for x in puzzle_input:
        if x > current:
            number_of_increases += 1
        current = x

    return number_of_increases


# PART 2
def part_02(puzzle_input):
    number_of_increases = -1
    sliding_sum = 0
    current = 0

    for x in range(len(puzzle_input) - 2):
        sliding_sum = sum(puzzle_input[x:x+3])
        if sliding_sum > current:
            number_of_increases += 1
        current = sliding_sum

    return number_of_increases


# Get Input
if __name__ == "__main__":
    file = r"C:\Users\BBREWER2\Documents\MyDirectory\AdventOfCode\inputs\2021\aoc202101.txt"
    puzzle_input = open(file, 'r').read().split('\n')
    puzzle_input = list(map(int, puzzle_input))
    
    solution = part_01(puzzle_input)
    print(solution) # 1754
    
    solution = part_02(puzzle_input)
    print(solution) # 1789
