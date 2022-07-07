"""
判断一个链表是否成环

解题思路：
快慢指针，快指针一定会追上慢指针，当重合时候的节点不为None，则存在环
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        fast = head.next
        slow = head
        while (fast != slow):
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
