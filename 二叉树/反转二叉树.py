from base_tree import TreeNode


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return

        left_root = self.invertTree(root.left)
        right_root = self.invertTree(root.right)
        root.left, root.right = right_root, left_root

        return root


if __name__ == "__main__":
    tree = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
                    right=TreeNode(3, left=TreeNode(6), right=TreeNode(7)))

    my_solution = Solution()
    my_path = my_solution.invertTree(tree)
    print(my_path)