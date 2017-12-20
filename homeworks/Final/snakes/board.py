import random

from homeworks.Final.snakes.item import *
from homeworks.Final.snakes.snake import Snake


class Board:
    snakes = []
    grid = []

    def __init__(self, height: int = 15, width: int = 15):
        self.grid = [[Air() for j in range(width)] for i in range(height)]

    def check_collision(self):
        # Snakes and Items
        for snake in self.snakes:  # type: Snake
            block = self.get_block(snake.get_head())
            if type(block) != Air:  # type:Item
                if block.get_pt() > 0:
                    snake.add_tail()
                    block.set_pt(block.get_pt() - 1)
                elif block.get_pt() < 0:
                    snake.remove_head()
                    block.set_pt(block.get_pt() + 1)
                else:
                    self.set_block(snake.get_head(), Air())

        # Snakes and snakes
        for snake1 in self.snakes:  # type: Snake
            for snake2 in self.snakes:  # type: Snake
                if snake1 is not snake2:
                    if snake1.get_head() in snake2.get_body():
                        snake1.remove_head()

    def move_snakes(self):
        for snake in self.snakes:
            snake.move()

    def get_block(self, pos: tuple) -> Item:
        return self.grid[pos[0]][pos[1]]

    def set_block(self, pos: tuple, item: Item):
        self.grid[pos[0]][pos[1]] = item

    def get_grid(self) -> list:
        return self.grid

    def get_size(self) -> tuple:
        return (len(self.get_grid()), len(self.get_grid()[0]))

    def get_safe_place(self) -> tuple:
        while True:
            pos = (random.randint(self.get_size()[0]), random.randint(self.get_size()[1]))
            if type(self.get_block(pos)) == Air:
                return pos


if __name__ == '__main__':
    b = Board()
    print(b.grid)
