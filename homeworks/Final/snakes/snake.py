from homeworks.Final.snakes.player import Player


class Snake:
    body = []
    velocity = ()
    color = ()
    player = None
    length_change = 0

    def __init__(self, player: Player, body: list, velocity: list = (0, 1),
                 color: tuple = (0, 0, 0)):
        if player is None or body is None or len(body) == 0:
            raise TypeError('Illigal Arguments')
            # TODO Detailed Error Message
        self.player = player
        self.body = body
        self.velocity = velocity
        self.color = color
        self.length_change = 0

    def get_body(self) -> list:
        return self.body

    def get_head(self) -> tuple:
        return self.get_body()[0]

    def get_tail(self) -> tuple:
        return self.get_body()[-1]

    def get_length(self) -> int:
        return len(self.get_body())

    def appened_body(self, length: int = 1):
        self.length_change += length

    def remove_body(self, length: int = 1):
        self.length_change -= length

    def move(self):
        i = 0
        while i < len()
