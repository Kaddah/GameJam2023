import pygame

from settings import *


class Spritesheet:
    def __init__(self, imagePath):
        self.sheet = pygame.image.load(imagePath)

    def get_image(self, x, y):
        image = pygame.Surface((GRID, GRID))
        image.blit(self.sheet, (0, 0), (x * GRID, y * GRID, GRID, GRID))
        return image
