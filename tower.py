from typing import Any
import pygame
import math

class Tower(pygame.sprite.Sprite):
    
   def __init__(self, image, tile_x, tile_y, range, enemies):
      pygame.sprite.Sprite.__init__(self)
      self.tile_x = tile_x
      self.tile_y = tile_y
      self.x = (self.tile_x + 0.5) * 40
      self.y = (self.tile_y + 0.5) * 38
      self.range = range
      self.enemies = enemies
      self.image = image
      self.target = None
      self.rect = self.image.get_rect()
      self.rect.center = (self.x, self.y)
   
   def update(self):
      for enemy in self.enemies:
         distX = enemy.getPosition()[0] - self.rect.center[0]
         distY = enemy.getPosition()[1] - self.rect.center[1]
         distance = math.sqrt(distX ** 2 + distY ** 2)
         if distance <= self.range:
            self.target = enemy
         break
      print (self.target)
