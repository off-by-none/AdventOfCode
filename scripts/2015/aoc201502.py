'''
Advent of Code
Year 2015
Day 02
https://adventofcode.com/2015/day/2
'''

# Part 01
def part_01(puzzle_input):
    total_wrapping_needed = 0

    for present in puzzle_input:
        length = present[0]
        width = present[1]
        height = present[2]

        side01 = length * width
        side02 = width * height
        side03 = height * length

        wrapping_needed = 2 * (side01 + side02 + side03)
        slack = min(side01, side02, side03)

        total_wrapping_needed += wrapping_needed + slack
    
    return total_wrapping_needed


# Part 02
def part_02(puzzle_input):
    total_ribbon_needed = 0

    for present in puzzle_input:
        length = present[0]
        width = present[1]
        height = present[2]

        perimeter01 = 2 * (length + width)
        perimeter02 = 2 * (width + height)
        perimeter03 = 2 * (height + length)

        ribbon_needed = min(perimeter01, perimeter02, perimeter03)
        bow = length * width * height

        total_ribbon_needed += ribbon_needed + bow
    
    return total_ribbon_needed


# Puzzle Input
if __name__ == "__main__":
    file = r"..\..\inputs\2015\aoc201502.txt"
    puzzle_input = open(file, 'r').read().split('\n')
    puzzle_input = [x.split('x') for x in puzzle_input]
    puzzle_input = [list(map(int, x)) for x in puzzle_input]
    
    solution = part_01(puzzle_input)
    print(solution) # 1598415
    
    solution = part_02(puzzle_input)
    print(solution) # 3812909
