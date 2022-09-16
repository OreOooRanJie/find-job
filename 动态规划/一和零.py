"""
给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。

如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/ones-and-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int 0的个数
        :type n: int 1的个数
        :rtype: int
        """
        lenth = len(strs)
        # dp[i][j][k]的意义是：在前i个字符串中，使用j个0和k个1的情况下的最多字符串个数
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(lenth + 1)]

        for i in range(1, lenth+1):
            # 第i个字符的0和1的个数
            zero_nums = strs[i-1].count("0")
            one_nums = len(strs[i-1]) - zero_nums
            for j in range(m+1):  # 这里为什么取m+1 和 n+1，原因是：当j==m和k==n时，是合法的
                for k in range(n+1):
                    # 初始状态
                    if i == 0:
                        dp[i][j][k] = 0
                    elif j < zero_nums or k < one_nums:
                        dp[i][j][k] = dp[i - 1][j][k]
                    else:
                        # 两种情况，取较大者：
                        # 1. 选择第i个字符，那么dp[i][j][k]等于上一个状态+1
                        # 2. 不选择第i个字符
                        dp[i][j][k] = max(dp[i - 1][j - zero_nums][k - one_nums] + 1, dp[i - 1][j][k])
        return dp[lenth][m][n]


if __name__ == "__main__":
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    my_solution = Solution()
    res = my_solution.findMaxForm(strs, m, n)
