from base_tree import TreeNode


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if not left and not right:
            return True
        if not left and right:
            return False
        if not right and left:
            return False

        return left.val == right.val and self.helper(left.left, right.right) and self.helper(left.right, right.left)


if __name__ == "__main__":
    root = TreeNode(1, left=TreeNode(2, right=TreeNode(3)),
                    right=TreeNode(2, right=TreeNode(3)))
    solution = Solution()
    my_res = solution.isSymmetric(root)
    print(my_res)
