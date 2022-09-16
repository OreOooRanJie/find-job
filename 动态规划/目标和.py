"""
给你一个整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加'+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/target-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        total = sum(nums)
        if total < abs(target):
            return 0
        if (total + target) % 2:
            return 0
        cap = min((total - target) >> 1, (total + target) >> 1)
        # 定义dp数组：dp[i][j]的意义为：从前 i 个数字中选出若干个，使得被选出的数字其和为 j 的方案数目。
        dp = [[0] * (cap + 1) for _ in range(n + 1)]
        # 初始化
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(cap + 1):
                if j < nums[i - 1]:  # 容量有限，无法选择第i个数字nums[i-1]
                    dp[i][j] = dp[i - 1][j]
                else:  # 可选择第i个数字nums[i-1]，也可不选【两种方式之和】
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]

        return dp[-1][-1]


if __name__ == "__main__":
    nums = [100]
    target = -200
    solution = Solution()
    res = solution.findTargetSumWays(nums, target)
    print(res)
