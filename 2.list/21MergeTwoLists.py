# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        header = ListNode(val = 0)
        node = header
        while list1 or list2:
            if list1 and list2:
                if list1.val >= list2.val:
                    node.next = list2
                    list2 = list2.next
                else:
                    node.next = list1
                    list1 = list1.next
            elif list1:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        return header.next