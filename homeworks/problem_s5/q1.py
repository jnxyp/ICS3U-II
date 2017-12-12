# Course Code: ICS3U
# Author: jn_xyp
# Version: 2017-11-02
# Problem Set 5 - Question 1

nums = [1,2,3,4,5,6,7,8,9]

# for i in range(0,10):
#     nums.append(int(input()))

print(nums)

def _sum(nums):
    s = 0
    for n in nums:
        s += n
    return s

def _average(nums):
    return _sum(nums) / len(nums)

def _highest_and_lowest(nums):
    max, min = 0,0
    for n in nums:
        if n > max:
            max = n
        if n < min:
            min = n
    return [max,min]

def _count_odd_and_even(nums):
    odd = 0
    for n in nums:
        if not n % 2 == 0:
            odd += 1

    return [odd, len(nums) - odd]



print(_sum(nums))
print(_average(nums))
print(_highest_and_lowest(nums))
print(_count_odd_and_even(nums))
