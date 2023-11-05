from enum import Enum
import random

import pygame.sprite

from enemyfactory import EnemyFactory
from settings import *
from spritesheet import Spritesheet


class TileType(Enum):
    HORIZONTAL = 3
    VERTICAL = 3
    CORNERLEFTBOTTON = 3
    CORNERLEFTTOP = 3
    CORNERRIGHTBOTTON = 3
    CORNERRIGHTTOP = 3


TileType = Enum("TileType", "HORIZONTAL VERTICAL CORNERLEFTBOTTON CORNERLEFTTOP CORNERRIGHTBOTTON CORNERRIGHTTOP")


class Level():
    def __init__(self, level_data: dict, enemies: pygame.sprite.Group):
        self.spawnRate = 1000
        self.lastSpawn = 0

        self.waypointsRaw = []
        self.waypoints = []
        self.enemies = enemies
        for waypoint in level_data["waypoints"]:
            x = waypoint["x"] * GRID + (GRID * 0.5)
            y = waypoint["y"] * GRID + MENUHEIGHT + (GRID * 0.5)
            self.waypointsRaw.append((waypoint["x"], waypoint["y"]))
            self.waypoints.append((x, y))

        self.life = level_data["life"]
        self.images = Spritesheet(level_data["imagePath"])
        self.waves = level_data["waves"]
        self.waveCounter = 0

        self.tiles = []
        self.money = level_data["money"]
        self.menuIcon = pygame.image.load(level_data["menuIcon_Path"])
        self.name = level_data["name"]

        for x in range(GRIDWIDTH):
            self.tiles.append([])
            for y in range(GRIDHEIGHT):
                self.tiles[x].append(self.isPointPath((x, y)))

        self.background = pygame.Surface([WIDTH, HEIGHT])
        # draw normal tiles
        for i in range(GRIDWIDTH):
            for j in range(GRIDHEIGHT):
                img = 0
                if self.tiles[i][j] == TileType.HORIZONTAL:
                    img = 2
                elif self.tiles[i][j] == TileType.VERTICAL:
                    img = 1
                elif self.tiles[i][j] == TileType.CORNERLEFTBOTTON:
                    img = 5
                elif self.tiles[i][j] == TileType.CORNERLEFTTOP:
                    img = 4
                elif self.tiles[i][j] == TileType.CORNERRIGHTBOTTON:
                    img = 6
                elif self.tiles[i][j] == TileType.CORNERRIGHTTOP:
                    img = 3
                else:
                    img = 7

                self.background.blit(self.images.get_image(img, 0), (i * GRID, j * GRID + MENUHEIGHT))

        self.enemieFactory = EnemyFactory(self.waypoints)

    def isPointPath(self, point1) -> TileType:
        # is Waypoint
        for i in range(1, len(self.waypoints)):
            if i > 0:
                prevWaypoint = self.waypointsRaw[i - 1]
                currentWaypoint = self.waypointsRaw[i]

                if prevWaypoint[1] == currentWaypoint[1] == point1[1]:
                    if prevWaypoint[0] < point1[0] < currentWaypoint[0] or prevWaypoint[0] > point1[0] > \
                            currentWaypoint[0]:
                        return TileType.HORIZONTAL
                elif prevWaypoint[0] == currentWaypoint[0] == point1[0]:
                    if prevWaypoint[1] < point1[1] < currentWaypoint[1] or prevWaypoint[1] > point1[1] > \
                            currentWaypoint[1]:
                        return TileType.VERTICAL

            if self.waypointsRaw[i] == point1:
                if i == 0:
                    return TileType.CORNERLEFTTOP
                elif i == len(self.waypoints) - 1:
                    return TileType.CORNERLEFTBOTTON

                prevWaypoint = self.waypointsRaw[i - 1]
                currentWaypoint = self.waypointsRaw[i]
                nextWaypoint = self.waypointsRaw[i + 1]

                if prevWaypoint[1] == currentWaypoint[1]:
                    if prevWaypoint[0] < currentWaypoint[0]:
                        if nextWaypoint[1] > currentWaypoint[1]:
                            return TileType.CORNERLEFTBOTTON
                        else:
                            return TileType.CORNERLEFTTOP
                    else:
                        if nextWaypoint[1] < currentWaypoint[1]:
                            return TileType.CORNERRIGHTTOP
                        else:
                            return TileType.CORNERRIGHTBOTTON
                elif prevWaypoint[0] == currentWaypoint[0]:
                    if prevWaypoint[1] < currentWaypoint[1]:
                        if nextWaypoint[0] < currentWaypoint[0]:
                            return TileType.CORNERLEFTTOP
                        else:
                            return TileType.CORNERRIGHTTOP
                    else:
                        if nextWaypoint[0] < currentWaypoint[0]:
                            return TileType.CORNERLEFTBOTTON
                        else:
                            return TileType.CORNERRIGHTBOTTON

    def getWaypoints(self):
        return self.waypoints

    def draw(self, screen: pygame.Surface):
        screen.blit(self.background, (0, 0))
        # draw waypoints

    def createEnemy(self, name:str):
        self.enemies.add(self.enemieFactory.create(name))

    def spawnNextWave(self):
        if pygame.time.get_ticks() < self.lastSpawn + self.spawnRate:
            return
        self.lastSpawn = pygame.time.get_ticks()

        wave = self.waves[self.waveCounter]
        # get random enemy from wave
        randomEnemy =  list(wave)[random.randint(0, len(wave) - 1)]

        wave[randomEnemy] -= 1
        if wave[randomEnemy] >= 0:
            self.createEnemy(randomEnemy)

        counter = 0
        for enemy in wave:
            counter += wave[enemy]

        if counter <= 0:
            self.waveCounter += 1
            self.spawnRate *= 0.95

            if self.waveCounter >= len(self.waves):
                pygame.event.post(pygame.event.Event(GAMEWON_EVENT, {"name": "levelFinished", "level": self}))


class LevelMenuitem(pygame.sprite.Sprite):

    def __init__(self, x: int, y: int, width: int, height: int, level: Level):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(level.menuIcon, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.name = level.name
        self.level = level






