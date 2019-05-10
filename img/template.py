import pygame
from os import path 
import random

img_dir = path.join(path.dirname(__file__),)

width=500
height=500
fps=30 # frames per second



black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(200,200,255)
roxo=(180,0,200)
verdeagua=(0,180,255)


pygame.init() 
pygame.mixer.init() #som
win=pygame.display.set_mode((width,height)) #dimensões da tela
pygame.display.set_caption("asteroides")   #nome do jogo
clock=pygame.time.Clock() #relógio que garante o fps
all_sprites=pygame.sprite.Group()




class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(verdeagua)
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.rect.bottom = height-50
        self.speedx =0
     
    def update(self):
        self.rect.x+=self.speedx
        
        if self.rect.right> width:
            self.rect.right = width
        if self.rect.left<0:
            self.rect.left=0
 



class Platform(pygame.sprite.Sprite):

    def __init__(self,x,y,w,h, tipo):
        pygame.sprite.Sprite.__init__(self)
        filename = ''
        if tipo == 'left':
            filename = 'grassCliffLeftAlt.png'
        elif tipo == 'right':
            filename = 'grassCliffRightAlt.png'
        elif tipo== "middle":
           filename='grassMid.png'
        player_img=pygame.image.load(path.join(img_dir,filename)).convert()
        self.image=player_img
        
        self.image=pygame.transform.scale(player_img,(w,h))
        
        self.rect=self.image.get_rect()
        
        self.rect.centerx=x
        self.rect.bottom=y
        self.image.set_colorkey(black)
   
    
for i in range (4):
    
    if i==0:
        p1=Platform(30-width/2+i*50,height-400,50,20,'left')
    elif i==3:
        p1=Platform(width/2+i*50,height-400,50,20,'right')
    else:
        p1=Platform(width/2+i*50,height-400,50,20,'middle')
        
    all_sprites.add(p1)
    

    
#player_img=pygame.image.load(path.join(img_dir,'grassCliffLeftAlt.png')).convert()    
#p2=Platform(width/2+50,height-350,50,20)
        
player=Player()
all_sprites.add(player)



#p1=Platform(width/2,height-400,500,100)
#all_sprites.add(p1)
#p2=Platform(100,height-200,250,100)
#all_sprites.add(p2)
#p3=Platform(width-100,height-200,250,100)
#p4=Platform(width/2,height,width,50)
#all_sprites.add(p3)
#all_sprites.add(p4)





#class Enemy(pygame.sprite.Sprite):
   # def __init__(self): #a funçao que define qual codigo sera executado sempre que um novo objeto desse tipo for criado
       # pygame.sprite.Sprite.__init__(self)#inicializador de classe
        
       # enemy_img = pygame.image.load(path.join(img_dir, 'p3_jump.png')).convert()
        #self.image = enemy_img
        #self.image.set_colorkey(black)
        #self.rect=self.image.get_rect() #rect é retangulo
        #self.rect.y = random.randrange(0,height)
        #self.rect.x = random.randrange(0,8)
        #self.speedx =random.randrange(2,15)
        #self.speedy =random.randrange(1,2)
        
   # def update(self):
    #    if(self.rect.x - 16 > width/2):
     #      self.rect.x -= self.speedx
        
     #   elif(self.rect.x + 16 < width/2):
      #     self.rect.x += self.speedx
       
       # if(self.rect.y - 16 > height/2):
        #   self.rect.y -= self.speedy
        
        #elif(self.rect.y + 16 < height/2):
         #  self.rect.y += self.speedy


#p=pygame.sprite.Group()      










count=0
jogando=True

while jogando:
    
    clock.tick(fps)
    
    #if count==6:
     #   enemy= Enemy()
     #   all_sprites.add(enemy)
       # p.add(enemy)
      #  count=0

    
    for event in pygame.event.get():
        
        if event.type== pygame.QUIT:
            jogando=False
            
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                player.speedx = -8
            if event.key == pygame.K_RIGHT:
                player.speedx = 8
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.speedx =0
            if event.key == pygame.K_RIGHT:
                player.speedx =0
                
    win.fill(blue)            
    all_sprites.update()
    all_sprites.draw(win)
    pygame.display.flip()
    count+=1
    
pygame.quit()
quit()

