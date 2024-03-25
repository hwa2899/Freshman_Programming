# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 19:56:47 2017

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 23:29:56 2017

@author: user
"""

import turtle
myPen = turtle.Turtle()
myPen.ht()
myPen.speed(6)
colors=('orange','green','red','blue') 
points = [[-175.0,-125.0],[0.0,175.0],[175.0,-125.0]]

def mid(n1,n2):
    return [(n1[0]+n2[0])/2, (n1[1] + n2[1])/2] #find midpoint

def t(points,index):
    myPen.pencolor(colors[index])
    myPen.up()
    myPen.goto(points[0][0],points[0][1]) #就定位(第0點)
    myPen.down() #要開始畫了
    myPen.goto(points[1][0],points[1][1]) #從第0點畫到第1點
    myPen.goto(points[2][0],points[2][1])
    myPen.goto(points[0][0],points[0][1])

def g(n):
    if n==1:
        return 2
    else:
        return g(n-1)+3**n
    
def f(n):#要畫n層
    def r(p0,p1,p2):
        t([p0,mid(p0,p1),mid(p0,p2)],i%4)
        t([p1,mid(p1,p0),mid(p1,p2)],i%4)
        t([p2,mid(p2,p0),mid(p2,p1)],i%4)
        points.append(p0)
        points.append(mid(p0,p1))
        points.append(mid(p0,p2))
        points.append(p1)
        points.append(mid(p1,p0))
        points.append(mid(p1,p2))
        points.append(p2)
        points.append(mid(p2,p0))
        points.append(mid(p2,p1))
   
    for i in range(0,g(n)-1,3):
        r(points[i],points[i+1],points[i+2])

#執行        
f(6)
turtle.done()