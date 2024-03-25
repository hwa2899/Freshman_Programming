# -*- coding: utf-8 -*-
"""
Created on Thu May 31 09:44:57 2018

@author: Ching
"""

import pygame
import random
class Alien():
    def __init__(self,pic,x,y):
        self.canvas=pygame.image.load(pic)
        self.canvas.convert()
        self.x=x
        self.y=y
    def blit_me(self,screen):
        screen.blit(self.canvas,[self.x,self.y])
    def moveRight(self):
        self.x+=10
    def moveLeft(self):
        self.x-=10
    def moveDown(self):
        self.y+=20
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
class Bullet1():
    def __init__(self,ship,speed):
        super().__init__()
        self.x=ship.x+20
        self.y=ship.y-10
        self.speed=speed
    def move(self,screen):
        self.y-=self.speed
        self.x-=self.speed
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        pygame.draw.circle(screen,[r,g,b],[self.x,self.y],15)
    def checkCollision(self,aliens):
        for opp in aliens:
            xDiff=self.x-opp.x
            yDiff=self.y-opp.y
            if abs(xDiff)<50 and abs(yDiff)<50:
                aliens.remove(opp)
class Bullet2():
    def __init__(self,ship,speed):
        super().__init__()
        self.x=ship.x+40
        self.y=ship.y-10
        self.speed=speed
    def move(self,screen):
        self.y-=self.speed
        self.x+=self.speed
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        pygame.draw.circle(screen,[r,g,b],[self.x,self.y],15)
    def checkCollision(self,aliens):
        for opp in aliens:
            xDiff=self.x-opp.x
            yDiff=self.y-opp.y
            if abs(xDiff)<50 and abs(yDiff)<50:
                aliens.remove(opp)
class Bullet3():
    def __init__(self,ship,speed):
        super().__init__()
        self.x=ship.x+30
        self.y=ship.y-10
        self.speed=speed
    def move(self,screen):
        self.y-=self.speed
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        pygame.draw.circle(screen,[r,g,b],[self.x,self.y],15)
    def checkCollision(self,aliens):
        for opp in aliens:
            xDiff=self.x-opp.x
            yDiff=self.y-opp.y
            if abs(xDiff)<50 and abs(yDiff)<50:
                aliens.remove(opp)
class bullet4():
    def __init__(self,ship,speed):
        super().__init__()
        self.x=ship.x+30
        self.y=ship.y-10
        self.speed=speed
    def move(self,screen):
        self.y-=self.speed
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        pygame.draw.circle(screen,[r,g,b],[self.x,self.y],400)
    def checkCollision(self,aliens):
        for opp in aliens:
            xDiff=self.x-opp.x
            yDiff=self.y-opp.y
            if abs(xDiff)<400 and abs(yDiff)<400:
                aliens.remove(opp)
class Game():
    def __init__(self,w,h):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.screen=pygame.display.set_mode([w,h])
        pygame.display.set_caption("galaxy defender")
        pygame.mixer.init()
        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play(-1)
        self.sound=pygame.mixer.Sound("coin.wav")
        
        self.ship=Ship("ship.bmp",400,550,0)
        self.bullets=[]
        self.aliens=[]
        for i in range(6):
            self.aliens.append(Alien("alien.bmp",100+100*i,20))
        self.aliensDir=1
    def aliens_move(self):
        if self.aliensDir==1 and len(self.aliens)>0:
            num=len(self.aliens)-1
            if self.aliens[num].x>870:
                self.aliensDir*=-1
                for a in self.aliens:
                    a.moveDown()
            else:
                for a in self.aliens:
                    a.moveRight()
        elif self.aliensDir==-1 and len(self.aliens)>0:
            if self.aliens[0].x<30:
                self.aliensDir*=-1
                for a in self.aliens:
                    a.moveDown()
            else:
                for a in self.aliens:
                    a.moveLeft()
    def run_game(self):
        while True:
            self.clock.tick(30)
            self.screen.fill([230,230,230])
            self.ship.blit_me(self.screen)
            self.ship.checkUserControl(pygame.K_LEFT,pygame.K_RIGHT,
                                       pygame.K_UP,pygame.K_DOWN)
            self.aliens_move()
            for a in self.aliens:
                a.blit_me(self.screen)
            for b in self.bullets:
                b.move(self.screen)
                b.checkCollision(self.aliens)
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
                        nb=Bullet3(self.ship,10)
                        self.bullets.append(nb)
                    if event.key==pygame.K_a:
                        nb=bullet4(self.ship,10)
                        self.bullets.append(nb)
                    if event.key==pygame.K_f:
                        newB=Bullet1(self.ship,10)
                        self.bullets.append(newB)
                        newbullet=Bullet2(self.ship,10)
                        self.bullets.append(newbullet)
                        newb=Bullet3(self.ship,10)
                        self.bullets.append(newb)
myGame=Game(960,640)
myGame.run_game()
