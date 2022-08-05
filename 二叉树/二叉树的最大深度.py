from base_tree import TreeNode

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1


if __name__ == "__main__":
    tree = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
                    right=TreeNode(3, left=TreeNode(6), right=TreeNode(7)))

    my_solution = Solution()
    my_path = my_solution.maxDepth(tree)
    print(my_path)
