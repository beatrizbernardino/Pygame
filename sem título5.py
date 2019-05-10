# -*- coding: utf-8 -*-
"""
Created on Thu May  9 19:01:36 2019

@author: julia
"""

import pygame
import os
import random


WIDTH=500 
HEIGHT=500 
FPS=30 


pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("nosso jogo")
clock=pygame.time.Clock()
all_sprites=pygame.sprite.Group()

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
player_img = pygame.image.load(os.path.join(img_folder, 'p3_jump.png')).convert()


AZUL=(0,180,255)
ROSA=(255,0,150) 
BLACK=(0,0,0)
WHITE=(255,255,255)


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect() 
        self.rect.y = y 
        self.rect.x = x
        self.speedx = 10 
        self.speedy = 10 
        
    def update(self):


       
        if(self.rect.x - 16 > WIDTH/2):
           self.rect.x -= self.speedx
        
        elif(self.rect.x + 16 < WIDTH/2):
           self.rect.x += self.speedx
       
        if(self.rect.y - 16 > HEIGHT/2):
           self.rect.y -= self.speedy
        
        elif(self.rect.y + 16 < HEIGHT/2):
           self.rect.y += self.speedy

       


p=pygame.sprite.Group()
  
      
running=True 
count=0
while running:
    clock.tick(FPS)
    
    if count == 30:
        
        player= Player(random.randrange(0,WIDTH), random.randrange(0,HEIGHT))
        all_sprites.add(player)
        p.add(player)
        count=0
    
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    all_sprites.update()        
    screen.fill(AZUL) 
    all_sprites.draw(screen) 
    pygame.display.flip()
    count+=1
pygame.quit()
quit()
    
