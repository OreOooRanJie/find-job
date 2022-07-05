"""
给你一个链表的头节点 head 和一个整数 val ，
请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val):
        if not head:
            return head
        res = ListNode(0, head)
        pre = res
        while head is not None:
            if head.val == val:
                pre.next = head.next
                head = head.next
            else:
                head = head.next
                pre = pre.next
        return res.next