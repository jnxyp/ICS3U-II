# Course Code: ICS3U
# Author: jn_xyp
# Version: 2017-11-02
# Problem Set 5 - Question 2


fib_nums = [1, 1]

while len(fib_nums) <= 20:
    fib_nums.append(fib_nums[-1] + fib_nums[-2])


print(fib_nums)