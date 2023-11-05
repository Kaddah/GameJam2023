import json
from sys import exit

import gif_pygame
import pygame

from arrow import *
from enemy import Enemy
from level import Level, LevelMenuitem
from menuitem import *
from towerfactory import TowerType, TowerFactory

pygame.init()

# Create the screen
flags = pygame.FULLSCREEN | pygame.HWSURFACE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
print(screen.get_size())

# Title and Icon
pygame.display.set_caption("Tower Defenc")

# clock
clock = pygame.time.Clock()

# Grouping
enemies = pygame.sprite.Group()

towers = pygame.sprite.Group()
menu = pygame.sprite.Group()
arrow = pygame.sprite.Group()
menuTower = pygame.sprite.Group()
projectiles = pygame.sprite.Group()

levels = pygame.sprite.Group()

towerfactoryFrost = TowerFactory(TowerType.FROST, enemies, projectiles)
towerfactoryFire = TowerFactory(TowerType.FIRE, enemies, projectiles)
towerfactoryNormal = TowerFactory(TowerType.NORMAL, enemies, projectiles)

# setup menu
menu.add(MenuBackground(0, 0))
spacing = 16
temp = Menuitem(spacing, 16, 64, 64, towerfactoryFire.menu_image, towerfactoryFire.image, towerfactoryFire)
menu.add(temp)
menuTower.add(temp)
temp = Menuitem(spacing + 32 * 2, 16, 64, 64, towerfactoryFrost.menu_image, towerfactoryFrost.name, towerfactoryFrost)
menu.add(temp)
menuTower.add(temp)
temp = Menuitem(spacing + 32 * 4, 16, 64, 64, towerfactoryNormal.menu_image, towerfactoryNormal.name, towerfactoryNormal)
menu.add(temp)
menuTower.add(temp)

selectedTower = None

# load LEVEL
with open("Levels.json") as f:
    LEVEL_DATA = json.load(f)

# setup Levelselect
levels.add(LevelMenuitem(32, 32, 128, 128, Level(LEVEL_DATA["Level1"], enemies)))


level = None

# arrow
cursor = Arrow(0, 0)
arrow.add(cursor)

# GAME States
gamestate = "start"

# Game Loop
while True:
    clock.tick(60)
    screen.fill((0, 0, 0))

    # events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    if gamestate == "start":
        #TODO: Add Startscreen
        titlescreen = pygame.image.load("assets/Titlescreen.png")
        screen.blit(titlescreen, (0,0))
        for event in events:
            if event.type == pygame.KEYDOWN:
                gamestate = "levelselect"
                print("Start")
    elif gamestate == "gameover":
        #TODO: Add Gameover
        gameover = pygame.image.load("assets/Gameover.png")
        screen.blit(gameover, (0,0))
    elif gamestate == "levelselect":
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    cursor.vertical(-32)
                elif event.key == pygame.K_s:
                    cursor.vertical(32)
                elif event.key == pygame.K_a:
                    cursor.horizontal(-32)
                elif event.key == pygame.K_d:
                    cursor.horizontal(32)

                for l in levels:
                    if l.rect.collidepoint(cursor.rect.center) and event.key == pygame.K_k:
                        level = l.level
                        gamestate = "running"


        levels.update()
        screen.fill((0, 100, 0))
        levels.draw(screen)
        c = 1
    elif gamestate == "running":
        for event in events:
            if event.type == ENEMYKILLED_EVENT:
                level.money += 5
            elif event.type == LIFELOST_EVENT:
                level.life -= 1
                if level.life <= 0:
                    gamestate = "gameover"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == pygame.K_w:
                    cursor.vertical(-32)
                elif event.key == pygame.K_s:
                    cursor.vertical(32)
                elif event.key == pygame.K_a:
                    cursor.horizontal(-32)
                elif event.key == pygame.K_d:
                    cursor.horizontal(32)
                elif event.key == pygame.K_i:
                    selectedTower = None
                    cursor.image = pygame.image.load("assets/Arrow.png")
                elif event.key == pygame.K_u:
                    if selectedTower is not None:
                        mouse_pos = cursor.rect.center
                        mouse_tile_x = mouse_pos[0] // 32
                        mouse_tile_y = mouse_pos[1] // 32
                        if selectedTower is not None and level.tiles[mouse_tile_x][mouse_tile_y - 4] is None and level.money > 0:
                            newTower = selectedTower.create(mouse_tile_x, mouse_tile_y)
                            towers.add(newTower)
                            level.money -= newTower.costs

                    else:
                        for tower in menuTower:
                            if tower.rect.collidepoint(cursor.rect.center):
                                if tower.obj and isinstance(tower.obj, TowerFactory):
                                    selectedTower = tower.obj
                                    cursor.image = selectedTower.image
                                    print("Selected Tower: ", selectedTower.name)


        # update
        towers.update()
        enemies.update()
        menu.update()
        projectiles.update()

        level.spawnNextWave()

        # draw
        level.draw(screen)
        enemies.draw(screen)
        menu.draw(screen)
        towers.draw(screen)
        projectiles.draw(screen)
        # draw waypoints
        waypoints = level.getWaypoints()
        pygame.draw.lines(screen, (255, 0, 0), False, waypoints)

        # Life
        text_money = font.render("Life      "+str(int(level.life)), True, (255, 255, 255))
        screen.blit(text_money, (WIDTH/2+WIDTH/4, 50))
        # money
        text_money = font.render("Money "+str(int(level.money)), True, (255, 255, 255))
        screen.blit(text_money, (WIDTH / 2 + WIDTH / 4, 10))

    # draw cursor
    arrow.draw(screen)

    # draw FPS
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(int(clock.get_fps())), True, (255, 255, 255))
    screen.blit(text, (0, 0))

    # flip
    pygame.display.flip()
