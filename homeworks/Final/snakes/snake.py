from homeworks.Final.snakes.player import Player

class Snake:
    DIRECTIONS = {'UP': (0, -1), 'DOWN': (0, 1), 'LEFT': (-1, 0), 'RIGHT': (1, 0)}

    body = []
    direction = ()  # x,y
    color = ()
    player = None

    tail_add = 0
    head_remove = 0

    def __init__(self, player: Player, body: list, direction: str = 'UP',
                 color: tuple = (0, 0, 0)):
        # TODO Argument Checking
        self.player = player
        self.body = body
        self.direction = direction
        self.color = color
        self.tail_add = 0
        self.head_remove = 0

    def set_direction(self, direction: tuple):
        self.direction = direction

    def get_body(self) -> list:
        return self.body

    def get_head(self) -> tuple:
        return self.get_body()[0]

    def get_tail(self) -> tuple:
        return self.get_body()[-1]

    def get_length(self) -> int:
        return len(self.get_body())

    def add_tail(self, length: int = 1):
        self.tail_add += length
        # Add score for player
        self.player.score += length

    def remove_head(self, length: int = 1):
        self.head_remove += length

    def move(self):
        if self.head_remove == 0:
            # Move head forward
            new_head = (self.get_head()[1] + self.direction[1],
                        self.get_head()[0] + self.direction[0])
            self.get_body().insert(0, new_head)
        else:
            self.head_remove -= 1

        if self.tail_add == 0:
            # Delete the tail
            self.get_body().pop(-1)
        else:
            self.tail_add -= 1

    def eliminate(self):
        self.player.snake_death_process()

