from base_tree import TreeNode


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        return self.helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def helper(self, preorder, start_p, end_p, inorder, start_i, end_i):
        if start_p > end_p:
            return
        root = TreeNode(preorder[start_p])
        root_index = inorder.index(preorder[start_p])
        lenth = root_index - start_i
        root.left = self.helper(preorder, start_p + 1, start_p + lenth, inorder, start_i, root_index - 1)
        root.right = self.helper(preorder, 1 + lenth + start_p, end_p, inorder, root_index + 1,
                                 end_i)
        return root


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inoerder = [9, 3, 15, 20, 7]
    my_solution = Solution()
    my_path = my_solution.buildTree(preorder, inoerder)
    print(my_path)
