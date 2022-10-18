class Solution:
    def solveNQueens(self, n: int):
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(row: int):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                for i in range(n):
                    # i为列
                    # i in columns 判断的是是否有同列的元素
                    # row - i in diagonal1 判断的是向右斜线上有没有元素（因为在向右斜线上有 行坐标-纵坐标 等值的情况）
                    # row + i in diagonal2 判断的是向左斜线上有没有元素（因为在向左斜线上有 行坐标+纵坐标 等值的情况）
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    queens[row] = i  # 记录：第row行上的元素在第i列
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)

        solutions = list()
        queens = [-1] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        row = ["."] * n
        backtrack(0)
        return solutions


if __name__ == "__main__":
    solution = Solution()
    my_res = solution.solveNQueens(5)
