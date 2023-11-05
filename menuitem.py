import pygame

from settings import *


class Menuitem(pygame.sprite.Sprite):

    def __init__(self, x: int, y: int, width: int, height: int, img, name: str, obj):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.name = name
        self.obj = obj


class MenuBackground(pygame.sprite.Sprite):

    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([WIDTH, MENUHEIGHT])
        self.image.fill((225, 0, 195))

        self.rect = self.image.get_rect()
