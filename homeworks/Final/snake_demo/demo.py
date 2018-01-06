# Author: jn_xyp
# Version: 2018.01.05

import abc

import sys
from PyQt5.QtGui import QPainter, QFont
from PyQt5.QtWidgets import QWidget, QApplication

# Positive directions: right and down
# 2d array index: [Vertical][Horizontal]

# (Vertical move, Horizontal move)

DIRECTIONS = {'RIGHT': (0, 1), 'UP': (-1, 0), 'LEFT': (0, -1), 'DOWN': (1, 0)}
FONT = QFont('Arial', 15)

class Game:
    snakes = []
    grid = []
    window = None

    def __init__(self, size: tuple = (20, 20)):
        self.init_grid(size)

    def init_grid(self, size: tuple):
        grid = []
        for row in range(0, size[0]):
            # Fill grid with air
            grid.append([Air() for col in range(0, size[1])])
        self.grid = grid

    def draw(self, qp:QPainter):
        for row in self.grid:
            for item in row:
                item.draw(qp)
        for snake in self.snakes:
            snake.draw(qp)


class Window(QWidget):
    app = QApplication(sys.argv)

    def __init__(self):
        super().__init__()
        self.initUI()

    def paintEvent(self, event):



class Snake:
    body = []
    length_change = 0
    direction = ()

    def __init__(self, body: list, length_change: int, direction: tuple = DIRECTIONS.get('UP')):
        self.body = body
        self.length_change = length_change
        self.direction = direction

    def get_head(self):
        return self.body[0]

    def get_tail(self):
        return self.body[-1]

    def set_direction(self, direction: tuple or str):
        # TODO Input check
        if type(direction) == tuple:
            self.direction = direction
        else:
            self.direction = DIRECTIONS.get(direction)

    def move(self):
        if self.length_change > 0:
            new_head = (self.get_head()[0] + self.direction[0], self.get_head()[1] + self.direction[1])
            self.body.insert(0, new_head)
            self.length_change -= 1
        elif self.length_change < 0:
            self.body.pop(-1)
            self.length_change += 1
        else:
            new_head = (self.get_head()[0] + self.direction[0], self.get_head()[1] + self.direction[1])
            self.body.insert(0, new_head)
            self.body.pop(-1)

    def add_len(self, length: int):
        self.length_change += length

    def draw(self, qp:QPainter):
        pass


class Player:
    input_lock = False
    snake = None
    score = 0
    life = 1

    def __init__(self, life: int = 3, score: int = 0):
        self.life = life
        self.score = score


class Item:
    __metaclass__ = abc.ABCMeta
    value = 0

    def __init__(self, value: int):
        self.value = value

    # @abc.abstractmethod
    # def get_char(self):
    #     pass

    @abc.abstractmethod
    def draw(self, qp: QPainter):
        pass

    @abc.abstractmethod
    def contact_with(self, snake: Snake):
        pass


class Air(Item):

    def __init__(self):
        super().__init__(0)

    # def get_char(self):
    #     return '空'

    def contact_with(self, snake: Snake):
        pass  # DO NOTHING


class Food(Item):

    def __init__(self, value: int = 1):
        super().__init__(value)

    # def get_char(self):
    #     return '饭'

    def contact_with(self, snake: Snake):
        snake.add_len(self.value)
        self.value = 0


class Wall(Item):
    unbreakable = False

    def __init__(self, value: int = -1, unbreakable: bool = False):
        super().__init__(value)
        self.unbreakable = unbreakable

    # def get_char(self):
    #     return '墙'

    def contact_with(self, snake: Snake):
        if self.value < 0:
            snake.add_len(-1)
        if not self.unbreakable:
            self.value += 1
