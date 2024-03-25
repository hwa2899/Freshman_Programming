# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:26:00 2018

@author: user
"""

import pygame
pygame.init()
screen=pygame.display.set_mode([600,400])
pygame.display.set_caption("myFirstGame")
clock=pygame.time.Clock()

canvas=pygame.Surface(screen.get_size())
canvas.convert()
canvas.fill([255,255,255])
x=200
y=150

running=True
while running:
    clock.tick(30)
    pygame.draw.rect(canvas,[255,0,0],[x,y,30,30])
    screen.blit(canvas,[0,0])
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                print("left")
                pygame.draw.rect(canvas,[255,255,255],[x,y,30,30])
                x-=10
            elif event.key==pygame.K_RIGHT:
                print("right")
                pygame.draw.rect(canvas,[255,255,255],[x,y,30,30])
                x+=10
            elif event.key==pygame.K_DOWN:
                print("down")
                pygame.draw.rect(canvas,[255,255,255],[x,y,30,30])
                y+=10
            elif event.key==pygame.K_UP:
                print("up")
                pygame.draw.rect(canvas,[255,255,255],[x,y,30,30])
                y-=10
            elif event.key==pygame.K_w:
                print("up")
                y-=10
            elif event.key==pygame.K_a:
                print("left")
                x-=10
            elif event.key==pygame.K_s:
                print("down")
                y+=10
            elif event.key==pygame.K_d:
                print("right")
                x+=10
        elif event.type==pygame.QUIT:
            running=False
pygame.quit()