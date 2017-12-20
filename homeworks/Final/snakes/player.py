class Player:
    score = 0
    snake = None
    name = ''
    color = ()

    def __init__(self, board, name='Player', color: tuple = (0, 0, 0)):
        # TODO Argument Checking
        self.name = name
        self.color = color
        self.snake = board.gen_snake(self)
        self.score = 0

    def set_snake_direction(self, dir: tuple):
        self.snake.set_direction(dir)

    def snake_death_process(self):
        pass
