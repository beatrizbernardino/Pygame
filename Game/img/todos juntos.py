
import random
import pygame
from os import path
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

WIDTH=600
HEIGHT=600
width=900
height=600
win = pygame.display.set_mode((900,600))
pygame.display.set_caption("Projeto Final")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
pew = pygame.image.load("tiro.png").convert_alpha()
char  = pygame.image.load('standing.png')
pew = pygame.image.load("tiro.png").convert_alpha()
snd_dir = path.join(path.dirname(__file__))
som=pygame.mixer.Sound(path.join(snd_dir, 'pew.wav'))
boom=pygame.mixer.Sound(path.join(snd_dir, 'expl6.wav'))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
pygame.transform.scale(bg,(900,600))
clock = pygame.time.Clock()




player_img = pygame.image.load('R8E.png') 
all_sprites=pygame.sprite.Group()
playergroup = pygame.sprite.Group()
enemygroup = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_platforms=pygame.sprite.Group()
img_dir=path.join(path.dirname(__file__))

class player(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image= char
        self.image= pygame.transform.scale(char,(64,64))
        self.image.set_colorkey((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.x=1
        self.rect.y=510
        self.speedx=0
        self.speedy=0
        self.pulo = False
        self.vel = 10
        self.jumpCount = 10
        self.direita = False
        self.esquerda = False
    def update(self):
        self.rect.x += self.speedx
        self.rect.y+=self.speedy
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0

class enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey((0,0,0))
        self.rect=self.image.get_rect() 
        self.rect.y = y 
        self.rect.x = x
        self.speedx = 5 
        self.speedy = 5
        self.herox = WIDTH//2
        self.heroy = HEIGHT//2
        self.visible=True
        
    def update(self):
        if self.visible:
            if(self.rect.x - 16 > self.herox):
               self.rect.x -= self.speedx
            
            elif(self.rect.x + 16 < self.herox):
               self.rect.x += self.speedx
           
            if(self.rect.y - 16 > self.heroy):
               self.rect.y -= self.speedy
            
            elif(self.rect.y + 16 < self.heroy):
               self.rect.y += self.speedy
           
    def sethero(self, x, y):
        self.herox = x
        self.heroy = y
   
    def hit(self):
        if self.vida>0:
            self.vida -=1
        else:
            self.visible = False

class projetil(pygame.sprite.Sprite):
    def __init__(self,x,y,pew,facing):
        pygame.sprite.Sprite.__init__(self)
        self.image=pew
        self.image = pygame.transform.scale(pew, (70, 50))
        self.rect=self.image.get_rect()
        self.rect.bottom=y
        self.rect.centerx=x
        self.speedx=20 * facing
        self.facing = facing
    def update(self):
        self.rect.centerx += (self.speedx)
        if self.rect.centerx>width or self.rect.centerx<0:
            self.kill()
            
            
            
        

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
        self.image.set_colorkey((0,0,0))
   

for i in range (4):
    if i==0:
        for i in range (4):
    
            if i==0:
                p1=Platform(width/2-150+i*100,height-120,100,50,'left')
            elif i==3:
                p1=Platform(width/2-150+i*100,height-120,100,50,'right')
            else:
                p1=Platform(width/2-150+i*100,height-120,100,50,'middle')
        
            all_sprites.add(p1)
            all_platforms.add(p1)
        
    if i ==1:
         for i in range (4):
    
            if i==0:
                p1=Platform(width/2-400+i*70,height-300,70,45,'left')
            elif i==3:
                p1=Platform(width/2-400+i*70,height-300,70,45,'right')
            else:
                p1=Platform(width/2-400+i*70,height-300,70,45,'middle')
        
            all_sprites.add(p1)
            all_platforms.add(p1)
    if i ==2:
        
         for i in range (4):
    
            if i==0:
                p1=Platform(width/2+190+i*70,height-300,70,45,'left')
            elif i==3:
                p1=Platform(width/2+190+i*70,height-300,70,45,'right')
            else:
                p1=Platform(width/2+190+i*70,height-300,70,45,'middle')
            all_sprites.add(p1)
            all_platforms.add(p1)

    if i ==3:
        
        p1=Platform(width/2,height,900,30,'middle')
        
        all_sprites.add(p1)
        all_platforms.add(p1)




            
def RestaurarJanela():
    all_sprites.update()
    win.blit(bg, (0,0))
    all_sprites.draw(win)
    text=font.render("Lives: " + str(lives), 1, (255,215,0))
    placar=font.render("Score: " + str(score), 1, (255,215,0))
    win.blit(text,(750,10))
    win.blit(placar,(750,50))
    pygame.display.update()


   
man=player(1,510,64,64)
playergroup.add(man)
all_sprites.add(man)
projeteis=[]
font = pygame.font.SysFont("comicsana",40,True)
count=0
run = True
score=0

      
high_score_file = open("high_score_file.txt", "r")
high_score = int(high_score_file.read())
high_score_file.close()
                

end_it=False

while not end_it:
    win.fill((255,255,255))
    myfont=pygame.font.SysFont("Britannic Bold", 60)
    nlabel=myfont.render("Bem Vindo, Clique para começar", 1, (255,150,0))
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            end_it=True
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
    win.blit(nlabel,(150,300))
    pygame.display.flip()
    
try:

    
    lives=2
    while run:
        clock.tick(27)
        
        hits = pygame.sprite.groupcollide(playergroup, all_platforms, False, False)
        for hit in hits:
          man.rect.bottom = hit.rect.top
         
          
        if len(hits)==0:
            man.speedy-=-1#-(man.jumpCount ** 2) * 0.5
        else:
            man.speedy=0
        
        hits = pygame.sprite.groupcollide(enemygroup, playergroup, True, False)
     
        if hits:
            lives -= 1
           
            
        if lives == 0:
            if score>high_score:
                high_score_file = open("high_score_file.txt", "w")
                high_score_file.write(str(score))
                high_score_file.close()
                high_score_file = open("high_score_file.txt", "r")
                high_score = int(high_score_file.read())
                high_score_file.close()
            a= False
            pygame.mouse.get_pressed()
            while not a:
                win.fill((255,255,255))
                myfont=pygame.font.SysFont("Britannic Bold", 60)
                nlabel=myfont.render("Game Over", 1, (255,200,0))
                b=myfont.render("Score:"+ str(score),2, (255,200,0) )
                sco=myfont.render("HighScore:"+ str(high_score),2, (255,200,0) )
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        quit()
                    win.blit(nlabel,(300,200))
                    win.blit(b,(300,250))
                    win.blit(sco,(300,300))
                    
                    pygame.display.flip()
                    run =False
               

       
        

            
        hits =pygame.sprite.groupcollide(enemygroup,bullets , True, False ) 
        if hits:
             boom.play()
             score+=1
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                if man.esquerda:
                    facing = -1
                else:
                    facing = 1
                    
            if not(man.pulo):
                if keys[pygame.K_w]:
                    man.pulo = True
    
            else:
                if man.jumpCount >= -10:
                    neg = 1
                    if man.jumpCount < 0:
                        neg = -1
                    man.speedy -= 2#(man.jumpCount ** 2) * 0.5 * neg
                    man.jumpCount -= 1
                else:
                    man.jumpCount = 10
                    man.pulo = False
                    
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    man.speedx -= man.vel
                    man.direita = False
                    man.esquerda= True
                if event.key == pygame.K_d:
                    man.speedx += man.vel
                    man.direita = True
                    man.esquerda = False
                if event.key == pygame.K_SPACE:
                    bullet=projetil(man.rect.centerx,man.rect.bottom,pew,facing)
                    bullet.rect.centerx=man.rect.x +10
                    bullet.rect.bottom=man.rect.y + 40
                    som.play()
                    projeteis.append(bullet)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
            

             
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    man.speedx = 0
                if event.key == pygame.K_d:
                    man.speedx = 0
    
#            keys = pygame.key.get_pressed()
#            if keys[pygame.K_SPACE]:
#                if man.esquerda:
#                    facing = -1
#                else:
#                    facing = 1
#                if not(man.pulo):
#                    if keys[pygame.K_w]:
#                        man.pulo = True
#            
#            else:
#                if man.jumpCount >= -10:
#                    neg = 1
#                if man.jumpCount < 0:
#                    neg = -1
#                    man.rect.y -= (man.jumpCount ** 2) * 0.5 * neg
#                    man.jumpCount -= 1
#                else:
#                    man.jumpCount = 10
#                    man.pulo = False
       
                
        if count == 100:
            
            en= enemy(random.randrange(0,WIDTH), random.randrange(0,HEIGHT))
            enemygroup.add(en)
            all_sprites.add(en)
            count=0
        count+=1
                
        RestaurarJanela()
        for en in enemygroup:
            en.sethero(man.rect.x, man.rect.y)
            
        
finally:
    pygame.quit()
    quit()