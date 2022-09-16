"""
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def __init__(self):
        self.map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for item in s:
            if not stack:
                stack.append(item)
            else:
                top_char = stack[-1]
                if top_char == self.map.get(item):
                    del_char = stack.pop()
                else:
                    stack.append(item)
        if not stack:
            return True
        else:
            return False


if __name__ == "__main__":
    s = "(]"
    solution = Solution()
    my_res = solution.isValid(s)
