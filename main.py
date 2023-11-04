import pygame
from enemy import Enemy
from settings import *

from sys import exit

pygame.init()

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Title and Icon
pygame.display.set_caption("Tower Defenc")

# clock
clock = pygame.time.Clock()

# load images
enemy_images = pygame.image.load ("image-file")

# Grouping
enemies = pygame.sprite.Group()

enemy = Enemy (waypoints, enemy_images)
enemies.add (enemy)
towers = pygame.sprite.Group()

# load LEVEL


# Game Loop
while True:
    clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # update
    towers.update()
    enemies.update()

    # draw
    enemies.draw(screen)
    towers.draw(screen)

    # flip
    pygame.display.flip()
