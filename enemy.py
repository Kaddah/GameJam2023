import pygame
from pygame.math import Vector2
import math

class Enemy (pygame.sprite.Sprite):

    def __init__(self, waypoints):  #später noch image übergeben
        pygame.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = waypoints [0]
        self.target_waypoint = 1
        self.speed = 2
        self.angel = 0
        self.original_image = pygame.Surface((20, 20))
        self.original_image.fill('green')
        self.image = pygame.transform.rotate(self.original_image, self.angel)    
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
    
    def update (self):
        self.move()
        self.rotate()

    def move (self):
        #target waypoint
        if self.target_waypoint < len (self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        else:
            #enemy reached end of path
            self.kill()
        
        # calculate distance to target
        distance = self.movement.length()
        if distance >= self.speed:
            self.pos += self.movement.normalize() * self.speed
        else: 
            if distance != 0:
                self.pos += self.movement.normalize() * distance
            self.target_waypoint += 1
        self.rect.center = self.pos

    def rotate (self):
        #calculate distance to next waypoint
        distance = self.target - self.pos

        #calculate angels
        self.angle = math.degrees(math.atan2 (-distance[1], distance[0]))

        #rotate image and update
        self.image = pygame.transform.rotate(self.original_image, self.angel)    
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    