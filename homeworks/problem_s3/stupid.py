class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = {}
        for n in nums:
            s[len(s)] = n
        s = sorted(s, key=s.get)
        i, j = 0, 0
        print(s)


print(Solution().twoSum([11, -2,12,343,53], 9))