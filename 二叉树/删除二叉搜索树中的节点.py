from base_tree import TreeNode


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root

        if root.val == key:
            # 左右节点都为空，说明该节点为叶子节点，可以直接删除
            if not root.right and not root.left:
                return None
            # 如果左节点非空，右节点为空，
            if not root.right and root.left:
                return root.left

            if not root.left and root.right:
                return root.right

            if root.left and root.right:

                left = root.left
                node = root.right
                while node.left:
                    node = node.left
                node.left = left
                root = root.right
                return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        return root


if __name__ == "__main__":
    root = TreeNode(50, left=TreeNode(30, right=TreeNode(40)), right=TreeNode(70, left=TreeNode(60), right=TreeNode(80)))
    val = 50
    solution = Solution()
    my_res = solution.deleteNode(root, val)