"""
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""
class Solution:
    def maxSubArray(self, nums):
        former = 0
        max = nums[0]
        for idx in range(len(nums)):
            if idx == 0:
                cur = nums[0]
                former = cur
            elif nums[idx] >= nums[idx] + former:
                cur = nums[idx]
            else:
                cur = nums[idx] + former
            if cur > max:
                max = cur
            former = cur
        return max


my_solution = Solution()
print(my_solution.maxSubArray([-1]))

