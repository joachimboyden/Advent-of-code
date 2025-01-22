# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:03:18 2024

@author: joach
"""

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

file = inputFile.readlines()
data = ['...'+line.split()[0]+'...' for line in file]
buffer = ''
for i in range(len(data[0])+6):
    buffer += '.'
for j in range(3):
    data.append(buffer)
    data.insert(0, buffer)

directions = [[-1,-1],[-1, 0],[-1, 1],
              [ 0,-1]        ,[ 0, 1],
              [ 1,-1],[ 1, 0],[ 1, 1]]

def CountXMAS(wordSearch):
    total = 0
    for i in range(len(wordSearch)):
        for j in range(len(wordSearch[i])):
            if wordSearch[i][j] == 'X':
                for d in directions:
                    check = wordSearch[i+d[0]][j+d[1]] + wordSearch[i+2*d[0]][j+2*d[1]] + wordSearch[i+3*d[0]][j+3*d[1]]
                    if check == 'MAS':
                        total += 1
    return total

def CountXMASPartTwo(wordSearch):
    total = 0
    MAS = ['MS', 'SM']
    for i in range(len(wordSearch)):
        for j in range(len(wordSearch[i])):
            if wordSearch[i][j] == 'A':
                checkOne = wordSearch[i-1][j+1] + wordSearch[i+1][j-1]
                checkTwo = wordSearch[i-1][j-1] + wordSearch[i+1][j+1]
                if checkOne in MAS and checkTwo in MAS:
                    total += 1
    return total
                        
print(CountXMASPartTwo(data))
    