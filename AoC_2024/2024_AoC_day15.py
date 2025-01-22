# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 12:57:30 2024

@author: joach
"""
import numpy as np

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

file = inputFile.read()
grid, moves = file.split('\n\n')
smallGrid = np.array([list(line) for line in grid.split('\n')])
bigGrid = np.array([list(line.replace('O','[]').replace('#','##').replace('.','..').replace('@','@.')) for line in grid.split('\n')])
moves = list(moves.replace('\n', ''))

directionDict = {'<' : np.array([0,-1]),
                 '>' : np.array([0,1]),
                 '^' : np.array([-1,0]),
                 'v' : np.array([1,0])}

robotPosition = np.array([np.where(bigGrid == '@')]).flatten()

def MoveRobot(direction):
    global robotPosition
    direc = directionDict[direction]
    aheadOfRobot = ['O']
    steps = 1
    
    while aheadOfRobot[-1] == 'O':
        aheadOfRobot.append(smallGrid[tuple(robotPosition + (direc * steps))])
        steps += 1
        
    if aheadOfRobot[-1] == '#':
        return
    
    for step in range(len(aheadOfRobot)-1, 0, -1):
        smallGrid[tuple(robotPosition + (direc * step))] = smallGrid[tuple(robotPosition + (direc * (step - 1)))]
    smallGrid[tuple(robotPosition)] = '.'
    
    robotPosition += direc
    
def MoveRobotBig(direction):
    global robotPosition
    direc = directionDict[direction]
    
    if direction in '<>':
        aheadOfRobot = [']']
        steps = 1
        
        while aheadOfRobot[-1] in '[]':
            aheadOfRobot.append(bigGrid[tuple(robotPosition + (direc * steps))])
            steps += 1
            
        if aheadOfRobot[-1] == '#':
            return
        
        for step in range(len(aheadOfRobot)-1, 0, -1):
            bigGrid[tuple(robotPosition + (direc * step))] = bigGrid[tuple(robotPosition + (direc * (step - 1)))]
        bigGrid[tuple(robotPosition)] = '.'
        
        robotPosition += direc
        
    elif direction in 'v^':
        blocksToMove = []
        queue = [robotPosition]
        
        while queue != []:
            currentPosition = queue[0]
            queue.pop(0)
            nextPosition = currentPosition + direc
            if tuple(currentPosition) not in blocksToMove:
                blocksToMove.append(tuple(currentPosition))
            nextBlock = bigGrid[tuple(nextPosition)]
            
            if nextBlock == '#':
                return
            
            elif nextBlock == '.':
                pass
            
            elif nextBlock == '[':
                queue.extend([nextPosition, nextPosition + np.array([0,1])])
                
            elif nextBlock == ']':
                queue.extend([nextPosition, nextPosition + np.array([0,-1])])
        
        for i in range(len(blocksToMove), 0, -1):
            bigGrid[tuple(blocksToMove[i-1] + direc)] = bigGrid[tuple(blocksToMove[i-1])]
            bigGrid[tuple(blocksToMove[i-1])] = '.'
            
        robotPosition += direc
    
def RunSim():
    for i, move in enumerate(moves):
        MoveRobotBig(move)
        
def CountCoordinates(target):
    RunSim()
    count = 0
    coordinates = np.array(np.where(bigGrid == target))
    for i in range(len(coordinates[0])):
        count += (100 * coordinates[0][i]) + coordinates[1][i]
        
    return count

def PrintGrid(direc, i):
    print('------' + str(direc) + '----' + str(i) + '-----')
    for line in bigGrid:
        print(''.join(line))
        
print(CountCoordinates('['))
        