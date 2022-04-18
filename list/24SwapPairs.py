# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        header = ListNode(next = head)
        left = header

        while left.next != None and left.next.next != None:
            curr = left.next
            right = curr.next
            post = right.next

            left.next = right
            right.next = curr
            curr.next = post

            left = curr
        return header.next