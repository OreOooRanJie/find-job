"""
给你两个非空的链表，表示两个非负的整数。它们每位数字都是按逆序的方式存储的，并且每个节点只能存储一位数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。
例如：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

链表实际上是类对象的嵌套[val, next = ListNode(val)]，每一个next都是一个ListNode对象

author: ranjie
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = cur = ListNode()
        carry = 0
        while l1 or l2:
            if l1 and l2:
                sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1 == None:
                sum = l2.val + carry
                l2 = l2.next
            else:
                sum = l1.val + carry
                l1 = l1.next
            carry, rest = divmod(sum, 10)
            cur.next = ListNode(rest)
            cur = cur.next
        if carry:
            cur.next = ListNode(1)
        return ans.next


