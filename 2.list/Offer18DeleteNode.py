# 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
#
# 返回删除后的链表的头节点。
#
# 注意：此题对比原题有改动

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        header = ListNode(val = 0, next = head)
        node = header
        while node and node.next:
            if node.next.val == val:
                node.next = node.next.next
            node = node.next
        return header.next