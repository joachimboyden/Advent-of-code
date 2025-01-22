# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 10:19:44 2024

@author: joach
"""

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

file = inputFile.readlines()
data = [line.split() for line in file]

l1 = sorted([int(pair[0]) for pair in data])
l2 = sorted([int(pair[1]) for pair in data])

def Part_one():
    total = 0
    for i in range(len(l1)):
        total += abs(l1[i] - l2[i])
    
    return total
    
def Part_two():
    total = 0
    for num in l1:
        total += num * l2.count(num)
    return total

print(Part_two())
    

