# -*- coding: utf-8 -*-
"""
Created on Thu May 10 09:18:33 2018

@author: Ching
"""
import pygame
import random
import time
#---------------------------------------
#設定
pygame.init()
screen=pygame.display.set_mode([400,240])
pygame.display.set_caption("coin class")
clock=pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
sound=pygame.mixer.Sound("coin.wav")
#----------------------------------------
#道具類別
class Object():
    def __init__(self,pic,x,y):
        self.canvas=pygame.image.load(pic)
        self.canvas.convert()
        self.x=x
        self.y=y
    def blit_me(self,screen):
        screen.blit(self.canvas,[self.x,self.y])
#---------------------------------------
#玩家類別    
class player():
    def __init__(self,pic,x,y,score):
        self.canvas=pygame.image.load(pic)
        self.canvas.convert()
        self.x=x
        self.y=y
        self.score=score
    def blit_me(self,screen):
        screen.blit(self.canvas,[self.x,self.y])
        font=pygame.font.Font("DFTTNC5.TTC",14)
        txtScore=font.render(str(self.score),True,[255,255,0])
        screen.blit(txtScore,[self.x-10,self.y-10]) 
    def control(self,up,down,left,right):
        keys=pygame.key.get_pressed()
        if keys[up]:
            self.y-=5
        if keys[down]:
            self.y+=5
        if keys[left]:
            self.x-=5
        if keys[right]:
            self.x+=5
    def isCollidePlayer(self,opp):
        xDiff=self.x-opp.x
        yDiff=self.y-opp.y
        if abs(xDiff)<30 and abs(yDiff)<30:
            self.x+=xDiff*2
            self.y+=yDiff*2
            opp.x-=xDiff*2
            opp.y-=yDiff*2
    def isCollideCoin(self,opp,sound):
        xDiff=self.x-opp.x
        yDiff=self.y-opp.y
        if abs(xDiff)<30 and abs(yDiff)<30:
            opp.x=random.randrange(50,350)
            opp.y=random.randrange(50,200)
            self.score+=1
            sound.play()
            time.sleep(0.5)
   
bg=Object("bg.png",0,0)
coin=Object("coin.png",200,50)
p1=player("sprite1.png",100,150,0)
p2=player("sprite2.png",300,150,0)
#-------------------------------------------
#主程式
running=True
while running:
    bg.blit_me(screen)
    p1.control(pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d)
    p2.control(pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT)
    p1.isCollidePlayer(p2)
    p1.isCollideCoin(coin,sound)
    p2.isCollideCoin(coin,sound)
    p1.blit_me(screen)
    p2.blit_me(screen)
    coin.blit_me(screen)
    pygame.display.update()
    clock.tick(30)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()