class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        def reverse(ls):
            left, right = 0, len(ls) - 1
            while left <= right:
                ls[left], ls[right] = ls[right], ls[left]
                left += 1
                right -= 1
            return ls
        tmp = []
        fast, slow = 0, 0
        while fast <= len(s)-1:
            if s[fast] == " ":
                tmp.append(s[slow:fast])
                while s[fast] == " ":
                    fast += 1
                slow = fast
            fast += 1
        return " ".join(reverse(tmp))


if __name__ == "__main__":
    s = "a good   example"
    select_sort = Solution().reverseWords(s)
    s.split()
    import heapq
    print(11)