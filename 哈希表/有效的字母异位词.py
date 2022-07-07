"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若s 和 t中每个字符出现的次数都相同，则称s 和 t互为字母异位词。

"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_map, t_map = {}, {}
        for i in range(len(s)):
            if s[i] in s_map:
                s_map[s[i]] += 1
            else:
                s_map[s[i]] = 1

            if t[i] in t_map:
                t_map[t[i]] += 1
            else:
                t_map[t[i]] = 1

        # 实际上这里可以直接判断t_map == s_map 是否成立
        # map里面顺序不一致不影响比较结果
        for key, value in s_map.items():
            if t_map.get(key) != value:
                return False
        return True


if __name__ == "__main__":
    s = "aacc"
    t = "ccac"
    select_sort = Solution().isAnagram(s, t)
    print(11)