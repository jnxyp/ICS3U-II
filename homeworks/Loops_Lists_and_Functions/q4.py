# Course Code: ICS3U
# Author: jn_xyp
# Version: 2017-11-01
# Loops, Lists and Functions - Question 4


def greatest_difference(num1, num2):
    if not len(num1) == len(num2):
        return None
    i = 0
    max_diff = 0
    while i < len(num1):
        diff = abs(num1[i] - num2[i])
        if diff > max_diff:
            max_diff = diff
        i += 1
    return max_diff


print(greatest_difference([1, 2, 3], [6, 8, 10]))
