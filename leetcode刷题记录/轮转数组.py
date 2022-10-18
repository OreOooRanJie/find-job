"""
给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lenth = len(nums)
        k_position = lenth - k % lenth
        left1, right1 = 0, k_position - 1
        self.reverse(nums, left1, right1)
        left2, right2 = k_position, lenth - 1
        self.reverse(nums, left2, right2)
        left3, right3 = 0, lenth - 1
        self.reverse(nums, left3, right3)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    solution = Solution()
    my_res = solution.rotate(nums, k)
    print(nums)
