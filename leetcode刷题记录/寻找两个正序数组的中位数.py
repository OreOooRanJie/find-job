"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组nums1 和nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

例如：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

author: ranjie
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        def get_kth_value(k):
            index1, index2 = 0, 0
            while 1:
                if index1 == len(nums1):
                    return nums2[index2 + k - 1]
                elif index2 == len(nums2):
                    return nums1[index1 + k - 1]
                elif k == 1:
                    return min(nums1[index1], nums2[index2])
                newindex1 = min(index1 + k // 2 - 1, len(nums1) - 1)
                newindex2 = min(index2 + k // 2 - 1, len(nums2) - 1)
                # [1,2,3,4,5] [2,3,4,5]
                if nums1[newindex1] <= nums2[newindex2]:
                    k -= newindex1 - index1+ 1
                    index1 = newindex1 + 1
                else:
                    k -= newindex2 - index2 + 1
                    index2 = newindex2 + 1

        total_len = len(nums1) + len(nums2)

        if total_len % 2 == 1:
            return get_kth_value((total_len+1) // 2)
        else:
            return (get_kth_value(total_len // 2) + get_kth_value(total_len // 2 + 1)) / 2

my_solution = Solution()
print(my_solution.findMedianSortedArrays([1,2], [3,4]))