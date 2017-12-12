# coding=utf-8
import random
from ast import literal_eval

import easygui as g
import os

PAPER = os.path.join('res', 'paper.png')
STONE = os.path.join('res', 'stone.png')
SCISSORS = os.path.join('res', 'scissors.png')
CANCEL = 'Cancel'
ROUND = 5
RANKING_FILE = 'rank.sb'

rank = []

try:
    with open(RANKING_FILE, 'r') as file:
        rank = literal_eval(file.read())
except FileNotFoundError:
    pass

name = g.enterbox(msg='Enter your name', default='Player')
if name is None:
    name = 'Player'

# Game playing
score = 0
r = 1
while r <= ROUND:
    u_choice = g.buttonbox(images=[PAPER, STONE, SCISSORS], choices=['Cancel'])
    if u_choice == CANCEL or u_choice == None:
        break
    c_choice = random.choice([PAPER, STONE, SCISSORS])
    if u_choice == c_choice:
        g.msgbox('Tie.')
    elif ((u_choice == STONE) and (c_choice == SCISSORS)) or (
        (u_choice == SCISSORS) and (c_choice == PAPER)) or (
        (u_choice == PAPER) and (c_choice == STONE)):
        g.msgbox('You win!')
        score += 3
    else:
        g.msgbox('You lose')
        score -= 1
    r += 1


rank.append((name, score))
rank.sort(key=lambda t: t[1], reverse=True)

rank_str = 'Player Name' + '\t' * 5 + 'Score\n\n'
for tup in rank:
    if tup[0] == name:
        rank_str += '[' + tup[0] + ']'+'\t' * 5 + str(tup[1]) + '\n'
    else:
        rank_str += tup[0] + '\t'*5 + str(tup[1]) + '\n'

g.msgbox(rank_str, 'Ranking')


with open(RANKING_FILE, 'w') as file:
    file.write(repr(rank))

