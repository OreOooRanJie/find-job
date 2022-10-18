"""
如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。

字母和数字都属于字母数字字符。

给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。

作者：力扣 (LeetCode)
链接：https://leetcode.cn/leetbook/read/top-interview-questions/xah8k6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        a_z_0 = 97
        a_z_1 = 122
        A_Z_0 = 65
        A_Z_1 = 90
        num_0 = 48
        num_9 = 57
        res = ""
        for char in s:
            if a_z_0 <= ord(char) <= a_z_1 or A_Z_0 <= ord(char) <= A_Z_1 or num_0 <= ord(char) <= num_9:
                res += char.lower()
        return res == res[::-1]


if __name__ == "__main__":
    s = "race a car"
    solution = Solution()
    my_res = solution.isPalindrome(s)
    print(my_res)
