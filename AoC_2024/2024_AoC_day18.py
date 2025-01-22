# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:48:11 2024

@author: joach
"""
import numpy as np

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

file = inputFile.readlines()
data = [list(map(int, line.split()[0].split(','))) for line in file]

X = 71
Y = 71
grid = np.full((X, Y), '.')

def DropBytes(byteNum, grid):
    for i in range(byteNum):
        byte = data[i]
        x = byte[0]
        y = byte[1]
        grid[y, x] = '#'
    
    for line in grid:
        print(''.join(line))
        
    return grid

def DropBytesSlow(startByte, grid):
    for i, byte in enumerate(data):
        x = byte[0]
        y = byte[1]
        grid[y, x] = '#'
        if i >= startByte:
            print(i)
            path = AStar(MakeGraph(grid), (0,0), (X-1,Y-1))
            if path == 'fail':
                return byte
            else:
                continue
            

def FindNeighbours(location, grid):
    neighbours = []
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    for d in directions:
        x = d[0]+location[0]
        y = d[1]+location[1]
        if 0 <= x < X and 0 <= y < Y:
            newLoc = (x, y)
            if grid[tuple(newLoc)] == '.':
                neighbours.append(newLoc)
                
    return neighbours

def MakeGraph(grid):
    graph = {}
    for i, line in enumerate(grid):
        for j, obj in enumerate(line):
            graph[(i, j)] = FindNeighbours((i, j), grid)
            
    return graph

#----------------A-Star--------------------------------------------------------

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

print(DropBytesSlow(2900, grid))


'''
path = AStar(MakeGraph(12, grid), (0,0), (X-1,Y-1))
for i in path:
    grid[tuple((i[0], i[1]))] = 'O'
    
print(len(path) - 1)
    
for line in grid:
    print(''.join(line))

'''