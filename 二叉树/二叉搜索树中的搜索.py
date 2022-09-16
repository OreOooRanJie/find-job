from base_tree import TreeNode


class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return
        if root.val == val:
            return root
        while root:
            if val > root.val:
                root = root.right
            elif val < root.val:
                root = root.left
            else:
                return root
        return


if __name__ == "__main__":
    root = TreeNode(4, left=TreeNode(2, left=TreeNode(1)), right=TreeNode(7))
    val = 2
    solution = Solution()
    my_res = solution.searchBST(root, val)
    print(my_res)