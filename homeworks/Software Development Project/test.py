# coding=utf-8
import easygui as g

a = 0
b = 1
c = 2

if g.ccbox(msg='You Lose!\n\nNumber of win: %d\nNumber of lose: %d' % (a, b),
           default_choice="Try again",
           cancel_choice="Exit"):
    pass
