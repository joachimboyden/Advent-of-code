# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 10:39:04 2024

@author: joach
"""

import re

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

file = inputFile.read().split('\n\n')
machineList = []
for line in file:
    v = list(map(int, re.findall("[0-9]+", line)))
    machine = {'A' : (v[0], v[1]),
               'B' : (v[2], v[3]),
               'prize' : (v[4], v[5])}
    machineList.append(machine)

def FindCheapestRoute(machine):
    #goal = machine['prize']
    goal = (machine['prize'][0] + 10000000000000, machine['prize'][1] + 10000000000000)
    A = machine['A']
    B = machine['B']
    
    cost = ((goal[1] * (A[0] - 3*B[0])) + (goal[0] * (3*B[1] - A[1]))) / ((B[1] * A[0]) - (B[0] * A[1]))
    try:
        y = (cost - (goal[1] / B[1])) / (3 - (A[1] / B[1]))
    except:
        print('divition by zero')
        y = (cost - (goal[0] / B[0])) / (3 - (A[0] / B[0]))
        
    x = cost - 3*y
    G = (y*A[0] + x*B[0], y*A[1] + x*B[1])
    print(G, cost)
    if cost.is_integer():
        G = (round(G[0], 6), round(G[1], 6))
        if G == goal:
            return cost
        else:
            return 0
    else:
        return 0
    
#print(FindCheapestRoute(machineList[3]))

def CountCost():
    total = 0
    for i, machine in enumerate(machineList):
        cost = FindCheapestRoute(machine)
        total += cost
    return total

print(CountCost())

'''

75800131617315
62666303468007
48720930105847
47112712563478
52610277537794
63399586353946

59666640250625
366164463110739


'''


            