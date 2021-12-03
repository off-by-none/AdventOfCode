'''
Advent of Code
Year 2021
Day 03
https://adventofcode.com/2021/day/3
'''

# PART 1
def part_01(puzzle_input):
    gamma_binary_string = ''
    epsilon_binary_string = ''
    input_length_half = len(puzzle_input) / 2
    idx_array = [0] * len(puzzle_input[0])
    
    for input in puzzle_input:
        idx = 0
        for bit in input:
            idx_array[idx] += int(bit)
            idx += 1

    for bit_count in idx_array:
        if bit_count > input_length_half:
            gamma_binary_string += '1'
            epsilon_binary_string += '0'
        elif bit_count < input_length_half:
            gamma_binary_string += '0'
            epsilon_binary_string += '1'
        else: raise Exception('No.')

    gamma_rate = convert_to_decimal(gamma_binary_string)
    epsilon_rate = convert_to_decimal(epsilon_binary_string)
    power_consumption = gamma_rate * epsilon_rate
    
    return power_consumption


# PART 2
def part_02(puzzle_input):
    oxygen_rating = find_rating(puzzle_input, 0, True)
    co2_rating = find_rating(puzzle_input, 0, False)
    life_support_rating = convert_to_decimal(oxygen_rating) * convert_to_decimal(co2_rating)
    
    return life_support_rating


def convert_to_decimal(binary_number: str):
    number_length = len(binary_number)
    decimal_number = 0
    for i in binary_number:
        number_length -= 1
        number_place = 2 ** number_length
        decimal_number += int(i) * number_place
    
    return decimal_number


def find_rating(puzzle_input, idx, is_oxygen):
    input_length_half = len(puzzle_input) / 2
    bit_count = 0

    for input in puzzle_input:
        bit_count += int(input[idx])
    
    # filtering
    if (is_oxygen and bit_count >= input_length_half) or (not is_oxygen and bit_count < input_length_half):
        new_puzzle_input = [x for x in puzzle_input if x[idx] == '1']
    elif (is_oxygen and bit_count < input_length_half) or (not is_oxygen and bit_count >= input_length_half):
        new_puzzle_input = [x for x in puzzle_input if x[idx] == '0']

    # recurse until a single value remains
    if len(new_puzzle_input) == 1:
        return new_puzzle_input[0]
    return find_rating(new_puzzle_input, idx+1, is_oxygen)


# Get Input
if __name__ == "__main__":
    file = r"..\..\inputs\2021\aoc202103.txt"
    puzzle_input = open(file, 'r').read().split('\n')

    solution = part_01(puzzle_input)
    print(solution) # 4191876
    
    solution = part_02(puzzle_input)
    print(solution) # 3414905
