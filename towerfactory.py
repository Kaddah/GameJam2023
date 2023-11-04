from enum import Enum

import pygame

from tower import Tower


class TowerType(Enum):
    FROST = "Frosttower"
    FIRE = "Firetower"


class TowerFactory:
    def __init__(self, type: TowerType):
        self.type = type

        # It would be better to configure towers via some JSON file
        match type:
            case TowerType.FIRE:
                self.image = pygame.image.load("assets/Fire_Tower.png")
                self.name = "Firetower"
            case TowerType.FROST:
                self.image = pygame.image.load("assets/Frost_Tower.png")
                self.name = "Frosttower"

    def create(self, mouse_tile_x, mouse_tile_y, range, enemies_group):
        return Tower(self.image, mouse_tile_x, mouse_tile_y, range, enemies_group)
