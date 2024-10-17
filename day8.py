# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:40:25 2023

@author: joach
"""

import math

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

file = inputFile.readlines()
directions = file[0][:-1]
file = file[2:]
locations = [line[0:3] for line in file]
left = [line[7:10] for line in file]
right = [line[12:15] for line in file]


def part1():
    index = locations.index('AAA')
    steps = 0
    while True:
        for point in directions:
            nextStep = 'N'
            if point == 'R':
                nextStep = right[index]
            elif point == 'L':
                nextStep = left[index]
            index = locations.index(nextStep)
            steps += 1
            if nextStep == 'ZZZ':
                return steps
        
            
def part2():
    indexes = [locations.index(location) for location in locations if location[2] == 'A']
    points = [point for point in locations if point[2] == 'A']
    length = len(points)
    firstZStep = []
    steps = 0
    while True:
        for point in directions:
            for i in range(len(indexes)):
                nextStep = 'N'
                if point == 'R':
                    nextStep = right[indexes[i]]
                elif point == 'L':
                    nextStep = left[indexes[i]]
                indexes[i] = locations.index(nextStep)
                points[i] = nextStep
            
            steps += 1
            P = 0
            found = False
            for p in range(len(points)):
                if points[p][2] == 'Z':
                    firstZStep.append(steps)
                    P = p
                    found = True
            if found:
                indexes.pop(P)
                points.pop(P)
                found = True
            if len(firstZStep) == length:
                return firstZStep
            

print(math.lcm(14429, 16271, 18113, 18727, 21797, 22411))

inputFile.close()
testFile.close()