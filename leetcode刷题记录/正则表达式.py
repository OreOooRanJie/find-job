"""
给你一个字符串s和一个字符规律p，请你来实现一个支持 '.'和'*'的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖整个字符串s的，而不是部分字符串。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/regular-expression-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # if p == ".*":
        #     return True

        stack_s, stack_p = [], []

        for i in s:
            stack_s.append(i)

        for i in p:
            stack_p.append(i)

        while stack_s:
            cur_char = stack_s.pop()
            cur_rule = stack_p.pop()

            if cur_rule == "*":
                # do something
                cur_rule = stack_p.pop()
                if cur_rule == "*":
                    return False
                else:


                pass
            elif cur_rule == ".":
                # do something
                pass
            else:
                if cur_char != cur_rule:
                    return False



if __name__ == "__main__":
    s = ""
    solution = Solution()
    my_res = solution.isMatch()