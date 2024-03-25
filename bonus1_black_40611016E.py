# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:43:52 2017

@author: Ching
"""

import turtle
t= turtle.Turtle()
t.ht()
t.speed(10)
turtle.bgcolor('black')
colors=('red','orange','yellow','green','blue','violet','purple') 
points = [[-175.0,-175.0],[-175.0,175.0],[175.0,175.0],[175.0,-175.0]]

def mid(n1,n2):
    return [(n1[0]+5*n2[0])/6, (n1[1] + 5*n2[1])/6] #find midpoint

def square(points,n):
    t.pencolor(colors[n%7])#to keep in range
    t.up()
    t.goto(points[0]) #就定位(第0點)
    t.down() #要開始畫了
    t.goto(points[1]) #從第0點畫到第1點
    t.goto(points[2])
    t.goto(points[3])
    t.goto(points[0])
    
    if n>0:
        square([mid(points[0],points[1]),mid(points[1],points[2]),
        mid(points[2],points[3]),mid(points[3],points[0]),
        mid(points[0],points[1])],n-1) #using recursion to draw next square


square(points,20)

turtle.done()