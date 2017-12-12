# coding=utf-8
# Course Code: ICS3U
# Author: jn_xyp
# Version: 2017-11-14
# Problem Set 6 - Question 5
import random

stones = random.randint(15,30)
player_turn = False

if input('Input yes to play first:') == 'yes':
    player_turn = True

while True:
    print('There are', stones, 'stone(s).')
    if player_turn:
        temp = int(input('Enter the number of stone(s) you want to pick:'))
        stones = stones - temp
        print('Player picked', temp, 'stone(s).')
        player_turn = False
    else:
        while True:
            temp = random.randint(1,3)
            if temp <= stones:
                break
        stones = stones - temp
        print('Computer picked', temp, 'stone(s).')
        player_turn = True
    if stones == 0:
        if player_turn:
            print('You win!!!!!!!!!!!!!!!!!!!!!!!!')
        else:
            print('You lose....')