'''
Advent of Code
Year 2015
Day 04
https://adventofcode.com/2015/day/4
TODO: Feels like cheating to use a hashing library and brute-forcing the solution; revisit with own algo 
'''

import hashlib

# PART01
def part_01(puzzle_input):
    advent_coin = find_coin(puzzle_input, 5)
    return advent_coin


# PART02
def part_02(puzzle_input):
    advent_coin = find_coin(puzzle_input, 6)
    return advent_coin


def find_coin(secret_key, padding):
    solution = 0
    while True:
        solution += 1
        hashkey = secret_key + str(solution)
        result = hashlib.md5(hashkey.encode())
        md5 = result.hexdigest()
        md5_padding = md5[0:padding]
        if len(set(md5_padding)) == 1 and str(md5_padding[0]) == '0':
            return(solution)


if __name__ == "__main__":
    file = r"..\..\inputs\2015\aoc201504.txt"
    puzzle_input = open(file, 'r').read()
    
    solution = part_01(puzzle_input)
    print(solution) # 282749
    
    solution = part_02(puzzle_input)
    print(solution) # 9962624
