# coding=utf-8
# Course Code: ICS3U
# Author: jn_xyp
# Version: 2017-11-14
# Problem Set 6 - Question 2
import random


def pick():
    return random.choice(
        ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']) + ' of ' + random.choice(
        ['Hearts', 'Diamonds', 'Clubs', 'Spades'])


print(pick())
print(pick())
print(pick())
print(pick())
print(pick())
print(pick())
print(pick())
print(pick())
print(pick())
