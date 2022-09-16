"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请

你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for index in range(len(nums)-2):
            target = -nums[index]
            if index > 0 and nums[index] == nums[index - 1]: continue
            left, right = index + 1, len(nums) - 1
            while right > left:
                if nums[left] + nums[right] == target:

                    res.append([nums[index], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                else:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res


if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    solution = Solution()
    my_res = solution.threeSum(nums)
    print(my_res)
