# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 10:23:00 2024

@author: joach
"""
import functools

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

data = inputFile.read().split()

@functools.cache
def RemoveZeros(string):
    for i, char in enumerate(string):
        if char != '0':
            return string[i:]
    return '0'

def ChangeStone(index):
    num = data[index]
    if num == '0':
        data[index] = '1'
        
    elif len(num) % 2 == 0:
        half = int(len(num)/2)
        data[index] = RemoveZeros(num[half:])
        data.insert(index, num[:half])
        return True
    
    else:
        data[index] = str(int(num)*2024)
        
    return False
    
def ChangeAllStones():
    stoneDoubled = False
    for i, stone in enumerate(data):
        if not stoneDoubled:
            stoneDoubled = ChangeStone(i)
        else:
            stoneDoubled = False
        
def RunBlinks(blinkNum):
    for blink in range(blinkNum):
        print(len(data))
        ChangeAllStones()
    return len(data)
        
print(RunBlinks(25))