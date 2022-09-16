class Solution(object):
    def superEggDrop(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        # 定义：dp[i][j]：可以使用i个鸡蛋，在不高于j层楼的情况下找到f的最小操作数
        # dp[1][1] = 1
        # 第i个鸡蛋在第j层楼扔下有两种情况
        # 1. 碎