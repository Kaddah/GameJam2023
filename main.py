import pygame
from settings import *

from sys import exit

pygame.init()

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Title and Icon
pygame.display.set_caption("Tower Defenc")

# clock
clock = pygame.time.Clock()

# Grouping
enemies = pygame.sprite.Group()
towers = pygame.sprite.Group()

# LEVEL


#Game Loop
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # draw

    # update
    towers.update()
    enemies.update()

    #flip
    pygame.display.flip()
