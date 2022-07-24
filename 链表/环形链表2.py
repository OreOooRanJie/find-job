"""
判断链表是否成环，如果成环，返回入环节点
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head
        while (1):
            if not (fast and fast.next):
                return
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break
        fast = head
        while (fast != slow):
            fast, slow = fast.next, slow.next
        return fast

