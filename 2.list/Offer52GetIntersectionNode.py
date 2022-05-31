# 输入两个链表，找出它们的第一个公共节点。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodeA = headA
        nodeB = headB
        lengthA = 0
        lengthB = 0
        while nodeA:
            lengthA += 1
            nodeA = nodeA.next
        while nodeB:
            lengthB += 1
            nodeB = nodeB.next
        if lengthA < lengthB:
            headA, headB = headB, headA
            lengthA, lengthB = lengthB, lengthA
        for i in range(lengthA - lengthB):
            headA = headA.next
        for i in range(lengthB):
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None