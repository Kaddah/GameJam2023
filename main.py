import pygame

from level import Level
from enemy import Enemy
from settings import *
import json

from sys import exit

pygame.init()

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Title and Icon
pygame.display.set_caption("Tower Defenc")

# clock
clock = pygame.time.Clock()

# load images


# load LEVEL
with open("Levels.json") as f:
    LEVEL_DATA = json.load(f)

level = Level(LEVEL_DATA["Level1"])

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
        elif event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_w:       
                enemy = Enemy(level.getWaypoints())
                enemies.add(enemy)

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

    #draw waypoints
    waypoints = level.getWaypoints()
    pygame.draw.lines(screen, (255, 0, 0), False, waypoints)

    # flip
    pygame.display.flip()
