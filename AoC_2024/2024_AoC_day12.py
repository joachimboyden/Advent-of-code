# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 18:53:38 2024

@author: joach
"""

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

file = inputFile.readlines()
data = [list(line.split()[0]) for line in file]

directions = [[0,1],[0,-1],[1,0],[-1,0]]

corners = [[[-1,0],[0,-1],[-1,-1]],
           [[-1,0],[0,1],[-1,1]],
           [[1,0],[0,-1],[1,-1]],
           [[1,0],[0,1],[1,1]]]

visited = []

def FindNeighbours(x,y):
    neighbours = []
    for d in directions:
        if 0 <= x+d[0] < len(data) and 0 <= y+d[1] < len(data[0]):
            if data[x][y] == data[x+d[0]][y+d[1]]:
                neighbours.append([x+d[0], y+d[1]])
    return neighbours

def AddVectors(x, y, a, b):
    if 0 <= x+a < len(data) and 0 <= y+b < len(data[0]):
        return data[x+a][y+b]
    return '.'

def CountCorners(x, y):
    count = 0
    for c in corners:
        d = data[x][y]
        c1, c2 = AddVectors(x, y, c[0][0], c[0][1]), AddVectors(x, y, c[1][0], c[1][1])
        if c1 != d and c2 != d:
            count += 1
            
        c3 = AddVectors(x, y, c[2][0], c[2][1])
        if c1 == d and c2 == d and c3 != d:
            count += 1
    return count

def FindRegion(location):
    area = 0
    perimeter = 0
    sideNum = 0
    beenThere = []
    queue = [location]
    
    while queue != []:
        loc = queue[0]
        visited.append(loc)
        queue.pop(0)
        area += 1
        neighbours = FindNeighbours(loc[0], loc[1])
        sideNum += CountCorners(loc[0], loc[1])
        perimeter += 4 - len(neighbours)
        
        for n in neighbours:
            if n not in beenThere and n not in queue:
                queue.append(n)
        beenThere.append(loc)
        
    return area, perimeter, sideNum

def CalcFencingPrice():
    totalOne = 0
    totalTwo = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if [i,j] not in visited:
                area, perimeter, sides = FindRegion([i, j])
                totalOne += area*perimeter
                totalTwo += area*sides
    return totalOne, totalTwo

print(CalcFencingPrice())