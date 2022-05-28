# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

# Definition for singly-linked 2.list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        node = head
        while node != None:
            last = node.next
            node.next = prev
            prev = node
            node = last
        return prev