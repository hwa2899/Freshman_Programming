# -*- coding: utf-8 -*-
"""
Created on Thu May 24 11:57:19 2018

@author: Ching
"""

import pygame
import random
class Ship():
    def __init__(self,pic,x,y,score):
        self.canvas=pygame.image.load(pic)
        self.canvas.convert()
        self.x=x
        self.y=y
        self.score=score
    def blit_me(self,screen):
        screen.blit(self.canvas,[self.x,self.y])
    def checkUserControl(self,left,right,up,down):
        keys=pygame.key.get_pressed()
        if keys[left]:
            self.x-=5
        if keys[right]:
            self.x+=5
        if keys[up]:
            self.y-=5
        if keys[down]:
            self.y+=5
class Bullet():
    def __init__(self,ship,speed):
        super().__init__()
        self.x=ship.x+25
        self.y=ship.y-10
        self.speed=speed
    def move(self,screen):
        self.y-=self.speed
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        pygame.draw.circle(screen,[r,g,b],[self.x,self.y],15)
        
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
        self.ship=Ship("ship.bmp",400,550,0)
        self.bullets=[]
    def run_game(self):
        while True:
            self.clock.tick(30)
            self.screen.fill([230,230,230])
            self.ship.blit_me(self.screen)
            self.ship.checkUserControl(pygame.K_LEFT,pygame.K_RIGHT,
                                       pygame.K_UP,pygame.K_DOWN)
            for b in self.bullets:
                if b.y <=0:
                    self.bullets.remove(b)
                else:
                    b.move(self.screen)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        newB=Bullet(self.ship,10)
                        self.bullets.append(newB)
myGame=Game(800,600)
myGame.run_game()
