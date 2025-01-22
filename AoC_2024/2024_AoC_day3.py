# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 17:46:19 2024

@author: joach
"""

import re

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

file = inputFile.readlines()

partOneRegEx = "mul\([1-9][0-9]*,[1-9][0-9]*\)"
partTwoRegEx = "don't\(\)|do\(\)|mul\([1-9][0-9]*,[1-9][0-9]*\)"

def FindUncorruptedMemory(memory, regEx):
    newMemory = []
    for line in memory:
        newMemory.extend(re.findall(regEx, line))
    return newMemory

def CalculateMemory(memory):
    total = 0
    doMult = True
    for mult in memory:
        if mult == "don't()":
            doMult =  False 
        elif mult == "do()":
            doMult = True
        else:
            if doMult:
                numbers = re.findall("[1-9][0-9]*", mult)
                total += int(numbers[0])*int(numbers[1])
    return total

print(CalculateMemory(FindUncorruptedMemory(file, partTwoRegEx)))