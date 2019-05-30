# -*- coding: utf-8 -*-
"""
Created on Thu May 30 19:03:03 2019

@author: Vitor Bandeira
"""

import pygame
pygame.init()
screen = pygame.display.set_mode((900,600))
clock = pygame.time.Clock()

counter, text = 5, '5'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: 
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'Acabou!'
        if event.type == pygame.QUIT: break
    else:
        screen.fill((255, 255, 255))
        screen.blit(font.render(text, True, (190,2,20)), (400,50 ))
        pygame.display.flip()
        clock.tick(60)
        continue
    break