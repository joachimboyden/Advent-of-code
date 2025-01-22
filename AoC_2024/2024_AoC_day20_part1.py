# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 16:33:07 2024

@author: joach
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 10:54:08 2024

@author: joach
"""

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

file = inputFile.readlines()
data = [list(line.split()[0]) for line in file]

X, Y = len(data), len(data[0])
start, end = (0,0), (0,0)
directions = [(0,1), (0,-1), (1,0), (-1,0)]

for i in range(X):
    for j in range(Y):
        if data[i][j] == 'S':
            start = (i,j)
        elif data[i][j] == 'E':
            end = (i,j)

def PrintMaze(maze):
    for line in maze:
        print(''.join(line))
        
def FindBasePath(maze):
    position = start
    path = [start]
    previous = (0,0)
    while position != end:
        for d in directions:
            newPosition = (position[0] + d[0], position[1] + d[1])
            if maze[newPosition[0]][newPosition[1]] in '.E' and newPosition != previous:
                previous = position
                position = newPosition
                path.append(position)
                break
                
    return path

basePath = FindBasePath(data)
baseLength = len(basePath) - 1
print(baseLength, 'bang')

def FindCheats(maze):
    count = 0
    for i, step in enumerate(basePath):
        for d in directions:
            x, y = step[0] + d[0], step[1] + d[1]
            if maze[x][y] == '#':
                nextX, nextY = x + d[0], y + d[1]
                if 0 <= nextX < X and 0 <= nextY < Y:
                    if maze[nextX][nextY] in '.E':
                        index = basePath.index((nextX, nextY))
                        pathLength = i + 1 + baseLength - index
                        if baseLength - pathLength >= 100 and index > i:
                            #print(pathLength)
                            count += 1
                            
    return count

print(FindCheats(data))
                    