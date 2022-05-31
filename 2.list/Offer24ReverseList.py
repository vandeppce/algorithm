# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

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