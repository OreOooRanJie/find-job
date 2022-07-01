"""
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""
class Solution:
    def maxSubArray(self, nums):
        lenth = len(nums)
        dp = [[0]*lenth for _ in nums]

        left, right = 0, 0
        for right in range(lenth):
            for left in range(right):
                if right == 0 and left == 0:
                    dp[right][left] = nums[right]
                else:
