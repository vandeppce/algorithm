class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.num = 0

    def get(self, index: int) -> int:
        if 0 <= index < self.num:
            node = self.head.next
            for i in range(self.num):
                if i == index:
                    return node.val
                node = node.next
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        node = self.head
        nextNode = node.next
        addNode = Node(val=val, next=nextNode)
        node.next = addNode
        self.num += 1

    def addAtTail(self, val: int) -> None:
        addNode = Node(val=val)
        node = self.head

        while node.next != None:
            node = node.next
        node.next = addNode
        self.num += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
        elif index == self.num:
            self.addAtTail(val)
        elif index > self.num:
            pass
        else:
            node = self.head
            for i in range(index):
                node = node.next
            prev_node = node
            last_node = node.next
            addNode = Node(val=val, next=last_node)
            prev_node.next = addNode
            self.num += 1

    def deleteAtIndex(self, index: int) -> None:
        node = self.head
        if 0 <= index < self.num:
            for i in range(index):
                node = node.next
            prev_node = node
            last_node = node.next.next
            prev_node.next = last_node
            self.num -= 1