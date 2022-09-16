from base_tree import TreeNode


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = []
        self.helper(root)
        return self.is_sorted()

    def helper(self, root):
        if not root:
            return
        # 中序遍历
        self.helper(root.left)
        self.res.append(root.val)
        self.helper(root.right)

    def is_sorted(self):

        for i in range(1, len(self.res)):
            if self.res[i] <= self.res[i - 1]:
                return False
        return True


if __name__ == "__main__":
    root = TreeNode(5, left=TreeNode(4), right=TreeNode(6, left=TreeNode(3, right=TreeNode(7))))
    solution = Solution()
    my_res = solution.isValidBST(root)
    print(my_res)
