"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

解题思路：
可以换个角度思考，将A链表和B链表收尾相连，形成一个环。两条链表可以假想为两个人在同向而行，链表长度不一代表着速度不一致，但是慢的总会被快的追上。
当相遇的时候即是相交的时候。只需要返回当前节点即可。
"""


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        dummy_A = headA
        dummy_B = headB
        while dummy_A != dummy_B:
            dummy_A = dummy_A.next if dummy_A else headB
            dummy_B = dummy_B.next if dummy_B else headA
        # 当A节点和B节点相遇，则直接返回当前节点A或者B即可
        return dummy_A