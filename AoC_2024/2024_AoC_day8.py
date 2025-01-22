# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 09:47:30 2024

@author: joach
"""
import numpy as np

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

file = inputFile.readlines()
data = [list(line.split()[0]) for line in file]

antinodes = [[False for c in data[0]] for r in data]
R = len(data)
C = len(data[0])
    
def FindAntinodePair(node1, node2):
    c = 0
    vector = node2 - node1
    anti1, anti2 = node1 - vector, node2 + vector
    if 0 <= anti1[0] < R and 0 <= anti1[1] < C and not antinodes[anti1[0]][anti1[1]]:
        antinodes[anti1[0]][anti1[1]] = True
        c +=1
    if 0 <= anti2[0] < R and 0 <= anti2[1] < C and not antinodes[anti2[0]][anti2[1]]:
        antinodes[anti2[0]][anti2[1]] = True
        c +=1
    return c

def FindAntinodeRun(node1, node2):
    c = 0
    vector = node2 - node1
    anti = np.copy(node1)
    while 0 <= anti[0] < R and 0 <= anti[1] < C:
        if not antinodes[anti[0]][anti[1]]:
            c += 1
            antinodes[anti[0]][anti[1]] = True
        anti += vector
    anti = np.copy(node1)
    while 0 <= anti[0] < R and 0 <= anti[1] < C:
        if not antinodes[anti[0]][anti[1]]:
            c += 1
            antinodes[anti[0]][anti[1]] = True
        anti -= vector
        
    return c

def FindAllAntinodes(maap):
    count = 0
    for r in range(len(maap)):
        for c in range(len(maap[r])):
            if maap[r][c] == '.':
                pass
            else:
                node = maap[r][c]
                maap[r][c] = '.'
                for i in range(len(maap)):
                    for j in range(len(maap[i])):
                        if maap[i][j] == node:
                            count += FindAntinodeRun(np.array([r,c]), np.array([i,j]))
    return count

print(FindAllAntinodes(data))

'''
def temp(boo):
    if boo:
        return '#'
    else:
        return '.'
    
print('\n'.join([''.join(list(map(temp, line))) for line in antinodes]))
'''
            
                
                