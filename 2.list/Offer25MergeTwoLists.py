# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 伪头节点，双指针
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        header = ListNode(val = 0)
        node = header
        while l1 and l2:
            if l1.val >= l2.val:
                node.next = l2
                l2 = l2.next
            else:
                node.next = l1
                l1 = l1.next
            node = node.next
        if l1:
            node.next = l1
        else:
            node.next = l2
        return header.next