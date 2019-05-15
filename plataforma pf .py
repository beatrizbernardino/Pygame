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
        p1=Platform(width/2-95+i*70,height-400,70,50,'left')
    elif i==3:
        p1=Platform(width/2-85+i*70,height-400,70,50,'right')
    else:
        p1=Platform(width/2-85+i*70,height-400,70,50,'middle')
        
    all_sprites.add(p1)