import pygame


class AnimatedSprite(pygame.sprite.Sprite):

    def __init__(self, image):
        super().__init__()
        self.animated = image

    @property
    def image(self):
        return self.animated.blit_ready()[0]

    @property
    def rect(self):
        return self.animated.get_rect()
