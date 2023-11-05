import pygame
import gif_pygame


class AnimatedSprite(pygame.sprite.Sprite):

    def __init__(self, image_path):
        super().__init__()
        self.animated = gif_pygame.load(image_path)

    @property
    def image(self):
        return self.animated.blit_ready()[0]

    @property
    def rect(self):
        return self.animated.get_rect()
