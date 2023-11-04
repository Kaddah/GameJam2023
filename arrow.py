import pygame

class Arrow(pygame.sprite.Sprite):
    
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./assets/Arrow.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.x = x
        self.y = y
    
    def vertical(self, y:int):
        self.y += y
        self.rect.center = (self.x,self.y)
    def horizontal(self, x:int):
        self.x += x 
        self.rect.center = (self.x,self.y)

      
   
   

   