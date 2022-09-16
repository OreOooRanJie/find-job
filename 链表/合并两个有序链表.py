"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。


"""

from base_listnode import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if not l1:
        #     return l2  # 终止条件，直到两个链表都空
        # if not l2:
        #     return l1
        # if l1.val <= l2.val:  # 递归调用
        #     l1.next = self.mergeTwoLists(l1.next,l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1,l2.next)
        #     return l2
        return self.helper(l1,l2,ListNode(-1), ListNode(-2))

    def helper(self, l1, l2, node1, node2):
        if not l1:
            return l2  # 终止条件，直到两个链表都空
        if not l2:
            return l1
        if l1.val <= l2.val:  # 递归调用
            node1.next = self.helper(l1.next,l2, node1, node2)
            return node1
        else:
            node2.next = self.helper(l1,l2.next,node1, node2)
            return node2

if __name__ == "__main__":
    list1 = ListNode(1, next=ListNode(2, next=ListNode(4)))
    list2 = ListNode(1, next=(ListNode(3, next=ListNode(4))))
    solution = Solution()
    my_res = solution.mergeTwoLists(list1, list2)
    print(my_res)
