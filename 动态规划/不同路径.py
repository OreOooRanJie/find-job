"""
一个机器人位于一个 m x n网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp[i][j]的意义是：到达坐标为(i, j)的路径数
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # 遍历
        for row in range(m):
            for col in range(n):
                # 选择
                # 当坐标为第一行或者第一列的时候，由于机器人只能向下或者向右运动，所以行走路径是唯一的
                if row == 0 or col == 0:
                    dp[row][col] = 1
                else:
                    # 当坐标为(row, col)时，此时的路径数为到达(row-1, col)的路径数
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        return dp[-1][-1]


if __name__ == "__main__":
    m = 3
    n = 2
    solution = Solution()
    res = solution.uniquePaths(m, n)
    print(res)
