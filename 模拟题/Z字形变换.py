class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
        比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
        P   A   H   N
        A P L S I I G
        Y   I   R
        """
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)

    def convert1(self, s: str, numRows: int) -> str:
        n, r = len(s), numRows
        if r == 1 or r >= n:
            return s
        t = r * 2 - 2
        ans = []
        for i in range(r):  # 枚举矩阵的行
            for j in range(0, n - i, t):  # 枚举每个周期的起始下标
                ans.append(s[j + i])  # 当前周期的第一个字符
                if 0 < i < r - 1 and j + t - i < n:
                    ans.append(s[j + t - i])  # 当前周期的第二个字符
        return ''.join(ans)


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 5
    solution = Solution()
    my_res = solution.convert1(s, numRows)
