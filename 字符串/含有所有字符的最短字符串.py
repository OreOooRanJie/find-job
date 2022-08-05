import collections
import math

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_len = len(s)
        t_len = len(t)
        need = t_len
        left = 0
        count = collections.Counter(t)
        start, end = 0, math.inf

        # 窗口右边界开始滑动
        for right in range(s_len):
            char_right = s[right]  # 进入窗口的元素
            if char_right in count:
                if count[char_right] > 0:  # 如果进入窗口的元素在count中的值大于零，说明，该元素是需要的
                    need -= 1  # 新来了一个符合要求的元素，那么需要的元素个数-1
                count[char_right] -= 1

            # 当need==0时，说明left到right这个窗口内包含了t的所有字符，但是可能存在过多的其余字符，需要处理
            while need == 0:
                # 记录下此刻的起止索引
                if right - left < end - start:
                    start, end = left, right
                char_left = s[left]  # 即将弹出窗口的元素
                if char_left in count:
                    if count[char_left] >= 0: # 即将弹出的元素在count中的值大于等于零，代表着该元素刚好满足需要或者对该元素还有需求，那么该元素弹出之后需求会变大，所以需要更新need
                        need += 1
                    count[char_left] += 1
                left += 1  # 收缩滑动窗口
        if end != math.inf:
            return s[start:end + 1]
        return ""


if __name__ == "__main__":
    s = "a"
    t = "aa"
    solution = Solution()
    min_win = solution.minWindow(s, t)
    print(min_win)
