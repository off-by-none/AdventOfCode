'''
Advent of Code
Year 2015
Day 01
https://adventofcode.com/2015/day/1
'''
from collections import Counter

# Part 01
def part_01(puzzle_input):
    cnt = Counter(puzzle_input)
    ups = cnt['(']
    downs = cnt[')']

    return ups - downs


# Part 02
def part_02(puzzle_input):
    floor = 0
    position = 0

    for command in puzzle_input:
        position += 1
        
        if command == '(': 
            floor += 1
        elif command == ')': 
            floor -= 1
        
        if floor < 0:
            break

    return position


# Puzzle Input
if __name__ == "__main__":
    file = r"..\..\inputs\2015\aoc201501.txt"
    puzzle_input = open(file, 'r').read().split('\n')
    puzzle_input = puzzle_input[0]
    
    solution = part_01(puzzle_input)
    print(solution) # 280
    
    solution = part_02(puzzle_input)
    print(solution) # 1797
