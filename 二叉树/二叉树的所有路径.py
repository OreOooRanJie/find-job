"""
给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。

叶子节点 是指没有子节点的节点。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        self.dfs(root, [], res)
        return res

    def dfs(self, root, tmp_res, res):
        tmp_res.append(str(root.val))
        if not root.left and not root.right:
            res.append("->".join(tmp_res))
            return
        if root.left:
            # 递归的结果如果用列表（可变数据类型）来存放，那么在调用递归函数的时候实际上是在不断的覆盖，因为此时调用栈中存放的信息是对列表的
            # 引用，相当于浅拷贝。
            self.dfs(root.left, tmp_res, res)
            # 当遍历到叶子节点的时候，需要将临时列表中的元素回退一个
            tmp_res.pop()
        if root.right:
            self.dfs(root.right, tmp_res, res)
            tmp_res.pop()

if __name__ == "__main__":
    tree = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
                    right=TreeNode(3, left=TreeNode(6), right=TreeNode(7)))

    my_solution = Solution()
    my_path = my_solution.binaryTreePaths(tree)
    print(my_path)
