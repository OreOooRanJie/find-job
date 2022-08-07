from base_tree import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            if not root:
                res.append("#")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        def dfs(data):
            val = data.pop(0)
            if val == "#":
                return
            root = TreeNode(val)
            root.left = dfs(data)
            root.right = dfs(data)
            return root
        return dfs(data)


if __name__ == "__main__":
    tree = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
                    right=TreeNode(3, left=TreeNode(6), right=TreeNode(7)))

    solution = Codec()
    my_serialize = solution.serialize(tree)
    print(my_serialize)
    my_deserialize = solution.deserialize(my_serialize)
    print(my_deserialize)