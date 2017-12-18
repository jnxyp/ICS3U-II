import pygame
import sys
from pygame.locals import *

pygame.init()
size = (800, 600)

WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode(size)  # type: pygame.Surface
screen.fill((255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            pygame.draw.line(screen, GRAY,(mouse_pos[0], 0), (mouse_pos[0], size[0]))
        elif event.type == QUIT:
            sys.exit(666)

    pygame.display.update()
