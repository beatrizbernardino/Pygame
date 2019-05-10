import pygame
from os import path
pygame.init()
import random

width=560
height=520
img_dir = path.join(path.dirname(__file__), 'img')
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Projeto Final")
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
plat=pygame.image.load("grassMid.png")
clock = pygame.time.Clock()
all_sprites=pygame.sprite.Group()
#width=500
#height=500


black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(200,200,255)
roxo=(180,0,200)
verdeagua=(0,180,255)





class player(pygame.sprite.Sprite):
    
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
        
    def update(self,win):
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
                
                
                


              
class Platform(pygame.sprite.Sprite):

    def __init__(self,x,y,w,h):
        pygame.sprite.Sprite.__init__(self)
        
        #player_img=pygame.image.load(path.join(img_dir,'grassMid.png')).convert()
        self.image=plat
        
        self.image=pygame.transform.scale(self.image,(w,h))
        
        self.rect=self.image.get_rect()
        
        self.rect.centerx=x
        self.rect.bottom=y
        self.image.set_colorkey(white)
   
    
    
p1=Platform(width/2,height-400,50,20)
 
p2=Platform(width/2,height-400,100,20)  
#p1=Platform(width/2,height-400,500,100)
all_sprites.add(p1)
#p2=Platform(100,height-200,250,100)
all_sprites.add(p2)
#p3=Platform(width-100,height-200,250,100)
#p4=Platform(width/2,height,width,50)
#all_sprites.add(p3)
#all_sprites.add(p4)                
 
class Enemy(pygame.sprite.Sprite):
    def __init__(self): #a funçao que define qual codigo sera executado sempre que um novo objeto desse tipo for criado
        pygame.sprite.Sprite.__init__(self)#inicializador de classe
        
        enemy_img = pygame.image.load(path.join('p3_jump.png')).convert()
        self.image = enemy_img
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect() #rect é retangulo
        self.rect.y = random.randrange(0,height)
        self.rect.x = random.randrange(0,8)
        self.speedx =random.randrange(2,15)
        self.speedy =random.randrange(1,2)
        
    def update(self):
        if(self.rect.x - 16 > width/2):
           self.rect.x -= self.speedx
        
        elif(self.rect.x + 16 < width/2):
           self.rect.x += self.speedx
       
        if(self.rect.y - 16 > height/2):
           self.rect.y -= self.speedy
        
        elif(self.rect.y + 16 < height/2):
           self.rect.y += self.speedy


p=pygame.sprite.Group()      

count=0
jogando=True





class projetil(pygame.sprite.Sprite):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 20 * facing
        
    def update(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y), self.radius)

def RestaurarJanela():
    win.blit(bg, (0,0))
    man.update(win)
    for proj in projeteis:
        proj.update(win)
    pygame.display.update()
    all_sprites.update()
    all_sprites.draw(win)
   

man=player(300,300,64,64)# oq e esses 64
projeteis=[]
run = True


while run:
    clock.tick(27)
    
    if count==6:
        enemy= Enemy()
        all_sprites.add(enemy)
        p.add(enemy)
        count=0


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
    
    if keys[pygame.K_a] and man.x>man.vel:
        man.x -= man.vel
        man.left= True 
        man.right= False
        man.standing = False
    elif keys[pygame.K_d] and man.x < 500 - man.vel - man.width:
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
    win.fill(white)        
    RestaurarJanela()         
    count+=1    
    
pygame.quit()
quit()