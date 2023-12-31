import pygame

from projectile import Projectile


class Tower(pygame.sprite.Sprite):

    def __init__(self, image, tile_x, tile_y, range, enemies, projectiles, projectile_image, target_mode, damage, attack_speed,costs):
        pygame.sprite.Sprite.__init__(self)
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.x = (self.tile_x + 0.5) * 32
        self.y = (self.tile_y + 0.5) * 32
        self.range = range
        self.enemies = enemies
        self.image = image
        self.target = None
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.projectiles = projectiles
        self.last_shot = 0
        self.attack_speed = (11 - attack_speed) *100
        self.projectile_image = projectile_image
        self.target_mode = target_mode
        self.damage = damage
        self.costs = costs

    def distance(self, enemy):
        vec = pygame.math.Vector2(enemy.rect.center[0] - self.x, enemy.rect.center[1] - self.y)
        return vec.length()


    def update(self):
        minDist = 9999999
        if pygame.time.get_ticks() < self.last_shot + self.attack_speed:
            return

        self.target = None
        if self.target_mode == "nextEnemy":
            # find closest enemy
            for enemy in self.enemies:
                dist = self.distance(enemy)
                if dist <= self.range and dist <= minDist:
                    minDist = dist
                    self.target = enemy

        if self.target_mode == "strongestEnemy":
            # find strongest enemy
            maxLifes = -1
            for enemy in self.enemies:
                dist = self.distance(enemy)
                if dist <= self.range and maxLifes < enemy.lifes:
                    maxLifes = enemy.lifes
                    self.target = enemy

        # find fastest enemy
        maxSpeed = 0
        if self.target_mode == "fastesEnemy":
            for enemy in self.enemies:
                dist = self.distance(enemy)
                if dist <= self.range and maxSpeed < enemy.speed:
                    maxSpeed = enemy.speed
                    self.target = enemy

        if self.target is not None:
            projectile = Projectile(self, self.target, self.projectile_image, self.damage, 5)
            self.projectiles.add(projectile)
            self.last_shot = pygame.time.get_ticks()
