import os
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
dt = 0
ghost = pygame.image.load(os.path.join('assets', 'ghost.png'))
x = 0
y = 0

while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("pink")
    screen.blit(ghost, (x,y))

    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= 300 * dt 
    if keys[pygame.K_s]:
        y += 300 * dt
    if keys[pygame.K_a]:
        x -= 300 * dt
    if keys[pygame.K_d]:
        x += 300 * dt

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()