class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        count = {}
        left = 0
        res = 0
        for right in range(len_s):
            char_right = s[right]

            # 当前字符如果不在count中，则说明是个新的元素，需要加入
            # 窗口右边界的滑动不需要做异常处理，异常处理交给窗口的左边界的收缩来控制
            if char_right not in count:
                count[char_right] = 1
            else:
                count[char_right] += 1

            if right - left + 1 > len(count):  # 当窗口大小大于count中键值的数量时，代表窗口内有重复元素，不合法
                char_left = s[left]
                count[char_left] -= 1
                if count[char_left] == 0:  # 当某字符串在count中的值为零时，代表着窗口内没有该元素了，不需要维护，所以需要将其删除
                    del count[char_left]
                left += 1  # 通过收缩窗口来达到窗口合法的控制

            # 当窗口合法了之后来计算正确结果
            res = max(right - left + 1, res)

        return res


if __name__ == "__main__":
    s = "abcabcbb"
    solution = Solution()
    min_win = solution.lengthOfLongestSubstring(s)
    print(min_win)