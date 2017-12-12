# coding=utf-8
# Course Code: ICS3U
# Author: jn_xyp
# Version: 2017-11-14
# Problem Set 6 - Question 5 hehe
import random

stones = random.randint(15, 30)
pick_choices = [1, 2, 3]


def pick(remain_stone, pick_choices):
    for choice in pick_choices:
        if remain_stone - choice > 0:
            if (remain_stone - choice) % (min(pick_choices) + max(pick_choices)) == 1:
                return choice
    return min(pick_choices)


player_turn = None

if input('Type \'Yes\' to pick first.') == 'yes':
    player_turn = True
else:
    player_turn = False

print('There are', stones, 'stone(s) now.')

while True:
    if player_turn:
        while True:
            temp = input('Input the number of stone(s) you want to pick:')
            try:
                temp = int(temp)
            except:
                print('Please input a valid number.')
                continue
            if temp not in pick_choices or temp > stones:
                print('Please input a valid number.')
                continue
            else:
                stones = stones - temp
                print('Player picked', temp, 'stone(s).')
                player_turn = False
                break
    else:
        temp = pick(stones, pick_choices)
        stones = stones - temp
        player_turn = True
        print('Computer picked', temp, 'stone(s).')
    if stones == 0:
        if player_turn:
            print('You win!')
        else:
            print('You lose!')
        break
    print('There are', stones, 'stone(s) remain.')

