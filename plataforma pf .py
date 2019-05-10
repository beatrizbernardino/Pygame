class Platform(pygame.sprite.Sprite):

    def __init__(self,x,y,w,h):
        pygame.sprite.Sprite.__init__(self)
        
        player_img=pygame.image.load(path.join(img_dir,'grassMid.png')).convert()
        self.image=player_img
        
        self.image=pygame.transform.scale(player_img,(w,h))
        
        self.rect=self.image.get_rect()
        
        self.rect.centerx=x
        self.rect.bottom=y
        
 
        
        
  
player=Player()
all_sprites.add(player)


for i in range(3):
    p1=Platform(10,height-400,20,10)
    
       
p1=Platform(width/2,height-400,500,100)
all_sprites.add(p1)
p2=Platform(100,height-200,250,100)
all_sprites.add(p2)
p3=Platform(width-100,height-200,250,100)
p4=Platform(width/2,height,width,50)
all_sprites.add(p3)
all_sprites.add(p4)
