"""
给你一个字符串 s ，请你将该字符串划分成一个或多个 子字符串 ，并满足每个子字符串中的字符都是 唯一 的。也就是说，在单个子字符串中，字母的出现次数都不超过 一次 。

满足题目要求的情况下，返回 最少 需要划分多少个子字符串。

注意，划分后，原字符串中的每个字符都应该恰好属于一个子字符串。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/optimal-partition-of-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def partitionString(self, s: str) -> int:

        return self.helper(s, [], 0)

    def helper(self, s, res, count):

        for i in range(len(s)):
            if s[i] not in res:
                res.append(s[i])
            else:
                return self.helper(s[i:], [], count + 1)
        return count + 1


if __name__ == "__main__":
    s = "cuieokbs"
    solution = Solution()
    my_res = solution.partitionString(s)
    print(my_res)
