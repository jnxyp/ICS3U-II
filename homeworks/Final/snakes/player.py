from homeworks.Final.snakes.board import Board
from homeworks.Final.snakes.snake import *


class Player:
    score = 0
    snake = None
    name = ''
    color = ()

    def __init__(self, board: Board, name='Player', color: tuple = (0, 0, 0)):
        # TODO Argument Checking
        self.name = name
        self.color = color
        self.snake = Snake(self, [board.get_safe_place()], color=self.color)
        self.score = 0

    def set_snake_direction(self):
        # Console input
        dir = ''
        while dir not in ['W', 'A', 'S', 'D']:
            dir = input(self.name + ':').upper()
        if dir == 'W':
            dir = DIRECTIONS['UP']
        elif dir == 'A':
            dir = DIRECTIONS['LEFT']
        elif dir == 'S':
            dir = DIRECTIONS['DOWN']
        else:
            dir = DIRECTIONS['RIGHT']
        self.snake.set_direction(dir)
