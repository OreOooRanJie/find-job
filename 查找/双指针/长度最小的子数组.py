"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s
的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
"""


class Solution(object):
    def minSubArrayLen(self, target, nums) -> int:
        res = float("inf")
        Sum = 0
        index = 0
        for i in range(len(nums)):
            Sum += nums[i]
            while Sum >= target:
                res = min(res, i-index+1)
                Sum -= nums[index]
                index += 1
        return 0 if res==float("inf") else res


if __name__ == "__main__":
    data = [1, 4, 4]  # 9,1,0,9,100
    select_sort = Solution()
    print(select_sort.minSubArrayLen(4, data))
