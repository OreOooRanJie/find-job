"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回[-1, -1]。

你必须设计并实现时间复杂度为O(log n)的算法解决此问题。


输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or target < nums[0] or target > nums[-1]:
            return [-1, -1]

        left_limit = self.get_left_limit(nums, target)
        right_limit = self.get_right_limit(nums, target)

        if right_limit == -1:
            return [-1, -1]
        elif right_limit - left_limit > 1:
            return [left_limit + 1, right_limit - 1]
        else:
            return [left_limit, right_limit]


    def get_left_limit(self, nums, target):
        """

        """
        left, right = 0, len(nums) - 1
        res = -1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                res = right
        return res

    def get_right_limit(self, nums, target):
        """

        """
        res = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                res = left
        return res

if __name__ == "__main__":
    data = [1, 3, 3, 3, 6]
    select_sort = Solution()
    print(select_sort.searchRange(data, 0))

# 1 2 3 6 7 8 9 10