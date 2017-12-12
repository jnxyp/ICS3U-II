# coding=utf-8
# Course Code: ICS3U
# Author: jn_xyp
# Version: 2017-11-14
# Problem Set 6 - Question 3
import random

rand = random.randint(1,100)

while True:
    guess = input('Enter your guess (leave blank to exit game):')
    if guess == '':
        break
    try:
        guess = int(guess)
    except:
        print('Please enter an integer!')
        continue
    if guess > rand:
        print('Smaller than guess')
    elif guess < rand:
        print('Bigger than guess')
    else:
        print('So U belly gud!')
        break
