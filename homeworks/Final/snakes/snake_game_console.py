from homeworks.Final.snakes.board import Board
from homeworks.Final.snakes.item import *
from homeworks.Final.snakes.player import Player
from homeworks.Final.snakes.snake import Snake

b = Board()
m = b.get_grid()
p = [Player(b)]


def list_players(pl:list):
    s = ''
    for p in pl: # type:Player
        s += p.name + '\t' + str(p.score) + '\n'
    return s

def render(b: Board):
    str_map = [['' for x in range(b.get_size()[1])] for y in range(b.get_size()[0])]

    y = 0
    # Draw items
    while y < b.get_size()[0]:
        x = 0
        while x < b.get_size()[1]:
            if type(m[y][x]) is Air:
                str_map[y][x] = '口 '
            elif type(m[y][x]) is Food:
                str_map[y][x] = '饭 '
            elif type(m[y][x]) is Wall:
                str_map[y][x] = '墙 '
            x += 1
        y += 1
        # Draw snakes
    for snake in b.snakes:
        for seg in snake.get_body():
            str_map[seg[0]][seg[1]] = '＃ '
        seg = snake.get_head()
        str_map[seg[0]][seg[1]] = '＠ '
    s = ''
    for line in str_map:
        for c in line:
            s += c
        s += '\n'

    return s

# Main loop
while len(b.snakes) > 0:
    print(render(b))
    print(list_players(p))

    for player in p: # type:Player
        direction = input(player.name + ':')
        if direction == 'w':
            direction = Snake.DIRECTIONS['UP']
        elif direction == 'a':
            direction = Snake.DIRECTIONS['LEFT']
        elif direction == 's':
            direction = Snake.DIRECTIONS['DOWN']
        elif direction == 'd':
            direction = Snake.DIRECTIONS['RIGHT']
        else:
            direction = player.snake.direction
        player.set_snake_direction(direction)

    b.move_snakes()
    b.check_collision()
    b.check_snakes_statues()

