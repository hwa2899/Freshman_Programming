# -*- coding: utf-8 -*-
"""
Created on Thu May 24 11:14:24 2018

@author: Ching
"""

import pygame 
import time
import random
class obj():
    def __init__(self,pic,x,y):
        self.canvas=pygame.image.load(pic)
        self.canvas.convert()
        self.x=x
        self.y=y
    def blit_me(self,screen):
        screen.blit(self.canvas,[self.x,self.y])
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
        txtscore=font.render(str(self.score),True,[255,255,0])
        screen.blit(txtscore,[self.x-10,self.y-10])
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
    def collideplayer(self,opp):
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
class Game():
    def __init__(self,w,h):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.screen=pygame.display.set_mode([w,h])
        pygame.display.set_caption("mySecondGame")
        pygame.mixer.init()
        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play(-1)
        self.sound=pygame.mixer.Sound("coin.wav")
        self.bg=obj("bg.png",0,0)
        self.p1=player("sprite1.png",100,150,0)
        self.p2=player("sprite2.png",300,150,0)
        self.coin=obj("coin.png",200,50)
    def run_game(self):
        while True:
            self.clock.tick(30)
            self.bg.blit_me(self.screen)
            self.p1.control(pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d)
            self.p2.control(pygame.K_UP,pygame.
                                 K_DOWN,pygame.K_LEFT,pygame.K_RIGHT)
            self.p1.collideplayer(self.p2)
            self.p1.isCollideCoin(self.coin,self.sound)
            self.p2.isCollideCoin(self.coin,self.sound)
            self.p1.blit_me(self.screen)
            self.p2.blit_me(self.screen)
            self.coin.blit_me(self.screen)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
myGame=Game(400,240)
myGame.run_game()