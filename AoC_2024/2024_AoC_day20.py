# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 10:54:08 2024

@author: joach
"""
import copy

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

file = testFile.readlines()
data = [list(line.split()[0]) for line in file]

X, Y = len(data), len(data[0])
print(X, Y)
start, end = (0,0), (0,0)
for i in range(X):
    for j in range(Y):
        if data[i][j] == 'S':
            start = (i,j)
        elif data[i][j] == 'E':
            end = (i,j)

def MakeGraph(grid):
    graph = {}
    for i, line in enumerate(grid):
        for j, obj in enumerate(line):
            graph[(i, j)] = FindNeighbours((i, j), grid)
            
    return graph

def FindNeighbours(location, grid):
    neighbours = []
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    for d in directions:
        x = d[0]+location[0]
        y = d[1]+location[1]
        if 0 <= x < X and 0 <= y < Y:
            newLoc = (x, y)
            if grid[newLoc[0]][newLoc[1]] in '.SE':
                neighbours.append(newLoc)
                
    return neighbours

class Node():
    
    def __init__(self, parent=None, position=None):
        self.parent = parent 
        self.position = position 
        self.h = 0
        self.g = 0
        self.f = 0
        
    def Equal(self, other):
        return self.position == other.position
    
def AStar(graph, start, end):
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0
    
    queue = []
    visited = []
    
    queue.append(start_node)
    
    while len(queue) > 0:
        current_node = queue[0]
        index = 0
        for i, node in enumerate(queue):
            if node.f < current_node.f:
                current_node = node
                index = i
                
                
        queue.pop(index)
        visited.append(current_node)
        
        if current_node.Equal(end_node):
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
                
            return path[::-1]
        
        neighbours = [Node(current_node, p) for p in graph[current_node.position]]
        
        for neigh in neighbours:
            
            visited_pos = [v.position for v in visited]
            if neigh.position in visited_pos:
                continue
            
            neigh.g = current_node.g + 1
            neigh.h = abs((neigh.position[0] - end_node.position[0])) + abs((neigh.position[1] - end_node.position[1]))
            neigh.f = neigh.g + neigh.h
            
            queue_pos = [q.position for q in queue]
            if neigh.position in queue_pos:
                continue
                
            queue.append(neigh)
            
    return 'fail'

baseTime = len(AStar(MakeGraph(data), start, end)) - 1
print(baseTime)

def FindCheats(maze):
    cheats = []
    for i, line in enumerate(maze):
        for j, point in enumerate(line):
            if point == '#':
                cheats.append((i,j))
                        
    return cheats

def AddCheat(maze, cheat):
    newMaze = copy.deepcopy(maze)
    newMaze[cheat[0]][cheat[1]] = '.'
    return newMaze

def RunSim(maze):
    count = 0
    for cheat in FindCheats(maze):
        print(cheat)
        newMaze = AddCheat(maze, cheat)
        time = len(AStar(MakeGraph(newMaze), start, end)) - 1
        if baseTime - time >= 100:
            count += 1

    return count

def PrintMaze(maze):
    for line in maze:
        print(''.join(line))
        
print(RunSim(data))