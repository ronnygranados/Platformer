import pygame
import sys
from variables import *
from settings import *
from level import Level

# pygame setup

pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
level = Level(level_map, SCREEN)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.fill(BLACK)
    level.run()
    pygame.display.update()
    CLOCK.tick(60)
