"""
给你一个大小为 n下标从 0开始的整数数组nums和一个正整数k。

对于k <= i < n - k之间的一个下标i，如果它满足以下条件，我们就称它为一个好下标：

下标 i 之前 的 k个元素是 非递增的。
下标 i 之后的 k个元素是 非递减的。
按 升序返回所有好下标。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-all-good-indices
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def goodIndices(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        for right in range(k, len(nums)):
            left_array = nums[right - k:right]
            if right + k + 1 < len(nums):
                right_array = nums[right + 1:right + k + 1]
