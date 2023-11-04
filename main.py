import pygame

from level import Level
from enemy import Enemy
from tower import Tower 
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
ghost_image = pygame.image.load("assets/Ghost.png")
spider_image = pygame.image.load("assets/Spider.png")

fireTower_image = pygame.image.load("assets/Fire_Tower.png")


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
                enemy_ghost = Enemy(level.getWaypoints(), ghost_image, 2, 5)
                enemy_spider = Enemy(level.getWaypoints(), spider_image, 3, 5)
                enemies.add(enemy_ghost)
                enemies.add(enemy_spider)
       

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            mouse_tile_x = mouse_pos[0] // 40
            mouse_tile_y = mouse_pos[1] // 38

            fireTower = Tower(fireTower_image, mouse_tile_x,  mouse_tile_y) 
            towers.add(fireTower)
        

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
