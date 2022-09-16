"""
给你一个整数数组 nums ，返回出现最频繁的偶数元素。

如果存在多个满足条件的元素，只需要返回 最小 的一个。如果不存在这样的元素，返回 -1 。


"""


class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for num in nums:
            if num % 2 == 0:
                if num not in dict:
                    dict[num] = 1
                else:
                    dict[num] += 1
        max_value = -float("inf")
        res = float("inf")
        for key, value in dict.items():
            if value > max_value:
                max_value = value
                res = key
            if value == max_value:
                res = min(key, res)
        return -1 if res == float("inf") else res