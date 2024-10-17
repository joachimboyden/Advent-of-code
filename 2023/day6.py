# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 08:47:01 2023

@author: joach
"""

import math as m

def part1():
    totalTime = [54,70,82,75]
    bestDistance = [239,1142,1295,1253]
    waysToWin = []
    for i in range(len(totalTime)):
        for j in range(totalTime[i]+1):
            distance = j*(totalTime[i] - j)
            if distance > bestDistance[i]:
                waysToWin.append(totalTime[i] + 1 - (j*2))
                break
    return waysToWin

def newWay(t, d):
    bit = m.sqrt((t**2) - (4*d))
    return m.floor((-t - bit)/-2) - m.ceil((-t + bit)/-2) + 1
    

def part2():
    totalTime = 54708275
    bestDistance =  239114212951253
    waysToWin = []
    for j in range(totalTime+1):
        distance = j*(totalTime - j)
        if distance > bestDistance:
            waysToWin.append(totalTime + 1 - (j*2))
            break
    return waysToWin

def multiplyList(myList):
 
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result

print('Part 1: ' + str(multiplyList(part1())))
print('Part 2: ' + str(multiplyList(part2())))
print('Better Way:')
print(newWay(54708275, 239114212951253))
