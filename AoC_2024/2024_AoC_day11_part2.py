import functools

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

data = inputFile.read().split()

stoneDict = {}
for stone in data:
    stoneDict[stone] = 1
    
@functools.cache
def RemoveZeros(string):
    for i, char in enumerate(string):
        if char != '0':
            return string[i:]
    return '0'

@functools.cache
def ChangeStoneLabel(num):
    if num == '0':
        return ['1']
    
    elif len(num) % 2 == 0:
        mid = int(len(num)/2)
        return [num[:mid], RemoveZeros(num[mid:])]
    
    else:
        return [str(int(num) * 2024)]
        

def ChangeStonesOfValue(value, newDict, sDict):
    newValues = ChangeStoneLabel(value)
    amount = sDict[value]
    for v in newValues:
        if v in newDict:
            newDict[v] += amount
        else:
            newDict[v] = amount
    return newDict
            
def ChangeAllStones(sDict):
    newDict = {}
    for key in sDict:
        newDict = ChangeStonesOfValue(key, newDict, sDict)
        
    return newDict

def RunBlinks(blinkNum, sDict):
    for blink in range(blinkNum):
        sDict = ChangeAllStones(sDict)
    return sum(sDict.values())
        
print(RunBlinks(75, stoneDict))