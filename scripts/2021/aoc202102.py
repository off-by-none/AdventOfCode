'''
Advent of Code
Year 2021
Day 02
https://adventofcode.com/2021/day/2
'''

# PART 1
def part_01(puzzle_input):
    position = 0
    depth = 0
    
    for command in puzzle_input:
        command = command.split(' ')
        direction = command[0]
        units = int(command[1])
        
        if direction == 'forward':
            position += units
        elif direction == 'down':
            depth += units
        elif direction == 'up':
            depth -= units

    return position * depth


# PART 2
def part_02(puzzle_input):
    position = 0
    depth = 0
    aim = 0
    
    for command in puzzle_input:
        command = command.split(' ')
        direction = command[0]
        units = int(command[1])
        
        if direction == 'forward':
            position += units
            depth += units * aim
        elif direction == 'down':
            aim += units
        elif direction == 'up':
            aim -= units

    return position * depth


# Get Input
if __name__ == "__main__":
    file = r"..\..\inputs\2021\aoc202102.txt"
    puzzle_input = open(file, 'r').read().split('\n')
    
    solution = part_01(puzzle_input)
    print(solution) # 1524750
    
    solution = part_02(puzzle_input)
    print(solution) # 1592426537
