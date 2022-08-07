from base_tree import TreeNode


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(postorder, 0, len(postorder) - 1, inorder, 0, len(inorder) - 1)

    def helper(self, postorder, p_start, p_end,
               inorder, i_start, i_end):
        if p_start > p_end:
            return None

        root = TreeNode(postorder[p_end])
        root_index = inorder.index(postorder[p_end])
        left_lenth = root_index - i_start

        root.left = self.helper(postorder, p_start, p_start + left_lenth-1, inorder, i_start, root_index - 1)
        root.right = self.helper(postorder, p_start+left_lenth, p_end - 1, inorder, root_index + 1, i_end)

        return root


if __name__ == "__main__":
    postorder = [9, 15, 7, 20, 3]
    inoerder = [9, 3, 15, 20, 7]
    my_solution = Solution()
    my_path = my_solution.buildTree(inoerder, postorder)
    print(my_path)
