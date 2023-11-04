import pygame
import gif_pygame

class AnimatedSprite(pygame.sprite.Sprite):

    def __init__(self, image_path):
        super().__init__()
        self.animated = gif_pygame.load(image_path)
        self.rect = self.animated.get_rect()

    @property  
    def image(self): 
        return self.animated.blit_ready()[0]
    
    @image.setter
    def image(self, var):
        pass  

    
        

    
        


