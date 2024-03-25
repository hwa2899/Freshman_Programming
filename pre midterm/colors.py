# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:34:55 2018

@author: user
"""

import pygame
import random

pygame.init()
screen=pygame.display.set_mode([400,300])
pygame.display.set_caption("myFirstGame")
canvas=pygame.Surface(screen.get_size())
canvas.convert()
canvas.fill([255,255,255])

for x in range(0,400,40):
    for y in range(0,300,30):
        r=random.randint(0,255)    
        g=random.randint(0,255)
        b=random.randint(0,255)
        pygame.draw.rect(canvas,[r,g,b],[x,y,40,30])
    if x==400 and y==300:
        break




screen.blit(canvas,[0,0])
pygame.display.update()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()