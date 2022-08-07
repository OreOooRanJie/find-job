from base_tree import TreeNode


class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not preorder and not postorder:
            return None
        return self.helper(preorder, 0, len(preorder) - 1, postorder, 0, len(postorder) - 1)

    def helper(self, preorder, pre_start, pre_end, postorder, post_start, post_end):
        if pre_start > pre_end:
            return None

        if pre_start == pre_end:
            return TreeNode(preorder[pre_start])

        root = TreeNode(preorder[pre_start])
        left_root_val = preorder[1 + pre_start]
        left_root_idx = postorder.index(left_root_val)

        left_size = left_root_idx - post_start + 1

        root.left = self.helper(preorder, pre_start + 1, pre_start + left_size, postorder, post_start, left_root_idx)
        root.right = self.helper(preorder, pre_start + left_size + 1, pre_end, postorder, left_root_idx+1, post_end - 1)

        return root


if __name__ == "__main__":
    postorder = [4, 5, 2, 6, 7, 3, 1]
    preordre = [1, 2, 4, 5, 3, 6, 7]
    my_solution = Solution()
    my_path = my_solution.constructFromPrePost(preordre, postorder)
    print(my_path)
