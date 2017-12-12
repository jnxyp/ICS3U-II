# Course Code: ICS3U
# Author: jn_xyp
# Version: 2017-11-02
# Problem Set 5 - Question 3

def modify(nums):
    i = 0
    while i < len(nums):
        if nums[i] % 2 == 0:
            nums.insert(i+1, 0)
            i += 1
        i += 1
    return nums


print(modify([1,2,3,4,5,6,7,8,9]))