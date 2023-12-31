import math

import pygame
from pygame.math import Vector2

from animated_sprite import AnimatedSprite


class Enemy(AnimatedSprite):

    def __init__(self, waypoints, image, speed, lifes, rotation_offset):
        super().__init__(image)
        self.waypoints = waypoints
        self.pos = waypoints[0]
        self.target_waypoint = 1
        self.speed = speed
        self.lifes = lifes
        self.angle = 90
        self.rotation_offset = rotation_offset

    def update(self):
        self.move()
        self.rotate()

    def getPosition(self):
        return self.rect.center

    def on_hit(self, damage):
        self.lifes = self.lifes - damage
        if (self.lifes <= 0):
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, attr1=self))
            self.kill()

    def move(self):
        # target waypoint
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        else:
            # enemy reached end of path
            pygame.event.post(pygame.event.Event(pygame.USEREVENT+1, attr1=self))
            self.kill()

        # calculate distance to target
        distance = self.movement.length()
        if distance >= self.speed:
            self.pos += self.movement.normalize() * self.speed
        else:
            if distance != 0:
                self.pos += self.movement.normalize() * distance
            self.target_waypoint += 1

    def rotate(self):
        # calculate distance to next waypoint
        distance = self.target - self.pos

        # calculate angels
        self.angle = math.degrees(math.atan2(-distance[1], distance[0]))

    @property
    def image(self):
        return pygame.transform.rotate(super().image, self.angle + self.rotation_offset)

    @property
    def rect(self):
        rect = self.image.get_rect()
        rect.center = self.pos
        return rect
