# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

# Definition for singly-linked list.

# 使用虚拟头部

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        header = ListNode(next=head)
        curr = header

        while curr.next != None:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return header.next

"""
# 二刷
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        header = ListNode(val = 0, next = head)
        prev = header
        node = head
        while node:
            if node.val == val:
                node = node.next
            else:
                prev.next = node
                prev = node
                node = node.next
        prev.next = node
        return header.next
"""