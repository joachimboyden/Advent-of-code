# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 13:58:45 2023

@author: joach
"""

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

file = inputFile.readlines()
data = [line.split() for line in file]
for line in range(len(data)):
    for n in range(len(data[line])):
        data[line][n] = int(data[line][n])

def GetSeqDifference(seq):
    diffSeq = []
    for n in range(len(seq) - 1):
        diffSeq.append(seq[n+1]-seq[n])
    return diffSeq

def GetAllSeqs(seq):
    sequences = [seq]
    while True:
        sequences.append(GetSeqDifference(sequences[-1]))
        if all([n == 0 for n in sequences[-1]]):
               return sequences
           
def FindNextInSeq(seq):
    sequence = GetAllSeqs(seq)
    nextValue = 0
    for lis in reversed(sequence):
        nextValue = nextValue + lis[-1]
    return nextValue

def FindBeforeInSeq(seq):
    sequence = GetAllSeqs(seq)
    beforeValue = 0
    for lis in reversed(sequence):
        beforeValue = lis[0] - beforeValue
    return beforeValue

def PartTwo():
    finalValues = []
    for line in data:
        finalValues.append(FindBeforeInSeq(line))
    return sum(finalValues)

def mainLoop():
    finalValues = []
    for line in data:
        finalValues.append(FindNextInSeq(line))
    return sum(finalValues)

print(PartTwo())

inputFile.close()
testFile.close()