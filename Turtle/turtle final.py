# -*- coding: utf-8 -*-
"""
Created on Tue May  1 19:36:46 2018

@author: Ching
"""

import pygame
import random 
import time

global screen, canvas, clock, sound
global player1, x, y, score1
global player2,a,b,score2
global star, xstar, ystar
global rock, xrock, yrock
global winner

def initgame():
    global screen, canvas, clock, sound
    global player1, x, y, score1,easter1
    global player2,a,b,score2,easter2
    global star,xstar,ystar,starno
    global rock, xrock, yrock, rockno,total
    global speed1, speed2
    pygame.init()
    screen=pygame.display.set_mode([1000,550])
    pygame.display.set_caption("Under the sea")
    clock=pygame.time.Clock()

    canvas=pygame.image.load("wateredit.png")
    canvas.convert()

    #player 1 starting point
    player1=pygame.image.load("turtle.png")
    player1.convert()
    x=585
    y=225
    score1=0
    easter1=0
    #player 2 starting point
    player2=pygame.image.load("turtle2.png")
    player2.convert()
    a=195
    b=225
    score2=0
    easter2=0
    #------------------------------------
    #coin starting point
    star=[]
    xstar=[]
    ystar=[]
    starno=random.randrange(13,34,2)
    total=starno
    count=0
    while count<starno:
        star.append(pygame.image.load("starfish.png"))
        xstar.append(random.randrange(0,950))
        ystar.append(random.randrange(0,500))
        count+=1
    #-------------------------------------
    #rock starting point
    rock=[]
    xrock=[]
    yrock=[]
    rockno=random.randint(3,10)
    rcount=0
    while rcount<rockno:
        rock.append(pygame.image.load("rock.png"))
        xrock.append(random.randrange(0,950))
        yrock.append(random.randrange(0,500))
        rcount+=1
    #--------------------------------------
    speed1=3
    speed2=3
    #--------------------------------------
    pygame.mixer.init()
    pygame.mixer.music.load("Master_of_the_Feast.ogg")
    pygame.mixer.music.play(-1)
    sound=pygame.mixer.Sound("Water_Drop.wav")
def win():
    global can
    can=pygame.image.load("you-win.png")
    can.convert()
    screen.blit(canvas,[0,0])
    screen.blit(can,[0,0])
    if score1>=5:
        screen.blit(player1,[585,225])
    else:
        screen.blit(player2,[195,225])
    pygame.display.update()
   
    
def boom(x1,y1,x2,y2):
    global xdiff
    global ydiff
    xdiff=x1-x2
    ydiff=y1-y2
    if abs(xdiff)<50 and abs(ydiff)<40:
        return True
    else:
        return False

def controls():
    global a, b, x, y,speed1,speed2
    clock.tick(30)
    keys=pygame.key.get_pressed()
    #left, right, down, up player 1 movement
    if keys[pygame.K_LEFT]:
        if x>=0:
            x-=speed1
    if keys[pygame.K_RIGHT]:
        if x<=950:
            x+=speed1
    if keys[pygame.K_DOWN]:
        if y<=500:
            y+=speed1
    if keys[pygame.K_UP]:
        if y>=0:
            y-=speed1
    #w,s,d,a player 2 movement
    if keys[pygame.K_w]:
        if b>=0:
            b-=speed2
    if keys[pygame.K_s]:
        if b<=500:
            b+=speed2
    if keys[pygame.K_a]:
        if a>=0:
            a-=speed2
    if keys[pygame.K_d]:
        if a<=950:
            a+=speed2
            
def updatescreen():
    global screen, canvas, clock, sound
    global player1, x, y
    global player2,a,b
    global star, xstar,ystar,starno
    global rock, xrock, yrock, rockno
    screen.blit(canvas,[0,0])
    screen.blit(player1,[x,y])
    screen.blit(player2,[a,b])
    for i in range(starno):
        screen.blit(star[i],[xstar[i],ystar[i]])
    for i in range(rockno):
        screen.blit(rock[i], [xrock[i],yrock[i]])
    #see points
    font=pygame.font.Font("DFTTNC5.TTC",14)
    text1=font.render(str(score1),True,[255,255,0])
    text2=font.render(str(score2),True,[255,255,0])
    screen.blit(text1,[x-10,y-10])
    screen.blit(text2,[a-10,b-10])
    pygame.display.update()

def easteregg():
    global speed1,speed2
    
def checkObjectCollision():
    global a,b, x, y, score1,easter1,easter2,score2,sound
    global xstar, ystar,starno
    global xrock, yrock
    global speed1,speed2
    if boom(x,y,a,b):
        xdiff=x-a
        ydiff=y-b
        x+=xdiff*2
        a-=xdiff*2
        y+=ydiff*2
        b-=ydiff*2
    for i in range(starno):
        if boom(x,y,xstar[i],ystar[i]):
            sound.play()
            xstar[i]=800
            ystar[i]=800
            score1+=1
            easter1=0
        if boom(a,b,xstar[i],ystar[i]):
            sound.play()
            xstar[i]=800
            ystar[i]=800
            score2+=1
            easter2=0
    for j in range(rockno):
        if boom(x,y,xrock[j],yrock[j]):
            xrock[j]=random.randrange(50,700)
            yrock[j]=random.randrange(50,400)
            star.append(pygame.image.load("starfish.png"))
            xstar.append(random.randrange(0,950))
            ystar.append(random.randrange(0,500))
            starno+=1
            score1-=1
            easter1+=1
            if easter1>=5:
                speed1+=5
#                score1+=5
#                starno-=5
                easter1=0
        if boom(a,b,xrock[j],yrock[j]):
            xrock[j]=random.randrange(50,700)
            yrock[j]=random.randrange(50,400)
            star.append(pygame.image.load("starfish.png"))
            xstar.append(random.randrange(0,950))
            ystar.append(random.randrange(0,500))
            starno+=1
            score2-=1
            easter2+=1
            if easter2>=5:
                speed2+=5
#                score2+=5
#                starno-=5
                easter2=0

initgame()      
running=True
while running:
    controls()
    updatescreen()
    checkObjectCollision()
    if score1+score2==total:
        win()
        time.sleep(5)
        break
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()