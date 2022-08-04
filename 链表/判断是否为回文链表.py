# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        self.left = head

        def check(head):
            if not head:
                return True
            res = check(head.next)
            res = res & (self.left.val == head.val)
            self.left = self.left.next
            return res

        return check(head)


if __name__ == "__main__":
    head = ListNode(1, next=ListNode(2, next=ListNode(9, ListNode(1))))
    my_solution = Solution()
    my_ans = my_solution.isPalindrome(head)
    print(my_ans)
