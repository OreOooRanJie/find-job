import collections


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        m, n = len(s), len(p)
        p_count = collections.Counter(p)
        nead = n
        res = []

        for right in range(m):
            chr_right = s[right]
            if chr_right in p_count:
                if p_count[chr_right] > 0:
                    nead -= 1
                p_count[chr_right] -= 1

            left = right - n
            if left >= 0:
                chr_left = s[left]
                if chr_left in p_count:
                    if p_count[chr_left] >= 0:
                        nead += 1
                    p_count[chr_left] += 1

            if nead == 0:
                res.append(left + 1)

        return res


if __name__ == "__main__":
    t = "cbaebabacd"
    s = "abc"
    solution = Solution()
    min_win = solution.findAnagrams(t, s)