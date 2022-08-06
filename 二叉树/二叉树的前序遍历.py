from base_tree import TreeNode


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return None
        self.res.append(root.val)
        self.helper(root.left)
        self.helper(root.right)


if __name__ == "__main__":
    tree = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
                    right=TreeNode(3, left=TreeNode(6), right=TreeNode(7)))

    my_solution = Solution()
    my_path = my_solution.preorderTraversal(tree)
    print(my_path)

