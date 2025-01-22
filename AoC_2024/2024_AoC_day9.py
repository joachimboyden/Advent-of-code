# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 17:44:56 2024

@author: joach
"""

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

file = inputFile.read()
data = []
def ProcessData(part):
    for i, num in enumerate(file):
        if i%2 == 0:
            section = [str(int(i/2)) for n in range(int(num))]
        else:
            section = ['.' for n in range(int(num))]
        data.extend(section) 

ProcessData(1)

def moveData(d):
    furthest = 0
    for i, dataPoint in reversed(list(enumerate(d))):
        if dataPoint != '.':
            for j in range(furthest, len(d)):
                if d[j] == '.':
                    furthest = j
                    if j > i:
                        return d
                    d[j] = dataPoint
                    d[i] = '.'
                    break
                
def moveDataTwo(d):
    IDsChecked = []
    for i, value in reversed(list(enumerate(d))):
        print(i)
        if value != '.' and value not in IDsChecked:
            IDsChecked.append(value)
            setFound = False
            length = 0
            while not setFound:
                if d[i-length] != value:
                    setFound = True
                else:
                    length += 1
            
            for j in range(len(d)):
                if d[j] == '.' and j < i:
                    setFound = False
                    l = 0
                    while not setFound:
                        if d[j+l] != '.':
                            setFound = True
                        else:
                            l += 1
                    
                    if l >= length:
                        for k in range(length):
                            d[j+k] = value
                            d[i-k] = '.'
                        break
    return d
                        
                
def FindChecksum(d):
    checksum = 0
    for i, num in enumerate(d):
        if num == '.':
            pass
        else:
            checksum += i * int(num)
    return checksum
                
print(FindChecksum(moveDataTwo(data)))