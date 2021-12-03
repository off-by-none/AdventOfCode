'''
Advent of Code
Year 2015
Day 05
https://adventofcode.com/2015/day/5
TODO: Should just use regex.
'''

# PART01
def part_01(puzzle_input):
    total_nice_strings = 0

    for input in puzzle_input:
        if contains_three_or_more_vowels(input) and contains_double_letters(input) and not contains_bad_strings(input):
            total_nice_strings += 1

    return total_nice_strings


# PART02
def part_02(puzzle_input):
    total_nice_strings = 0

    for input in puzzle_input:
        if contains_repeating_pairs(input) and contains_middle_letter(input):
            total_nice_strings += 1

    return total_nice_strings


def contains_three_or_more_vowels(string):
    total_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for letter in string:
        if letter in vowels:
            total_vowels += 1
    
    return total_vowels >= 3


def contains_double_letters(string):
    previous_letter = ''
    
    for letter in string:
        if letter == previous_letter:
            return True
        previous_letter = letter
    
    return False


def contains_bad_strings(string):
    previous_letter = ''
    bad_strings = ['ab', 'cd', 'pq', 'xy']
    
    for letter in string:
        if previous_letter + letter in bad_strings:
            return True
        previous_letter = letter

    return False


def contains_repeating_pairs(string):
    pairs = []
    for i in range(len(string) - 1):
        pairs.append(string[i] + string[i + 1])
    
    for x in range(len(pairs) - 2):
        for y in range(x + 2, len(pairs)):
            if pairs[x] == pairs[y]:
                return True
    
    return False


def contains_middle_letter(string):
    pairs = []
    for i in range(len(string) - 1):
        pairs.append(string[i] + string[i + 1])

    for i in range(len(pairs) - 1):
        if pairs[i][0] == pairs[i + 1][1]:
            return True

    return False


if __name__ == "__main__":
    file = r"..\..\inputs\2015\aoc201505.txt"
    puzzle_input = open(file, 'r').read().split('\n')
    
    solution = part_01(puzzle_input)
    print(solution) # 236
    
    solution = part_02(puzzle_input)
    print(solution) # 51
