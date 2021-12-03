'''
Advent of Code
Year 2015
Day 06
https://adventofcode.com/2015/day/6
TODO: use regex
'''

# PART01
def part_01(puzzle_input):
    lights = [[0 for x in range(1000)] for y in range(1000)]
    lights_on_count = 0
    for instruction in puzzle_input:
        action = instruction[0]
        
        if action == "toggle":
            for light_row in range(instruction[2], instruction[4] + 1):
                for light_col in range(instruction[1], instruction[3] + 1):
                    if lights[light_row][light_col] == 0:
                        lights[light_row][light_col] = 1
                    else:
                        lights[light_row][light_col] = 0
        elif action == "off":
            for light_row in range(instruction[2], instruction[4] + 1):
                for light_col in range(instruction[1], instruction[3] + 1):
                    lights[light_row][light_col] = 0
        elif action == "on":
            for light_row in range(instruction[2], instruction[4] + 1):
                for light_col in range(instruction[1], instruction[3] + 1):
                    lights[light_row][light_col] = 1

    for x in range(1000):
        for y in range(1000):
            lights_on_count += lights[x][y]

    return lights_on_count


# PART02
def part_02(puzzle_input):
    lights = [[0 for x in range(1000)] for y in range(1000)]
    brightness = 0
    for instruction in puzzle_input:
        action = instruction[0]
        
        if action == "toggle":
            for light_row in range(instruction[2], instruction[4] + 1):
                for light_col in range(instruction[1], instruction[3] + 1):
                    lights[light_row][light_col] += 2
        elif action == "off":
            for light_row in range(instruction[2], instruction[4] + 1):
                for light_col in range(instruction[1], instruction[3] + 1):
                    if lights[light_row][light_col] > 0:
                        lights[light_row][light_col] -= 1
        elif action == "on":
            for light_row in range(instruction[2], instruction[4] + 1):
                for light_col in range(instruction[1], instruction[3] + 1):
                    lights[light_row][light_col] += 1

    for x in range(1000):
        for y in range(1000):
            brightness += lights[x][y]

    return brightness


def format_input(input):
    formatted_input = []
    for instruction in input:
        build_instruction = []
        instruction = instruction.split(" ")
        
        if "turn" in instruction:
            instruction.remove("turn")
        
        start = instruction[1].split(",")
        end = instruction[3].split(",")

        build_instruction.append(instruction[0])
        build_instruction.append(int(start[0]))
        build_instruction.append(int(start[1]))
        build_instruction.append(int(end[0]))
        build_instruction.append(int(end[1]))
        
        formatted_input.append(build_instruction)

    return formatted_input


if __name__ == "__main__":
    file = r"..\..\inputs\2015\aoc201506.txt"
    puzzle_input = open(file, 'r').read().split('\n')
    puzzle_input = format_input(puzzle_input)

    solution = part_01(puzzle_input)
    print(solution) # 543903
    
    solution = part_02(puzzle_input)
    print(solution) # 14687245
