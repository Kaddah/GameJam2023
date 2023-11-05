from enum import Enum

import gif_pygame
import pygame

from enemy import Enemy

import json


class EnemyFactory:

    def __init__(self, waypoints):
        self.type = type
        self.waypoints = waypoints

        with open("enemies.json") as f:
            ENEMY_DATA = json.load(f)

        self.enemySettings = {}
        for entry in ENEMY_DATA:
            tmp = {}
            tmp["image"] = gif_pygame.load(entry["image_Path"])
            tmp["speed"] = entry["speed"]
            tmp["lifes"] = entry["lifes"]
            tmp["rotation_offset"] = entry["rotation_offset"]

            self.enemySettings[entry["name"]] = tmp

    def create(self, type: str):
        return Enemy(self.waypoints, self.enemySettings[type]["image"], self.enemySettings[type]["speed"],
                     self.enemySettings[type]["lifes"], self.enemySettings[type]["rotation_offset"])
