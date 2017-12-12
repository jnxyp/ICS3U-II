# Course Code: ICS3U
# Author: jn_xyp
# Version: 2017-10-11
# Problem Set 3 - Question 1-5

# Question 1
def every_nth_character(s:str,n:int):
    i = 0
    r = ''
    while i < len(s) or i < 0:
        r += s[i]
        i += n
    return r

print(every_nth_character('Computer Science', 3))


