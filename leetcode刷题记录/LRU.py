class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.cache = DoubleList()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        # 若目标键在map中，那么代表着可以访问。
        # get获取的节点是最新访问的节点，那么需要将该节点挪到链表尾部
        # 1.在原来的双向链表中删除该节点
        # 2.在队尾添加该节点
        self.makeRecently(key)
        return self.map[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            # 若新增的key在map中，那么则是对原有节点的更新
            # 按照最近访问原则，需要将该节点放到队尾
            # 1.在原链表中删除该节点
            # 2.在链表尾部加入该节点
            self.deleteKey(key)
            self.addRecently(key, value)
            return

        if self.cap == self.cache.size:
            # 当容量已满，则需要删除掉队首节点
            self.removeLeastRecently()

        self.addRecently(key, value)
        return

    def makeRecently(self, key):
        temp = self.map[key]
        self.cache.remove(temp)
        self.cache.addLast(temp)

    def addRecently(self, key, val):
        temp = Node(key, val)
        self.cache.addLast(temp)
        self.map[key] = temp

    def deleteKey(self, key):
        temp = self.map[key]
        self.cache.remove(temp)
        del self.map[key]

    def removeLeastRecently(self):
        temp = self.cache.removeFirst()
        temp_key = temp.key
        del self.map[temp_key]


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class DoubleList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addLast(self, new_node: Node):
        # 这里的tail.prev不能直接等于head，在初始化新增节点的时候，尾节点的前一个节点确实是head节点，但是有节点新增之后，再新增节点时，
        # 尾节点的前一个节点就不是head了，而是新增的节点，所以这里用tail.prev
        # 这里的语句更新的是new_node中的prev和next，另其分别指向尾节点的上一个节点和尾节点
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        # 这里的语句更新的是尾节点的上一个节点的next和尾节点的prev，令其都指向新增节点，这样就将新增节点嵌入到双向链表的结构中了
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        # 更新链表的大小
        self.size += 1

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        # 这里的意义是将node和双向链表的联系断开
        node.prev = None
        node.next = None
        self.size -= 1

    def removeFirst(self):
        if self.head.next == self.tail:
            return None

        first = self.head.next
        self.remove(first)

        return first


if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    lru.get(1)
    lru.put(3, 3)
