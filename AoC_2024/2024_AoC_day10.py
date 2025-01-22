# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:32:06 2024

@author: joach
"""

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

file = inputFile.readlines()
data = [list(map(int, list(line.split()[0]))) for line in file]

directions = [[0,1],[0,-1],[1,0],[-1,0]]

def FindTrailScore(start, nines):
    score = 0
    rating = 0
    position = start
    splitFound = False
    splits = []
    
    if data[position[0]][position[1]] == 9:
        if position not in nines:
            nines.append(position)
            score += 1
        rating += 1
        return score, nines, rating
    
    while not splitFound:
        nextPositions = []
        for d in directions:
            try:
                data[position[0]+d[0]][position[1]+d[1]]
            except:
                pass
            else:
                if data[position[0]+d[0]][position[1]+d[1]] == data[position[0]][position[1]]+1 and position[0]+d[0] >= 0 and position[1]+d[1] >= 0:
                    nextPositions.append([position[0]+d[0], position[1]+d[1]])
                    
        if len(nextPositions) == 1:
            position = nextPositions[0]
            if data[position[0]][position[1]] == 9:
                if position not in nines:   
                    nines.append(position)
                    score += 1
                rating += 1
                return score, nines, rating
                
        elif len(nextPositions) == 0:
            return score, nines, rating
        
        else:
            splits = nextPositions
            splitFound = True
            
    for split in splits:
        s, nines, r = FindTrailScore(split, nines)
        score += s
        rating += r
        
    return score, nines, rating

#print(FindTrailScore([6,0], [])[0])
        
def FindTrailHeads():
    score = 0
    rating = 0
    for i, line in enumerate(data):
        for j, point in enumerate(line):
            if point == 0:
                s, nines, r = FindTrailScore([i,j], [])
                rating += r
                score += s
    return score, rating

print(FindTrailHeads())