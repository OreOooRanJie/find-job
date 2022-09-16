class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # dp[i][j]: 到坐标(i,j)位置的最小路径和
        dp = [[10000] * (len(grid[0]) + 1) for _ in range(len(grid) + 1)]

        for i in range(1, len(grid) + 1):
            for j in range(1, len(grid[0]) + 1):
                if i == 1 and j == 1:
                    dp[i][j] = grid[i - 1][j - 1]
                else:
                    # 向右或者向下，取最小值
                    dp[i][j] = min(dp[i][j - 1] + grid[i - 1][j - 1], dp[i - 1][j] + grid[i - 1][j - 1])
        return dp[-1][-1]


if __name__ == "__main__":
    grid = [[1, 2, 3], [4, 5, 6]]
    solution = Solution()
    my_res = solution.minPathSum(grid)
    print(my_res)
