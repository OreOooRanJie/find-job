"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        root.next = None

        def helper(node1, node2):
            if not node2:
                return

            node1.next = node2

            helper(node1.left, node1.right)
            helper(node2.left, node2.right)
            helper(node1.right, node2.left)

        helper(root.left, root.right)
        return root
