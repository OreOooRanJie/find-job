"""
给你一个长度为 n 的整数数组 nums 。

考虑 nums 中进行 按位与（bitwise AND）运算得到的值 最大 的 非空 子数组。

换句话说，令 k 是 nums 任意 子数组执行按位与运算所能得到的最大值。那么，只需要考虑那些执行一次按位与运算后等于 k 的子数组。
返回满足要求的 最长 子数组的长度。

数组的按位与就是对数组中的所有数字进行按位与运算。

子数组 是数组中的一个连续元素序列。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/longest-subarray-with-maximum-bitwise-and
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #
        max_value = -1
        res = -1
        lenth = 0

        for right in range(len(nums)):
            right_value = nums[right]

            if right_value > max_value:
                left = right
                max_value = right_value
                lenth = right - left + 1
                res = lenth
            elif right_value == max_value:
                lenth += 1
                res = max(lenth, res)
            else:
                lenth = 0
        return res


if __name__ == "__main__":
    nums = [96317, 96317, 96317, 96317, 96317, 96317, 96317, 96317, 96317, 279979]
    solution = Solution()
    my_res = solution.longestSubarray(nums)
    print(my_res)
