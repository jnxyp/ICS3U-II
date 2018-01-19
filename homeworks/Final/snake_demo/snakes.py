from tkinter import *
from random import choice

SNAKE_HEAD_COLOR = 'gray'
SNAKE_BODY_COLORS = ['gold', 'cyan', 'orangered', 'royalblue2', 'darkorchid2']
DIRECTIONS = {'STOP': (0, 0), 'UP': (0, -1), 'DOWN': (0, 1), 'RIGHT': (1, 0), 'LEFT': (-1, 0)}

BLOCK_SIZE = 15


def add_tuple(t1, t2):
    return (t1[0] + t2[0]), (t1[1] + t2[1])


class Snake:
    can_turn = False
    alive = True
    direction = DIRECTIONS['STOP']
    body = []
    length_change = 0
    color = ''
    board = None

    def __init__(self, board, head_pos: tuple = None, direction: tuple = DIRECTIONS['STOP'],
                 color=choice(SNAKE_BODY_COLORS)):
        self.board = board  # type:Board
        if head_pos is None:
            head_pos = board.get_safe_pos()
        self.body = [head_pos]
        self.direction = direction
        self.color = color

    def get_head(self):
        return self.body[0]

    def move_head(self):
        new_head = add_tuple(self.get_head(), self.direction)
        new_head = self.board.mod_pos(new_head)
        self.body.insert(0, new_head)

    def move_tail(self):
        self.body.pop()

    def move(self):
        if self.check_forward():
            # Move forward
            if self.length_change >= 0:
                self.move_head()
                if self.length_change > 0:
                    self.length_change -= 1
        # Remove tail
        if self.length_change <= 0:
            self.move_tail()
            if self.length_change < 0:
                self.length_change += 1

    def check_forward(self):
        next_pos = add_tuple(self.get_head(), self.direction)
        # Check snake
        snake = self.board.get_snake_at(next_pos)
        if snake is not None:
            # if contact with other snake's body, -1 length per cycle
            self.length_change -= 1
            return False
        else:
            # Check item
            item = self.board.get_item_at(next_pos)
            item.contact_with(self)  # send contact message to item
            if item.can_pass:
                return True
            else:
                return False


class Board:
    width = 0
    height = 0
    grid = []
    snakes = []

    def get_safe_pos(self) -> tuple:
        pass

    def mod_pos(self, pos: tuple):
        return pos[0] % self.width, pos[1] % self.height

    def get_snake_at(self, pos: tuple):
        for snake in self.snakes:  # type: Snake
            if pos in snake.body:
                return snake
        return None

    def get_item_at(self, pos: tuple):
        return self.grid[pos[1]][pos[0]]

    def remove_item(self, item):
        y = 0
        while y < len(self.grid):
            x = 0
            while x < len(self.grid[y]):
                if self.grid[y][x] == item:
                    break
        self.grid[y][x] = Air()


class Item:
    board = None
    can_pass = True
    value = 0

    def __init__(self, board: Board, value: int, can_pass: bool):
        self.board = board
        self.value = value
        self.can_pass = can_pass

    def contact_with(self, snake: Snake):
        pass


class Air(Item):
    def __init__(self, board: Board):
        super().__init__(board, 0, True)

    def contact_with(self, snake: Snake):
        pass


class Food(Item):

    def __init__(self, board: Board, value=1):
        super().__init__(board, value, True)

    def contact_with(self, snake: Snake):
        snake.length_change += self.value
        self.board.remove_item(self)


class Wall(Item):
    unbreakable = False

    def __init__(self, board: Board, value=-1, unbreakable=False):
        super().__init__(board, value, False)
        self.unbreakable = unbreakable

    def contact_with(self, snake: Snake):
        snake.length_change -= 1
        self.value += 1
        if self.value >= 0:
            self.board.remove_item(self)
