class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        count = {}  # 维护的是滑动窗口内的数据情况，根据count来判断窗口是否合法（即满足题目要求）
        res = 0
        left = 0
        for right in range(len_s):
            # 当前字符
            chr_right = s[right]
            count[chr_right] = count.get(chr_right, 0) + 1

            # 如果当前的窗口非法时，需要收缩窗口，保证窗口的合法性
            while right - left + 1 > len(count):
                chr_left = s[left]
                count[chr_left] -= 1
                if count[chr_left] == 0:
                    del count[chr_left]
                left += 1

            # 窗口调整为合法之后，判断当前长度是否为最长
            res = max(right - left + 1, res)

        return res


if __name__ == "__main__":
    s = "pwwek"
    solution = Solution()
    min_win = solution.lengthOfLongestSubstring(s)