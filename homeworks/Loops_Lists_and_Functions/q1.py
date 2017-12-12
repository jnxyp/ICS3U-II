# Course Code: ICS3U
# Author: jn_xyp
# Version: 2017-11-01
# Loops, Lists and Functions - Question 1


def collect_underperformers(nums, threshold):
    ans = []
    for n in nums:
        if n < threshold:
            ans.append(n)
    return ans


print(collect_underperformers([1, 2, 3, 4], 3))
