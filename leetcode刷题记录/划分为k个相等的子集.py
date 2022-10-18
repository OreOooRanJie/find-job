class Solution:
    def canPartitionKSubsets(self, nums, k):
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        target = total_sum // k

    def helper(self, target, nums, ):


if __name__ == "__main__":
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    solution = Solution()
    my_res = solution.canPartitionKSubsets()
