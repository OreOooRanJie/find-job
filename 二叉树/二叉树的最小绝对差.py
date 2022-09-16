from base_tree import TreeNode

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return

        left = self.getMinimumDifference(root.left)
        val = root.val
        right = self.getMinimumDifference(root.right)

if __name__ == "__main__":
    root = TreeNode(4, left=TreeNode(2, left=TreeNode(1, right=TreeNode(3))), right=TreeNode(6))
    solution = Solution()
    my_res = solution.getMinimumDifference(root)
    print(my_res)