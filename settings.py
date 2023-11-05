import pygame

# window

GRIDWIDTH = 40
GRIDHEIGHT = 28

GRID = 32
MENUHEIGHT = GRID * 4

WIDTH = GRIDWIDTH * GRID
HEIGHT = GRIDHEIGHT * GRID + MENUHEIGHT


#EVENTS
LIFELOST_EVENT = pygame.USEREVENT + 1
ENEMYKILLED_EVENT = pygame.USEREVENT + 0


#GAME STATE
LEVELSELECT = 0
GAME = "running"
STARTSCREEN ="start"
GAMEOVER = "gameover"