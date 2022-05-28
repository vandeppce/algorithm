# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

# 快慢指针

# Definition for singly-linked 2.list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        header = ListNode(0, next=head)
        slow = header
        fast = header

        for i in range(n):
            fast = fast.next

        while fast.next != None:
            slow = slow.next
            fast = fast.next

        skip = slow.next.next
        slow.next = skip
        return header.next