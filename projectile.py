import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, source, target, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.position = source.rect.center
        self.speed = 5
        self.source = source
        self.target = target
        self.damage = 5

    def update(self):
        target_rect = self.target.rect
        vec = pygame.math.Vector2(target_rect.center[0] - self.position[0], target_rect.center[1] - self.position[1])
        length, angle = vec.as_polar()
        if length < self.speed:
            self.target.on_hit(self.damage)
            self.kill()
        vec.from_polar((self.speed, angle))
        self.position = (self.position[0] + vec.x, self.position[1] + vec.y)
        self.rect.center = self.position
