"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
"""


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        m = len(matrix)  # 行
        n = len(matrix[0])  # 列
        l, r, t, b = 0, n - 1, 0, m - 1
        val = 1
        res = []
        while val <= n * m:
            # left to right
            i = l
            while i < r + 1 and len(res) < m * n:
                res.append(matrix[t][i])
                val += 1
                i += 1
            t += 1
            # top to bottom
            i = t
            while i < b + 1 and len(res) < m * n:
                res.append(matrix[i][r])
                val += 1
                i += 1
            r -= 1
            # right to left
            i = r
            while i > l - 1 and len(res) < m * n:
                res.append(matrix[b][i])
                val += 1
                i -= 1
            b -= 1
            # bottom to top
            i = b
            while i > t - 1 and len(res) < m * n:
                res.append(matrix[i][l])
                val += 1
                i -= 1
            l += 1
        return res
