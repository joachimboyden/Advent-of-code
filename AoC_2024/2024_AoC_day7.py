# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 10:01:58 2024

@author: joach
"""

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

file = inputFile.readlines()
data = [[int(line.split(':')[0]), list(map(int, line.split(':')[1].split()))] for line in file]

def can_make(value, nums, concat):
    if len(nums) == 1:
        return nums[0] == value

    last = nums[-1]

    if value % last == 0:
        possible_mul = can_make(value // last, nums[:-1], concat)
    else:
        possible_mul = False

    possible_concat = False
    if concat:
        next_power_of_10 = 1
        
        while next_power_of_10 <= last:
            next_power_of_10 *= 10
        if (value - last) % next_power_of_10 == 0:
            possible_concat = can_make((value - last) // next_power_of_10, nums[:-1], concat)
        else:
            possible_concat = False

    possible_add = can_make(value - last, nums[:-1], concat)
    return possible_mul or possible_add or possible_concat

total = 0
for line in data:
    value, nums = line[0], line[1]
    if can_make(value, nums, True):
        total += value

print(total)  
 