# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 18:30:39 2024

@author: joach
"""
import numpy as np

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

file = inputFile.readlines()
guardMap = np.array([list(line.split()[0]) for line in file])

guardDict = {'^' : [np.array([-1,0]), '>'],
             '>' : [np.array([0,1]), 'v'],
             'v' : [np.array([1,0]), '<'],
             '<' : [np.array([0,-1]), '^']}


def guardMovement(gMap, R, C):
    count = 0
    visited = [[[False, ''] for c in range(C)] for r in range(R)]
    direction = '^'
    position = np.array([np.argwhere(gMap == direction)[0]])
    position = position[0]
    edgeReached = False
    causesLoop = False
    while not edgeReached:
        if not visited[position[0]][position[1]][0]:
            count += 1 
            visited[position[0]][position[1]] = [True, direction]
        elif visited[position[0]][position[1]][1] == direction:
            edgeReached = True
            causesLoop = True
        nextPosition = position + guardDict[direction][0]
        if not 0 <= nextPosition[0] < R or not 0 <= nextPosition[1] < C:
            edgeReached = True
        else:
            if gMap[nextPosition[0], nextPosition[1]] == '#':
                direction = guardDict[direction][1]
            else:
                position = nextPosition    
    return count, causesLoop

def FindLoops(gMap):
    count = 0
    R, C = len(gMap), len(gMap[0])
    for r in range(R):
        print(r)
        for c in range(C):
            if gMap[r,c] != '#' and gMap[r,c] != '^': 
                tempMap = np.copy(gMap)
                tempMap[r,c] = '#'
                c, causesLoop = guardMovement(tempMap, R, C)
                if causesLoop:
                    count += 1
    return count
                
print(FindLoops(guardMap))