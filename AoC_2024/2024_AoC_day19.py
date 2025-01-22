# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 15:48:02 2024

@author: joach
"""

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

file = inputFile.read().split('\n\n')
availableTowels = file[0].split(', ')
desiredPatterns = file[1].split()


def IsComboPossible(pattern):
    possibleTowels = FindMatchs(pattern[0], len(pattern))
    print(len(possibleTowels))
    if possibleTowels == []:
        return False
    
    for towel in possibleTowels:
        
        if towel == pattern:
            return True
        
        elif towel == pattern[:len(towel)] and len(towel) <= len(pattern):
            
            if IsComboPossible(pattern[len(towel):]):
                return True
            
    return False
    
    
def FindMatchs(letter, length):
    towels = []
    
    for towel in availableTowels:
        
        if letter == towel[0] and len(towel) <= length:
            towels.append(towel)
            
    return towels

def IsPoss(pattern):
    if pattern in availableTowels:
        return True
    else:
        for i in range(len(pattern)):
            if pattern[:-i] in availableTowels:
                if IsPoss(pattern[-i:]):
                    return True
    
    return False

def CountPossible():
    count = 0
    
    for i, pattern in enumerate(desiredPatterns):
        print('')
        print(pattern, i)
        print('')
        if i != 7:
            if IsPoss(pattern):
                count += 1
            
    return count

print(IsPoss(desiredPatterns[7]))
#bwbbrrgrrbrggubuggwgguguburbbgbgrruggugbggggb