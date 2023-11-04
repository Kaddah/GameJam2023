import pygame.sprite

from spritesheet import Spritesheet
from settings import *
from enum import Enum


class TileType(Enum):
    HORIZONTAL = 3
    VERTICAL = 3
    CORNERLEFTBOTTON = 3
    CORNERLEFTTOP = 3
    CORNERRIGHTBOTTON = 3
    CORNERRIGHTTOP = 3


TileType = Enum("TileType", "HORIZONTAL VERTICAL CORNERLEFTBOTTON CORNERLEFTTOP CORNERRIGHTBOTTON CORNERRIGHTTOP")


class Level():
    def __init__(self, level_data: dict):
        self.waypointsRaw = []
        self.waypoints = []
        for waypoint in level_data["waypoints"]:
            x = waypoint["x"] * GRID + (GRID * 0.5)
            y = waypoint["y"] * GRID + MENUHEIGHT + (GRID * 0.5)
            self.waypointsRaw.append((waypoint["x"], waypoint["y"]))
            self.waypoints.append((x, y))

        self.images = Spritesheet(level_data["imagePath"])

        self.tiles = []

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

        for waypoint in self.waypoints:
            pygame.draw.circle(screen, (255, 0, 0), waypoint, 3)
