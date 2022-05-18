# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 这里当node1或者node2=header后，即使node1=node1.next，但是header指向的地址不变，所以header仍然是头节点。
# 只是由于在遍历过程中删除了部分节点，所以header指向的是新链表的头
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        header = ListNode(next=head)
        node1 = header
        node2 = header

        for i in range(n):
            node1 = node1.next

        while node1.next != None:
            node2 = node2.next
            node1 = node1.next

        skip = node2.next
        node2.next = skip.next

        return header.next