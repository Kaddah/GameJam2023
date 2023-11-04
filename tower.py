import math
from typing import Any
import pygame
import math
from projectile import Projectile

class Tower(pygame.sprite.Sprite):
    
   def __init__(self, image, tile_x, tile_y, range, enemies, projectiles):
      pygame.sprite.Sprite.__init__(self)
      self.tile_x = tile_x
      self.tile_y = tile_y
      self.x = (self.tile_x + 0.5) * 40
      self.y = (self.tile_y + 0.5) * 32
      self.range = range
      self.enemies = enemies
      self.image = image
      self.target = None
      self.rect = self.image.get_rect()
      self.rect.center = (self.x, self.y)
      self.projectiles = projectiles
      self.last_shot = 0
      self.attack_speed = 0.6 * 1000
   
   def distance (self, enemy):
      distX = enemy.getPosition()[0] - self.rect.center[0]
      distY = enemy.getPosition()[1] - self.rect.center[1]
      distance = math.sqrt(distX ** 2 + distY ** 2)   
      return distance

   def update(self):
      minDist = 9999999
      if pygame.time.get_ticks() < self.last_shot + self.attack_speed:
         return
      for enemy in self.enemies:
         dist = self.distance(enemy)
         if dist <= self.range:
            if dist <= minDist:
               minDist = dist        
               self.target = enemy 
               projectile = Projectile(self, enemy)   
               self.projectiles.add(projectile)
               self.last_shot = pygame.time.get_ticks()
               break
      
         