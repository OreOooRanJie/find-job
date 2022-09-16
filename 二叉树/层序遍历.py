from base_tree import TreeNode

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        deq = [root]
        while deq:
            tmp = []
            for _ in range(len(deq)):
                cur_node = deq.pop(0)
                tmp.append(cur_node.val)
                if cur_node.left:
                    deq.append(cur_node.left)
                if cur_node.right:
                    deq.append(cur_node.right)
            res.append(tmp)
        return res