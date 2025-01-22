# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 10:27:39 2024

@author: joach
"""

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

file = testFile.readlines()
codes = [list(line.split()[0]) for line in file]

numberPad = [['7', '8', '9'],
             ['4', '5', '6'],
             ['1', '2', '3'],
             ['' , '0', 'A']]

keyPad = [['', '^', 'A'],
          ['<','v', '>']]

direcDict = {(0,1)  : '>',
             (0,-1) : '<',
             (-1,0) : '^',
             (1,0)  : 'v'}

def GetIndex(character, array):
    for i, line in enumerate(array):
        for j, char in enumerate(line):
            if char == character:
                return (i, j)

def NumToString(lis):
    newList = []
    for num in lis:
        newList.append(direcDict[num])
    return newList

def VectorToInstructions(position, goal, pad):
    x = goal[0] - position[0]
    y = goal[1] - position[1]
    xSteps = [(int(x/abs(x)),0) for i in range(abs(x))]
    ySteps = [(0, int(y/abs(y))) for i in range(abs(y))]
    p = position
    instructions = ySteps + xSteps
    for step in instructions:
        p = (p[0] + step[0], p[1] + step[1])
        if pad[p[0]][p[1]] == '':
            return NumToString(xSteps) + NumToString(ySteps) + ['A']
    
    return NumToString(instructions) + ['A']

def GetNewCode(code, pad, start):
    position = start
    instructions = []
    for character in code:
        goal = GetIndex(character, pad)
        instructions += VectorToInstructions(position, goal, pad, )
        position = goal
        
    return instructions

def GetFinalCode():
    complexity = 0
    for code in codes:
        firstCode = GetNewCode(code, numberPad, (3,2))
        secondCode = GetNewCode(firstCode, keyPad, (0,2))
        thirdCode = GetNewCode(secondCode, keyPad, (0,2))
        complexity += len(thirdCode) * int(''.join(code)[:-1])
        
    return complexity

print(GetFinalCode())