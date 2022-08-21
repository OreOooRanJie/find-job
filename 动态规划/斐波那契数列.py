"""
斐波那契数（通常用F(n) 表示）形成的序列称为 斐波那契数列 。该数列由0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1)= 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给定n ，请计算 F(n) 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/fibonacci-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 0:
            return n
        return self.fib(n-1) + self.fib(n-2)

    def fib_1(self, n):
        """
        备忘录，自顶向下
        :param n:
        :return:
        """
        memo = [-1] * (n + 1)
        res = self.help(n, memo)
        return res

    def help(self, n, memo):
        if n == 1 or n == 0:
            return n

        if memo[n] == -1:
            memo[n] = self.help(n-1, memo) + self.help(n-2, memo)
        else:
            return memo[n]

        return memo[n]

    def fib_2(self, n):
        """
        dp数组，自底向上
        :param n:
        :return:
        """
        # 初始化
        dp = [0] * 2
        # 遍历
        for i in range(n + 1):
            # 选择
            if i == 0 or i == 1:
                dp[i] = i
            else:
                # 状态转移
                sum = dp[0] + dp[1]
                dp[0] = dp[1]
                dp[1] = sum
        return dp[1]


if __name__ == "__main__":
    solution = Solution()
    res = solution.fib_2(4)
    print(res)