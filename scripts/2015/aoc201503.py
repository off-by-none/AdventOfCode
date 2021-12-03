'''
Advent of Code
Year 2015
Day 03
https://adventofcode.com/2015/day/3
'''

# PART01
def part_01(puzzle_input):
    distinct_houses = []
    visited_houses = [[0, 0]]

    for direction in puzzle_input:
        previous_house = visited_houses[-1]
        next_house = move_to_next_house(previous_house, direction)
        visited_houses.append(next_house)

    for house in visited_houses:
        if house not in distinct_houses:
            distinct_houses.append(house)
    
    return len(distinct_houses)


# PART02
def part_02(puzzle_input):
    distinct_houses = []
    santa_visited_houses = [[0, 0]]
    robo_visited_houses = [[0, 0]]
    direction_count = 0

    for direction in puzzle_input:
        direction_count += 1

        if direction_count % 2 == 0:
            previous_house = santa_visited_houses[-1]
            next_house = move_to_next_house(previous_house, direction)
            santa_visited_houses.append(next_house)
        else: 
            previous_house = robo_visited_houses[-1]
            next_house = move_to_next_house(previous_house, direction)
            robo_visited_houses.append(next_house)

    all_visited_houses = santa_visited_houses + robo_visited_houses

    for house in all_visited_houses:
        if house not in distinct_houses:
            distinct_houses.append(house)
    
    return len(distinct_houses)


def move_to_next_house(location, direction):
    house_row = location[0]
    house_col = location[1]

    if direction == '^': house_row += 1
    elif direction == 'v': house_row -= 1
    elif direction == '>': house_col += 1
    elif direction == '<': house_col -= 1

    next_house = [house_row, house_col]
    return next_house


# Puzzle Input
if __name__ == "__main__":
    file = r"..\..\inputs\2015\aoc201503.txt"
    puzzle_input = open(file, 'r').read()
    
    solution = part_01(puzzle_input)
    print(solution) # 2081
    
    solution = part_02(puzzle_input)
    print(solution) # 2341
