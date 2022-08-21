"""
一个机器人位于一个m x n网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/unique-paths-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # dp定义：到达坐标(row, col)的路径数量
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        if obstacleGrid[0][0]:
            return 0
        # 遍历
        for i in range(row):
            for j in range(col):
                # 选择
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue
                if i == 0:
                    if obstacleGrid[i][j]:
                        dp[i][j] = 0
                        continue
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    if obstacleGrid[i][j]:
                        dp[i][j] = 0
                        continue
                    dp[i][j] = dp[i - 1][j]
                else:
                    if obstacleGrid[i][j]:
                        dp[i][j] = 0
                        continue
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


if __name__ == "__main__":
    solution = Solution()
    res = solution.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    print(res)
