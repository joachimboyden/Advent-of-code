# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 14:24:22 2024

@author: joach
"""
import re
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

inputFile = open('input.txt', 'r')
testFile = open('test.txt', 'r')

file = inputFile.readlines()
data = [list(map(int, re.findall("-*[0-9]+", line))) for line in file]

X, Y = 101, 103

def FindFinalPosition(steps, robot):
    xPosition, yPosition, xVelocity, yVelocity = robot[0], robot[1], robot[2], robot[3]
    xFinal = ((steps * xVelocity) + xPosition) % X
    yFinal = ((steps * yVelocity) + yPosition) % Y
    return xFinal, yFinal

def FindQuadrant(x, y):
    if 0 <= x < int(X/2) and 0 <= y < int(Y/2):
        return 0
    elif int(X/2) < x <= X and 0 <= y < int(Y/2):
        return 1
    elif int(X/2) < x <= X and int(Y/2) < y <= Y:
        return 2
    elif 0 <= x < int(X/2) and int(Y/2) < y < Y:
        return 3
    else:
        return 4
    
def RunRobotSim(steps):
    robotsInQuads = [0,0,0,0,0]
    for robot in data:
        x, y = FindFinalPosition(steps, robot)
        robotsInQuads[FindQuadrant(x, y)] += 1
        
    return robotsInQuads[0]*robotsInQuads[1]*robotsInQuads[2]*robotsInQuads[3]

def MakeRoom(steps):
    room = np.zeros((Y,X))
    for robot in data:
        x, y = FindFinalPosition(steps, robot)
        room[y, x] = 1
        
    return room
    
def ShowRoom(step):
    figure, axis = plt.subplots()
    axis.imshow(MakeRoom(step))
            
fig = plt.figure()
room = MakeRoom(0)
im=plt.imshow(room, interpolation='none')

def init():
    im.set_data(room)
    return [im]

# animation function.  This is called sequentially
def animate(i):
    room=im.get_array()
    room=MakeRoom(i+6620)    
    im.set_array(room)
    print(i+6620)
    return [im]
        
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1, interval=20, blit=True)

plt.show()