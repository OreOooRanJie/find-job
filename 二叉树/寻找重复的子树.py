from base_tree import TreeNode


class Solution(object):
    def __init__(self):
        self.dict = {}
        self.res = []

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return '#'

        left = self.helper(root.left)
        right = self.helper(root.right)

        my_seri = left + "," + right + "," + str(root.val)

        if self.dict.get(my_seri, 0) == 1:
            self.res.append(root)

        self.dict[my_seri] = self.dict.get(my_seri, 0) + 1

        return my_seri


if __name__ == "__main__":
    root = TreeNode(2, left=TreeNode(2, left=TreeNode(3)), right=TreeNode(2, left=TreeNode(3)))
    solution = Solution()
    my_res = solution.findDuplicateSubtrees(root)
    print(my_res)
