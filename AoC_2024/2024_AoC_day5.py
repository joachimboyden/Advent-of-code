# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 12:57:52 2024

@author: joach
"""
import math as m

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

file = testFile.read()
instructionsFile, pagesFile = file.strip().split('\n\n')
instructionsData = [tuple(map(int, pair.split('|'))) for pair in instructionsFile.splitlines()]
pagesData = [list(map(int, pages.split(','))) for pages in pagesFile.splitlines()]

pageDict = {pair[0]:[] for pair in instructionsData}
for pair in instructionsData:
    pageDict[pair[0]].append(pair[1])
    
def CheckPagesInOrder(pageList):
    for page in pageList:
        if page in pageDict:
            for previousPage in pageList[:pageList.index(page)]:
                if previousPage in pageDict[page]:
                    return False
    return True

def FindMiddlePage(pageList):
    return pageList[m.floor(len(pageList)/2)]

def PartOne():
    total = 0
    for pageList in pagesData:
        if CheckPagesInOrder(pageList):
            total += FindMiddlePage(pageList)
    return total

def OrderPages(pageList):
    ordered = False
    while not ordered:
        for page in pageList:
            if page in pageDict:
                for previousPage in pageList[:pageList.index(page)]:
                    if previousPage in pageDict[page]:
                        i, j = pageList.index(page), pageList.index(previousPage)
                        pageList[i], pageList[j] = pageList[j], pageList[i]
        if CheckPagesInOrder(pageList):
            ordered = True
    return pageList

def TopSort(pageList):
    N = len(pageList)
    V = [False for p in pageList]
    ordering = [0 for p in pageList]
    i = N - 1
    
    for at in range(N):
        print(at)
        if V[at] == False:
            visitedNodes = []
            V, visitedNodes = Dfs(at, V, visitedNodes, pageDict, pageList)
            for nodeID in visitedNodes:
                ordering[i] = nodeID
                i -= 1
    return ordering

def Dfs(at, V, visitedNodes, graph, nodes):
    V[at] = True
    edges = graph.get(nodes[at])
    for edge in edges:
        if edge in nodes:
            if V[nodes.index(edge)] == False:
                print(edge)
                #V, visitedNodes = Dfs(at, V, visitedNodes, graph, nodes)
    visitedNodes.append(nodes[at])
    return V, visitedNodes
            
def PartTwo():
    total = 0
    for pageList in pagesData:
        if not CheckPagesInOrder(pageList):
            total += FindMiddlePage(OrderPages(pageList))
    return total

print(pagesData[3])
print(pageDict)
print(TopSort(pagesData[3]))

            