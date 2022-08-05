import collections

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # 数据准备
        s_len = len(s)
        p_len = len(p)
        count = collections.Counter(p)
        need = p_len
        res = []
        # 窗口展开
        for right in range(s_len):

            char_right = s[right]  # 新加入窗口的元素
            if char_right in count:
                if count[char_right] > 0:
                    need -= 1
                count[char_right] -= 1

            # 因为是固定窗口长度，所以实际上窗口不用收缩，只需要当有元素离开窗口时，动态更新need和count即可
            left = right - p_len
            if left >= 0:
                char_left = s[left]
                if char_left in count:
                    if count[char_left] >= 0:
                        need += 1
                    count[char_left] += 1
                # left += 1

            if need == 0:
                res.append(left + 1)

        return res



if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    solution = Solution()
    min_win = solution.findAnagrams(s, p)
    print(min_win)