# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 09:52:47 2018

@author: user
"""

import pygame
pygame.init()
screen=pygame.display.set_mode([600,400])
pygame.display.set_caption("myfirstGame")

canvas=pygame.Surface(screen.get_size())
canvas.convert()
canvas.fill([255,255,255])
pygame.draw.line(canvas,[255,0,0],[50,50],[100,50])
pygame.draw.circle(canvas,[0,255,255],[150,50],30)
pygame.draw.rect(canvas,[0,0,255],[200,50,30,50])

screen.blit(canvas,[0,0])
pygame.display.update()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()