from enum import Enum

import pygame

from tower import Tower

import json


class TowerType(Enum):
    FROST = "Frosttower"
    FIRE = "Firetower"
    NORMAL = "Normaltower"


class TowerFactory:
    def __init__(self, type: TowerType, enemies_group: pygame.sprite.Group, projectiles_group: pygame.sprite.Group):
        self.type = type
        self.enemies_group = enemies_group
        self.projectiles_group = projectiles_group

        with open("towers.json") as f:
            TOWER_DATA = json.load(f)

        match type:
            case TowerType.FIRE:
                TOWER_DATA = TOWER_DATA["Firetower"]
            case TowerType.FROST:
                TOWER_DATA = TOWER_DATA["Frosttower"]
            case TowerType.NORMAL:
                TOWER_DATA = TOWER_DATA["Normaltower"]

        self.image = pygame.image.load(TOWER_DATA["image_Path"])
        self.projectile_image = pygame.image.load(TOWER_DATA["projectile_image_Path"])
        self.name = TOWER_DATA["name"]
        self.range = TOWER_DATA["range"]
        self.target_mode = TOWER_DATA["target_mode"]

    def create(self, mouse_tile_x, mouse_tile_y):
        return Tower(self.image, mouse_tile_x, mouse_tile_y, self.range, self.enemies_group, self.projectiles_group,self.projectile_image, self.target_mode)
