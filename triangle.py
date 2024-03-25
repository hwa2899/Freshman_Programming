# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 00:02:52 2017

@author: Ching
"""

import turtle
t=turtle.Turtle()
t.ht()
t.speed(1)
colors=('orange','green','red','blue','pink')
points=[[-175,-125],[0,175],[175,-125]]

def mid(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2) #find midpoint
    
def tri(points, depth):
    t.pencolor(colors[depth%5])
    t.up()
    t.goto(points[0][0],points[0][1])
    t.down()
    t.goto(points[1][0],points[1][1])
    t.goto(points[2][0],points[2][1])
    t.goto(points[0][0],points[0][1])
    if depth>0:
        tri([points[0],mid(points[0],points[1]),
             mid(points[0],points[2])],depth-1)
        tri([points[1],mid(points[0],points[1]),
             mid(points[1],points[2])],depth-1)
        tri([points[2],mid(points[2],points[1]),
             mid(points[0],points[2])],depth-1)
tri(points,3)
turtle.done()