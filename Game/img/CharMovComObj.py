# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:49:38 2019

@author: Vitor Bandeira
"""

import pygame
pygame.init()

#width=900
#height=600
win = pygame.display.set_mode((900,600))
pygame.display.set_caption("Projeto Final")
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.pulo = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        
    def draw(self,win):
        if self.walkCount +1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x,self.y))
            else:
                win.blit(walkLeft[0], (self.x,self.y))

class projetil(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 20 * facing
           
    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
     
def RestaurarJanela():
    win.blit(bg, (0,0))
    man.draw(win)
    for proj in projeteis:
        proj.draw(win)
    pygame.display.update()

man=player(1,510,64,64)# oq e esses 64
projeteis=[]
run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for proj in projeteis:
        if proj.x <900 and proj.x >0:
            proj.x += proj.vel
        else:
            projeteis.pop(projeteis.index(proj))

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(projeteis) <100:
            projeteis.append(projetil(round(man.x+man.width//2),round(man.y+man.height//2),6,(0,0,0),facing))
    
    if keys[pygame.K_a]:
        if man.x>man.vel:
            man.x -= man.vel
        man.left= True
        man.right= False
        man.standing = False
        if  keys[pygame.K_d]:
            if man.x < 900 - man.vel - man.width:
                man.x += man.vel
            man.left= False
            man.right= True
            man.standing= False
    elif  keys[pygame.K_d]:
        if man.x < 900 - man.vel - man.width:
            man.x += man.vel
        man.left= False
        man.right= True
        man.standing= False
        
        
    else:
        man.standing= True
        walkCount = 0
    
    if not(man.pulo):
        if keys[pygame.K_w]:
            man.pulo = True
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.jumpCount = 10
            man.pulo = False
            
    RestaurarJanela()
        
    
pygame.quit()