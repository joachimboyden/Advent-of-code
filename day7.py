# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 08:04:19 2023

@author: joach
"""

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

file = inputFile.readlines()
data = [line.split() for line in file]

handTier = [[1,1,1,1,1],
            [2,1,1,1],
            [2,2,1],
            [3,1,1],
            [3,2],
            [4,1],
            [5]]

charTier = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
jokerTier

def GetHandType(hand):
    usedChars = []
    copies = []
    for char in hand:
        if char not in usedChars:
            copies.append(hand.count(char))
            usedChars.append(char)
        
    return sorted(copies, reverse=True)

def IsHandBigger(hand1, hand2):
    handType1 = GetHandType(hand1)
    handType2 = GetHandType(hand2)
    if handTier.index(handType1) > handTier.index(handType2):
        return True
    elif handTier.index(handType1) < handTier.index(handType2):
        return False
    else:
        for i in range(len(hand1)):
            if charTier.index(hand1[i]) > charTier.index(hand2[i]):
                return True
            elif charTier.index(hand1[i]) < charTier.index(hand2[i]):
                return False
        
def sortHands():
    sortedHands = [0]*len(data)
    for hand in data:
        place = 0
        for compareHand in data:
            if IsHandBigger(hand[0], compareHand[0]):
                place += 1
        sortedHands[place] = (int(hand[1]))*(place+1)
    
    return sum(sortedHands)

print(sortHands())


inputFile.close()
testFile.close()