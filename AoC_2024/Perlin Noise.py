# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 14:09:45 2025

@author: joach
"""

import random 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
import math as m

resolution = 256

gVectorOptions = [(1,1), (1,-1), (-1,1), (-1,-1)]

corners = [np.array([0,0]), np.array([0,1]), np.array([1,0]), np.array([1,1])]

def Ease(value):
    return (value**3) * (10 + (value * (6*value - 15)))

def Lerp(i1, i2, x):
    return i1 + (x * (i2 - i1))

def Perlin(x, y, gVecs):
    x = x % 1
    y = y % 1
    point = np.array([x, y])
    distances = [point - c for c in corners]
    influences = [np.dot(distances[i], np.array(gVecs[i])) for i in range(4)]
    u = Ease(x)
    v = Ease(y)
    a1 = Lerp(influences[0], influences[1], v)
    a2 = Lerp(influences[2], influences[3], v)
    average = Lerp(a1, a2, u)
    return average

def MakeGVectors(tiles):
    corners = [[(0,0) for j in range(tiles+1)] for i in range(tiles+1)]
    for i, line in enumerate(corners):
        for j in range(len(line)):
            corners[i][j] = random.choice(gVectorOptions)
            
    return corners

def MakePerlin(tiles, pointy=False):    
    grid = np.zeros((resolution, resolution))
    gVectors = MakeGVectors(tiles)
    
    for i, line in enumerate(grid):
        for j in range(len(line)):
            x = tiles * (i/resolution)
            y = tiles * (j/resolution)
            
            i1 = gVectors[m.floor(x)][m.floor(y)]
            i2 = gVectors[m.floor(x)][m.ceil(y)]
            i3 = gVectors[m.ceil(x)][m.floor(y)]
            i4 = gVectors[m.ceil(x)][m.ceil(y)]
                                                
            height = Perlin(x, y, [i1, i2, i3, i4])
            if pointy:
                height = 1 / (1 - height)
            grid[i, j] = height 
            
    return Normalize(grid)

def Normalize(array):
    mini = np.min(array)
    maxi = np.max(array)
    norm = (array - mini) / (maxi - mini)
    return norm

def ComplexPerlin(baseOctave, octaves, persistance, octaveChange):
    basePerlin = MakePerlin(baseOctave, True)
    if octaves > 1:
        for octave in range(1, octaves):
            basePerlin += octave * persistance[octave] * MakePerlin(baseOctave + (octave * octaveChange))
        
    return Normalize(basePerlin)

def RaiseFloor(array, floor):
    return Normalize(np.where(array > floor, array, floor))

grid = RaiseFloor(ComplexPerlin(3, 5, [1, 0.3, 0.09, 0.06, 0.02], 4), 0.1)

cmap = ListedColormap(["cornflowerblue", "paleturquoise", "palegoldenrod", "greenyellow", "mediumseagreen", "darkgrey", "whitesmoke"])

#plt.imshow(grid, cmap=cmap)

X = np.arange(-resolution/2, resolution/2, 1)
Y = np.arange(-resolution/2, resolution/2, 1)
X, Y = np.meshgrid(X, Y)
Z = grid

fig, axis = plt.subplots(subplot_kw={"projection": "3d"})
axis.set_zlim(bottom=-1, top=3)
surf = axis.plot_surface(X, Y, Z, cmap=cm.summer,
                       linewidth=0, antialiased=False)
plt.show()

    