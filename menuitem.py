from typing import Any
from settings import *
import pygame

class Menuitem (pygame.sprite.Sprite):

    def __init__(self, x: int, y: int, width: int, height: int, img, name:str):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.name = name

class MenuBackground (pygame.sprite.Sprite):

    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([WIDTH, MENUHEIGHT])
        self.image.fill((225, 0, 195))

        self.rect = self.image.get_rect()
   
   
    
    