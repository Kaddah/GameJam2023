import json
from sys import exit

import gif_pygame

from arrow import *
from enemy import Enemy
from level import Level
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

towerfactoryFrost = TowerFactory(TowerType.FROST, enemies, projectiles)
towerfactoryFire = TowerFactory(TowerType.FIRE, enemies, projectiles)
towerfactoryNormal = TowerFactory(TowerType.NORMAL, enemies, projectiles)

# setup menu
menu.add(MenuBackground(0, 0))
spacing = 16
temp = Menuitem(spacing, 16, 64, 64, towerfactoryFire.image, towerfactoryFire.image, towerfactoryFire)
menu.add(temp)
menuTower.add(temp)
temp = Menuitem(spacing + 32 * 2, 16, 64, 64, towerfactoryFrost.image, towerfactoryFrost.name, towerfactoryFrost)
menu.add(temp)
menuTower.add(temp)
temp = Menuitem(spacing + 32 * 4, 16, 64, 64, towerfactoryNormal.image, towerfactoryNormal.name, towerfactoryNormal)
menu.add(temp)
menuTower.add(temp)

selectedTower = None

# load LEVEL
with open("Levels.json") as f:
    LEVEL_DATA = json.load(f)

level = Level(LEVEL_DATA["Level1"],enemies)

# arrow
cursor = Arrow(0, 0)
arrow.add(cursor)

# Game Loop
while True:
    clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
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

            for tower in menuTower:
                if tower.rect.collidepoint(cursor.rect.center) and event.key == pygame.K_k:
                    if tower.obj and isinstance(tower.obj, TowerFactory):
                        selectedTower = tower.obj
                        print("Selected Tower: ", selectedTower.name)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            mouse_tile_x = mouse_pos[0] // 32
            mouse_tile_y = mouse_pos[1] // 32

            if selectedTower is not None and level.tiles[mouse_tile_x][mouse_tile_y - 4] is None:
                towers.add(selectedTower.create(mouse_tile_x, mouse_tile_y))

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
    arrow.draw(screen)
    projectiles.draw(screen)
    # draw waypoints
    waypoints = level.getWaypoints()
    pygame.draw.lines(screen, (255, 0, 0), False, waypoints)

    # draw FPS
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(int(clock.get_fps())), True, (255, 255, 255))
    screen.blit(text, (0, 0))

    # flip
    pygame.display.flip()
