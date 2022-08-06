from base_tree import TreeNode


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        left_flatten_res = self.flatten(root.left)
        right_flatten_res = self.flatten(root.right)

        root.left = None
        root.right = left_flatten_res
        p = root
        while p.right:
            p = p.right
        p.right = right_flatten_res

        return root


if __name__ == "__main__":
    tree = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
                    right=TreeNode(3, left=TreeNode(6), right=TreeNode(7)))

    my_solution = Solution()
    my_path = my_solution.flatten(tree)
    print(my_path)
