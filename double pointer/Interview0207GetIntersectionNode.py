# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        headerA = ListNode(next=headA)
        headerB = ListNode(next=headB)
        nodeA = headerA
        nodeB = headerB

        # A长度
        lengthA = 0
        while nodeA.next != None:
            nodeA = nodeA.next
            lengthA += 1

        # B长度
        lengthB = 0
        while nodeB.next != None:
            nodeB = nodeB.next
            lengthB += 1

        # 长度差
        diff = lengthA - lengthB
        if diff < 0:
            headA, headB = headB, headA

        # A移动到等长位置
        for i in range(abs(diff)):
            headA = headA.next

        # 判断
        for i in range(min(lengthA, lengthB)):
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next

        return None