"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]

解题思路：
可以用暴力解决，直接排序，例如归并排序就是O(n)的排序算法

可以利用辅助空间+双指针，两头向中间遍历，将较大者填入辅助空间即可
"""


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        ans = [0] * len(nums)
        pos = len(nums) - 1
        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                ans[pos] = nums[left] ** 2
                left += 1
            elif nums[left] ** 2 <= nums[right] ** 2:
                ans[pos] = nums[right] ** 2
                right -= 1
            pos -= 1
        return ans

    def merge_sort(self, nums):
        """

        :param nums:
        :return:
        """



if __name__ == "__main__":
    data = [-7, -3, 2, 3, 11]  # 9,1,0,9,100
    select_sort = Solution()
    print(select_sort.sortedSquares(data))
