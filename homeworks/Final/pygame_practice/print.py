import pygame
from sys import exit
from pygame.locals import *

pygame.init()

resolution = (800,600)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

screen = pygame.display.set_mode(resolution,0,32) # type: pygame.Surface
pygame.display.set_caption('Print Self')

font_obj = pygame.font.Font('font.ttc', 16)

file_content = ''
with open('print.py') as f:
    file_content = f.read()

y_pos = 0
for line in file_content.split('\n'):
    text_obj = font_obj.render(line, True, GREEN, (100,100,100))  # type: pygame.Surface
    rect = text_obj.get_rect() # type:pygame.Rect
    rect.top = y_pos
    y_pos += rect.height
    screen.blit(text_obj, rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()