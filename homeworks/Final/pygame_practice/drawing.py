import pygame
from pygame.locals import *
from sys import exit

pygame.init()
prev_pos = (300,300)

screen = pygame.display.set_mode((600,600),0,32)

while True:
    for event in pygame.event.get():
        assert type(event) == pygame.event.EventType
        if event.type ==QUIT:
            exit(0)
        elif event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.line(screen, (255,255,255), prev_pos, pos)
            prev_pos = pos
        pygame.display.update()
