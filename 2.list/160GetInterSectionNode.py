# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

# 和剑指offer02-07一样
# Definition for singly-linked 2.list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        headerA = ListNode(val=0, next=headA)
        headerB = ListNode(val=0, next=headB)

        lengthA = 0
        lengthB = 0

        nodeA = headerA
        nodeB = headerB

        while nodeA.next != None:
            lengthA += 1
            nodeA = nodeA.next

        while nodeB.next != None:
            lengthB += 1
            nodeB = nodeB.next

        if lengthA > lengthB:
            diff = lengthA - lengthB
            nodeA = headerA.next
            nodeB = headerB.next
            for i in range(diff):
                nodeA = nodeA.next

            for i in range(lengthB):
                if nodeA == nodeB:
                    return nodeA

                nodeA = nodeA.next
                nodeB = nodeB.next

        else:
            diff = lengthB - lengthA
            nodeA = headerA.next
            nodeB = headerB.next
            for i in range(diff):
                nodeB = nodeB.next

            for i in range(lengthA):
                if nodeA == nodeB:
                    return nodeA

                nodeA = nodeA.next
                nodeB = nodeB.next

        return None