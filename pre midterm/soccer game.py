# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 09:34:43 2018

@author: user
"""

import pygame
pygame.init()
screen=pygame.display.set_mode([400,240])
pygame.display.set_caption("Soccer game")
clock=pygame.time.Clock()

canvas=pygame.image.load("bg.png")
canvas.convert()

#player 1 starting point
player1=pygame.image.load("sprite1.png")
player1.convert()
x=200
y=150
#player 2 starting point
player2=pygame.image.load("sprite2.png")
player2.convert()
a=100
b=200
#coin starting point
coin=pygame.image.load("coin.png")
coin.convert()
xball=300
yball=200

def boom(x1,y1,x2,y2):
    xdiff=x1-x2
    ydiff=y1-y2
    if abs(xdiff)<20 and abs(ydiff)<20:
        x1+=xdiff*2
        x2-=xdiff*3
        y1+=ydiff*2
        y2-=ydiff*3
    return True
running=True
while running:
    clock.tick(30)
    #canvas.fill([255,255,255])
    #pygame.draw.rect(canvas,[255,0,0],[x,y,30,30])
    #pygame.draw.circle(canvas,[255,0,255],[xball,yball],10)
    screen.blit(canvas,[0,0])
    screen.blit(player1,[x,y])
    screen.blit(player2,[a,b])
    screen.blit(coin,[xball,yball])
    pygame.display.update()
    
    keys=pygame.key.get_pressed()
    #left, right, down, up player 1 movement
    if keys[pygame.K_LEFT]:
        x-=10
    elif keys[pygame.K_RIGHT]:
        x+=10
    elif keys[pygame.K_DOWN]:
        y+=10
    elif keys[pygame.K_UP]:
        y-=10
    #w,s,d,a player 2 movement
    if keys[pygame.K_w]:
        b-=10
    elif keys[pygame.K_s]:
        b+=10
    elif keys[pygame.K_a]:
        a-=10
    elif keys[pygame.K_d]:
        a+=10
    boom(x,y,xball,yball)   
#    xdiff=x-xball
#    ydiff=y-yball
#    if abs(xdiff)<20 and abs(ydiff)<20:
#        x+=xdiff*2
#        xball-=xdiff*3
#        y+=ydiff*2
#        yball-=ydiff*3
    boom(a,b,xball,yball)
#    adiff=a-xball
#    bdiff=b-yball
#    if abs(adiff)<20 and abs(bdiff)<20:
#        a+=adiff*2
#        xball-=adiff*3
#        b+=bdiff*2
#        yball-=bdiff*3
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()