"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs_1(self, n):
        memo = [-1] * (n + 1)
        return self.helper(n, memo)

    def helper(self, n, memo):
        if n == 0 or n == 1:
            return 1
        if memo[n] == -1:
            memo[n] = self.helper(n - 1, memo) + self.helper(n - 2, memo)
        else:
            # 此时递归还没结束
            return memo[n]
        # 此时递归结束，memo更新完成，只需要返回第n个值即可
        return memo[n]

    


if __name__ == "__main__":
    solution = Solution()
    res = solution.climbStairs_1(3)
    print(res)
