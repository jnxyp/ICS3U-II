# Course Code: ICS3U
# Author: jn_xyp
# Version: 2017-10-10
# Problem Set 3 - Question 7

def is_palindrome(_str:str):
    r = ''
    for s in _str:
        r = s + r
    if r == _str:
        return True
    return False

def is_palindrome_2(_str: str):
    i = 0
    while 2*i<len(_str):
        if _str[i] != _str[-i-1]:
            return False
        i+=1
    return True

def is_palindrome_ish(_str:str):
    return is_palindrome(_str.lower().replace(' ','').replace(',', '').replace('.', ''))

def brackets_match(_str:str):
    cot = 0
    for s in _str:
        if s == '(':
            cot+=1
        elif s == ')':
            cot -= 1
        if cot < 0:
            return False
    if cot != 0:
        return False
    return True



print(is_palindrome('racecar'))
print(is_palindrome('racear'))
print(is_palindrome_2('racecar'))
print(is_palindrome_ish('Race,.,.,Car..,,,'))
print(brackets_match(')('))

print(brackets_match('((()))()()'))
print(brackets_match('((()))(()'))