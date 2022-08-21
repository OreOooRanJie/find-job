"""
给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。

返回 你可以获得的最大乘积 。
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(i):
                # 选择：
                # 当i-j不继续分解时，当前乘积为j*(i-j)
                # 当i-j继续分解时，当前乘积为j * dp[i-j]
                # 当整数为i时，为了保证取到1 - i中的最大乘积，所以一直维护dp[i]的最大特性
                # 例如： 当i=5，j=3，i-j=2时，dp[i]=6；当j=4，i-j=1时，dp[i]=4。
                # 即当遍历完1-i时，最大值可能产生在中间的情况中
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]


if __name__ == "__main__":
    solution = Solution()
    res = solution.integerBreak(10)
    print(res)