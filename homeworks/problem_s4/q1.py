# Course Code: ICS3U
# Author: jn_xyp
# Version: 2017-10-18
# Problem Set 4 - Question 1

# a)
def _a(s: str):
    i = 0
    out = ''
    while i < len(s):
        if s[i] != str(i):
            out = out + s[i]
        i = i + 1
    return out


# Test Case
print(_a('15273'))
print(_a('351575908'))


# b)
def _b(num: int):
    num = str(num) # convert input integer to string
    num_max = 0 # the largest digit of number in num
    # find out the value of largest digit in num
    # e.g. the largest digit of 54321 is 5
    # check if each number from 1 to num_max is in the input number
    for n in range(1, len(num)+1):
        if not str(n) in num:
            return False
    return True


# Test Case
print(_b(12345))
print(_b(54321))
print(_b(15243))
print(_b(12456))


# c)
def _c(s: str):
    # if the previous character in string is a space
    prev_is_space = False
    out = ''
    for c in s:
        # if c is a space and
        if c == ' ' and not prev_is_space:
            prev_is_space = True
            out = out + ' '
        elif c != ' ':
            prev_is_space = False
            out = out + c
    return out

# Test Case
print(_c('   testing   123     hello'))
