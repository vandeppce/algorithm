# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        header = ListNode(val = 0, next = l1)
        head = header
        node1 = l1
        node2 = l2
        prev = 0
        while node1 or node2:
            if node1 and node2:
                curr = node1.val + node2.val + prev
                val = curr % 10
                prev = curr // 10
                node1 = node1.next
                node2 = node2.next
            elif node1:
                curr = node1.val + prev
                val = curr % 10
                prev = curr // 10
                node1 = node1.next
            else:
                curr = node2.val + prev
                val = curr % 10
                prev = curr // 10
                node2 = node2.next
            head.next = ListNode(val = val)
            head = head.next
        if prev:
            head.next = ListNode(val = prev)
        return header.next