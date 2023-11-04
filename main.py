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
menu = pygame.sprite.Group()

# load LEVEL

#setup menu
menu.add()
menu_surface = pygame.Surface([WIDTH, MENUHEIGHT])
menu_surface.fill((255, 255, 255))

# Game Loop
while True:
    clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # update
    for tower in towers:
        tower.update(enemies)
    enemies.update()
    menu.update()

    # draw
    enemies.draw(screen)
    towers.draw(screen)
    menu.draw(screen)
    screen.blit(menu_surface, (0, 0))

    # flip
    pygame.display.flip()
