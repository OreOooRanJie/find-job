"""
给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。

你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。

请你计算并返回达到楼梯顶部的最低花费。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/min-cost-climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        nums = len(cost)
        # dp[i]代表的意思是：上到第i个台阶所花费的最小代价
        dp = [0] * nums

        for i in range(1, nums):
            if i == 1:
                dp[i] = min(cost[1], cost[0])
            else:
                dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i - 1])

        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
    res = solution.minCostClimbingStairs([10, 15, 20])
    print(res)
