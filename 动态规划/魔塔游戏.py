class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        # dp[i][j]表示走到坐标为(i,j)的位置至少需要的血量
        dp = [[-10000] * (len(grid[0]) + 1) for _ in range(len(grid) + 1)]

        for i in range(1, len(dp) + 1):
            for j in range(1, len(dp[0]) + 1):
                if i == 1 and j == 1:
                    dp[i][j] = dungeon[i - 1][j - 1]
                else:
                    # 两种走法，向右或者向下
                    dp[i][j] = dp[]

if __name__ == "__main__":
    grid = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]

    solution = Solution()
    my_res = solution.calculateMinimumHP(grid)
