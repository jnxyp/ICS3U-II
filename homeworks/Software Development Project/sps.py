# coding=utf-8
import random

import easygui as g
import os

PAPER = os.path.join('res', 'paper.png')
STONE = os.path.join('res', 'stone.png')
SCISSORS = os.path.join('res', 'scissors.png')
CANCEL = 'Cancel'

while True:
    u_choice = g.buttonbox(images=[PAPER, STONE, SCISSORS], choices=[CANCEL])
    if u_choice == CANCEL or u_choice == None:
        break
    c_choice = random.choice([PAPER, STONE, SCISSORS])
    if u_choice == c_choice:
        g.msgbox('Tie.')
    elif ((u_choice == STONE) and (c_choice == SCISSORS)) or (
        (u_choice == SCISSORS) and (c_choice == PAPER)) or (
        (u_choice == PAPER) and (c_choice == STONE)):
        g.msgbox('You win!')
    else:
        g.msgbox('You lose')

