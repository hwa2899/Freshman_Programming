# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import turtle
t=turtle.Turtle()
t.speed(10)
p=[-60,-60] #p rep. points
l=120 #length rep. square length
turtle.bgcolor('black')
t.color('blue','yellow')

def ds(p,l):
    t.up()
    t.goto(p[0]-l,p[1]-l)
    t.down()
    for i in range(4):
        t.forward(3*l)
        t.left(90)
def square(p,l,n): #a represents which point
    t.begin_fill()
    t.up()
    t.goto(p)
    t.down()
    for i in range(4):
        t.forward(l)
        t.left(90)
    t.end_fill()
    if n>0:
        square([p[0]-(2/3)*l,p[1]+(4/3)*l],l/3,n-1)
        square([p[0]+(1/3)*l,p[1]+(4/3)*l],l/3,n-1)
        square([p[0]+(4/3)*l,p[1]+(4/3)*l],l/3,n-1)
        square([p[0]-(2/3)*l,p[1]+(1/3)*l],l/3,n-1)
        square([p[0]+(4/3)*l,p[1]+(1/3)*l],l/3,n-1)
        square([p[0]-(2/3)*l,p[1]-(2/3)*l],l/3,n-1)
        square([p[0]+(1/3)*l,p[1]-(2/3)*l],l/3,n-1)
        square([p[0]+(4/3)*l,p[1]-(2/3)*l],l/3,n-1)
    
#def sad(x):
#    if x==1:
#        return 1
#    else:
#        return sad(x-1)+8**(x-1)
#def d(n):
#    if n==1:
#        square(0,120)
#    else:
#        d(n-1)
#        for i in range(sad(n-1),sad(n)):
#            square(i,(1/3)**(n-1)*120)

ds(p,l)
square(p,l,3)
turtle.done()