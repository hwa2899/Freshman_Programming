# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 10:02:34 2018

@author: user
"""

import pygame
import random 
import time

global screen, canvas, clock, sound
global player1, x, y, score1
global player2,a,b,score2
global coin, xball, yball

def initgame():
    global screen, canvas, clock, sound
    global player1, x, y, score1
    global player2,a,b,score2
    global coin, xball, yball
    pygame.init()
    screen=pygame.display.set_mode([400,240])
    pygame.display.set_caption("Soccer game")
    clock=pygame.time.Clock()

    canvas=pygame.image.load("bg.png")
    canvas.convert()

    #player 1 starting point
    player1=pygame.image.load("sprite1.png")
    player1.convert()
    x=300
    y=120
    score1=0
    #player 2 starting point
    player2=pygame.image.load("sprite2.png")
    player2.convert()
    a=100
    b=120
    score2=0
    #coin starting point
    coin=pygame.image.load("coin.png")
    coin.convert()
    xball=200
    yball=120
    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)
    sound=pygame.mixer.Sound("coin.wav")

def boom(x1,y1,x2,y2):
    global xdiff
    global ydiff
    xdiff=x1-x2
    ydiff=y1-y2
    if abs(xdiff)<20 and abs(ydiff)<20:
#        x1+=xdiff*2
#        x2-=xdiff*3
#        y1+=ydiff*2
#        y2-=ydiff*3
        return True
    else:
        return False

def controls():
    global a, b, x, y, score1
    clock.tick(30)
    keys=pygame.key.get_pressed()
    #left, right, down, up player 1 movement
    if keys[pygame.K_LEFT]:
        if x>=0:
            x-=10
    if keys[pygame.K_RIGHT]:
        if x<=380:
            x+=10
    if keys[pygame.K_DOWN]:
        if y<=220:
            y+=10
    if keys[pygame.K_UP]:
        if y>=0:
            y-=10
    #w,s,d,a player 2 movement
    if keys[pygame.K_w]:
        if b>=0:
            b-=10
    if keys[pygame.K_s]:
        if b<=220:
            b+=10
    if keys[pygame.K_a]:
        if a>=0:
            a-=10
    if keys[pygame.K_d]:
        if a<=380:
            a+=10
            
def updatescreen():
    global screen, canvas, clock, sound
    global player1, x, y
    global player2,a,b
    global coin, xball, yball
    screen.blit(canvas,[0,0])
    screen.blit(player1,[x,y])
    screen.blit(player2,[a,b])
    screen.blit(coin,[xball,yball])
    #see points
    font=pygame.font.Font("DFTTNC5.TTC",14)
    text1=font.render(str(score1),True,[255,255,0])
    text2=font.render(str(score2),True,[255,255,0])
    screen.blit(text1,[x-10,y-10])
    screen.blit(text2,[a-10,b-10])
    pygame.display.update()

def checkObjectCollision():
    global a,b, x, y, score1,score2,sound
    global xball, yball
    if boom(x,y,a,b):
        xdiff=x-a
        ydiff=y-b
        x+=xdiff*2
        a-=xdiff*2
        y+=ydiff*2
        b-=ydiff*2
        
    if boom(x,y,xball,yball):
        sound.play()
        xball=random.randrange(50,350)
        yball=random.randrange(50,200)
        time.sleep(1)
        score1+=1
        
    if boom(a,b,xball,yball):
        sound.play()
        xball=random.randrange(50,350)
        yball=random.randrange(50,200)
        time.sleep(1)
        score2+=1  

initgame()      
running=True
while running:
    controls()
    updatescreen()
    checkObjectCollision()
#    if score1>=5 or score2>=5:
#        running=False
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()