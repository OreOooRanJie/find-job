"""
给定一个长度为 n 的整数数组height。有n条垂线，第 i 条线的两个端点是(i, 0)和(i, height[i])。

找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

"""


class Solution:
    def maxArea(self, height: [int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        if len(height) < 1:
            return 0
        while left < right:
            if height[left] > height[right]:
                max_area = max(max_area, (right - left) * height[right])
                right -= 1
            else:
                max_area = max(max_area, (right - left) * height[left])
                left += 1
        return max_area

my_solution = Solution()
print(my_solution.maxArea([1,8,6,2,5,4,8,3,7]))