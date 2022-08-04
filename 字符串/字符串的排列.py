import collections


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_len, s2_len = len(s1), len(s2)
        count = collections.Counter(s1)
        need = s1_len

        for right in range(s2_len):
            chr_s2 = s2[right]
            if chr_s2 in count:
                if count[chr_s2] > 0:
                    need -= 1
                count[chr_s2] -= 1

            # 处理窗口非法的情况
            left = right - s1_len
            if left >= 0:
                chr_left = s2[left]
                if chr_left in count:
                    if count[chr_left] >= 0:
                        need += 1
                    count[chr_left] += 1

            # 当need==0时，则代表匹配成功
            if need == 0:
                return True
        return False


if __name__ == "__main__":
    t = "eidbaooo"
    s = "ab"
    solution = Solution()
    min_win = solution.checkInclusion(s, t)