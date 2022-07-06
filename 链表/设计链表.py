"""
设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val和next。val是当前节点的值，next是指向下一个节点的指针/引用。
如果要使用双向链表，则还需要一个属性prev以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。

在链表类中实现这些功能：

get(index)：获取链表中第index个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为val的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第index个节点之前添加值为val 的节点。如果index等于链表的长度，则该节点将附加到链表的末尾。如果 index
大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引index 有效，则删除链表中的第index 个节点。

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):
    def __init__(self):
        self.head = ListNode()
        self.size = 0

    def get(self, index):
        """
        获取链表中第index个节点的值
        index无效则返回-1
        :param index:
        :return: int
        """
        if index >= self.size or index < 0:
            return -1
        head = self.head
        for i in range(index + 1):
            head = head.next
        return head.val

    def addAtHead(self, val):
        """
        在第一个节点之前新增一个节点
        :param val:
        :return: None
        """
        head = self.head
        to_add = ListNode(val)
        to_add.next = head.next
        head.next = to_add
        self.size += 1

    def addAtTail(self, val):
        """
        在尾节点之后新增一个节点
        :param val:
        :return:
        """
        head = self.head
        while head.next is not None:
            head = head.next
        head.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index, val):
        """
        在第index节点之前新增一个节点
        index大于链表长度时，不新增；
        index小于零时，新增在首节点之前
        index等于链表长度则新增在尾节点之后
        :param index:
        :param val:
        :return: None
        """
        if index > self.size:
            return
        if index <= 0:
            return self.addAtHead(val)
        if index == self.size:
            return self.addAtTail(val)
        head = self.head
        for i in range(index):
            head = head.next
        to_add = ListNode(val)
        to_add.next = head.next
        head.next = to_add
        self.size += 1

    def deleteAtIndex(self, index):
        """
        如果index有效，则删除掉第index个节点
        :param index:
        :return: None
        """
        if index >= self.size or index < 0:
            return
        head = self.head
        for i in range(index):
            head = head.next
        head.next = head.next.next
        self.size -= 1




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)