
import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        m, n = len(s1), len(s2)
        if m > n:
            return False

        cnt = collections.Counter(s1)  # 哈希表：记录需要匹配到的各个字符的数目
        need = m  # 记录需要匹配到的字符总数【need=0表示匹配到了】

        for right in range(n):

            # 窗口右边界
            ch = s2[right]  # 窗口中新加入的字符
            if ch in cnt:  # 新加入的字符ch位于s1中
                if cnt[ch] > 0:  # 此时新加入窗口中的字符ch对need有影响
                    need -= 1
                cnt[ch] -= 1

            # 窗口左边界
            left = right - m
            if left >= 0:
                ch = s2[left]
                if ch in cnt:  # 刚滑出的字符位于s1中
                    if cnt[ch] >= 0:  # 此时滑出窗口的字符ch对need有影响
                        need += 1
                    cnt[ch] += 1

            if need == 0:  # 找到了一个满足题意的窗口
                return True

        return False

if __name__ == "__main__":
    t = "AOBCODEBAC"
    s = "ABC"
    solution = Solution()
    min_win = solution.checkInclusion(s, t)