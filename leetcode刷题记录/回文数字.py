class Solution:
    def isPalindrome(self, x: int) -> bool:
        if isinstance(x, int):
            str_x = str(x)
        else:
            str_x = x
        if len(str_x) < 2:
            return True
        if str_x[0] == str_x[-1]:
            return self.isPalindrome(str_x[1:-1])
        else:
            return False

my_solution = Solution()
print(my_solution.isPalindrome(11))