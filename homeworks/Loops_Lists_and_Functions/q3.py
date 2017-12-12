# Course Code: ICS3U
# Author: jn_xyp
# Version: 2017-11-01
# Loops, Lists and Functions - Question 3


def stretch_string(s, stretch_factors):
    if not len(s) == len(stretch_factors):
        return None
    i = 0
    ans = ''
    while i < len(s):
        ans += s[i] * stretch_factors[i]
    return ans


print(stretch_string('Hello', [2, 0, 3, 1, 1]))
