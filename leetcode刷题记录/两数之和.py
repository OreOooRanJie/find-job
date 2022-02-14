"""
简单的两数之和，返回满足要求的数的下标

可以暴力循环，两个循环，平方级的复杂度；
也可以用hash表将问题转换为一个查询的问题，这里的hash表相当于一个记忆存储器，将遍历过的存在hash表中，方便查询

author: ranjie
"""


class Solution:
    def twoSum(self, nums, target):
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []


if __name__ == '__main__':
    mysolution = Solution()
    print(mysolution.twoSum([3,2,4], 6))