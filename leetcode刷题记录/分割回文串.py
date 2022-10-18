"""
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

回文串 是正着读和反着读都一样的字符串。
"""
import copy


class Solution:
    def partition(self, s: str):
        if len(s) <= 1:
            return 0
        res = []
        result = 10e9
        self.helper(s, [], res)
        for item in res:
            result = min(len(item), result)
        return result

    def helper(self, s, path, res):
        if not s:
            res.append(copy.deepcopy(path))
            return
        for i in range(1, len(s) + 1):
            if self.is_alindrome(s[:i]):
                path.append(s[:i])
                self.helper(s[i:], path, res)
                path.pop()

    def is_alindrome(self, s):
        return s == s[::-1]


if __name__ == "__main__":
    s = "aab"
    solution = Solution()
    my_res = solution.partition(s)
    print(my_res)
