"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
输入：head = [1,2,3,4,5], n = 2 输出：[1,2,3,5]

输入：head = [1], n = 1 输出：[]

输入：head = [1,2], n = 1 输出：[1]

解题思路：
快慢指针，慢指针指向虚拟节点，快指针指向虚拟节点的下一个节点，先让慢指针保持不懂，当快指针移动n个节点之后，慢指针跟快指针一起移动，
当快指针为None时，即快指针走到了链表尾部，此时慢指针刚好与快指针相差n+1个节点，此时只需要慢指针指向下下个节点即可

"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        i = 0
        res = ListNode(next=head)
        pre = res
        cur = pre.next
        if cur.next is None:
            return None
        while cur is not None:
            if i >= n:
                break
            cur = cur.next
            i += 1
        while cur is not None:
            cur = cur.next
            pre = pre.next

        pre.next = pre.next.next
        return res.next


if __name__ == "__main__":
    node = ListNode(1, ListNode(3))
    n = 2
    select_sort = Solution().removeNthFromEnd(node, n)
    print(11)
