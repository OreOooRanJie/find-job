from base_tree import TreeNode


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        max_value = max(nums)
        max_node = TreeNode(max_value)
        max_value_index = nums.index(max_value)
        left = self.constructMaximumBinaryTree(nums[:max_value_index])
        right = self.constructMaximumBinaryTree(nums[max_value_index + 1:])
        max_node.left = left
        max_node.right = right
        return max_node


if __name__ == "__main__":
    nums = [3, 2, 1, 6, 0, 5]
    solution = Solution()
    my_res = solution.constructMaximumBinaryTree(nums)
    print(my_res)
