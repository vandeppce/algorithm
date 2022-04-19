# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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