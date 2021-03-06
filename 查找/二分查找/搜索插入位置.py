"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

输入: nums = [1,3,5,6], target = 5
输出: 2

author: ranjie
"""


class Solution(object):

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)
        if not end:
            return start
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        while start <= end:
            mid = start + ((end - start) >> 1)
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] == target:
                return mid
        return start


if __name__ == "__main__":
    data = [1, 3, 5, 6]
    select_sort = Solution()
    print(select_sort.searchInsert(data, 2))
