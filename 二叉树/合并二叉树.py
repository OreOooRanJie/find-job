from base_tree import TreeNode


class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """

        if not root1:
            return root2
        if not root2:
            return root1

        val1 = root1.val
        val2 = root2.val

        root = TreeNode(val2 + val1)

        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)

        return root


if __name__ == "__main__":
    root1 = TreeNode(1, left=TreeNode(3, left=TreeNode(5)), right=TreeNode(2))
    root2 = TreeNode(2, left=TreeNode(1, right=TreeNode(4)), right=TreeNode(3, right=TreeNode(7)))
    solution = Solution()
    my_res = solution.mergeTrees(root1, root2)
    print(my_res)
