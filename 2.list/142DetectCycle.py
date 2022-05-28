# 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

# Definition for singly-linked 2.list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        header = ListNode(val=0, next=head)
        slow = header
        fast = header

        if head == None:
            return None

        while fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if fast == None:
                return None

            if slow == fast:
                slow = header
                while True:
                    slow = slow.next
                    fast = fast.next

                    if slow == fast:
                        return slow

        return None

"""
# 二刷
# Definition for singly-linked 2.list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        header = ListNode(next = head)
        slow = header
        fast = header

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = header
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
"""