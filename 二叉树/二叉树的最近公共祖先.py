from base_tree import TreeNode


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left

if __name__ == "__main__":
    p = TreeNode(5, right=TreeNode(6), left=TreeNode(2, right=TreeNode(7), left=TreeNode(3)))
    q = TreeNode(1, left=TreeNode(0), right=TreeNode(8))
    root = TreeNode(3, left=TreeNode(5, right=TreeNode(6), left=TreeNode(2, right=TreeNode(7), left=TreeNode(3))),
                    right=TreeNode(1, left=TreeNode(0), right=TreeNode(8)))
    solution = Solution()
    my_res = solution.lowestCommonAncestor(root, p, q)
