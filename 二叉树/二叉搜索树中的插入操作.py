from base_tree import TreeNode


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        return root

if __name__ == "__main__":
    root = TreeNode(4, left=TreeNode(2, left=TreeNode(1)), right=TreeNode(7))
    solution = Solution()
    my_res = solution.insertIntoBST(root, 5)
    print(my_res)