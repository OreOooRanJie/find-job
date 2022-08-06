from base_tree import TreeNode


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.max = 0
        self.helper(root)
        return self.max

    def helper(self, root):
        # 无需理会具体的递归细节，只需要按照函数定义去写逻辑就好了
        if not root:
            return 0
        left_depth = self.helper(root.left)  # 左子树的最大深度
        right_depth = self.helper(root.right)  # 右子树的最大深度
        self.max = max(left_depth + right_depth, self.max)  # 求解左右子树最大深度之和，去掉这一行，实际上这个helper是在求解二叉树的最大深度
        return max(left_depth, right_depth) + 1  # 计算左右子树的最大深度，+1是加上根节点的深度


if __name__ == "__main__":
    tree = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
                    right=TreeNode(3, left=TreeNode(6), right=TreeNode(7)))

    my_solution = Solution()
    my_path = my_solution.diameterOfBinaryTree(tree)
    print(my_path)
