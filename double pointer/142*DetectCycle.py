# 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
# 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
# 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 判断是否有环
        header = ListNode(next=head)
        nodeA = header
        nodeB = header

        while nodeB.next != None:
            nodeA = nodeA.next
            nodeB = nodeB.next.next

            if nodeB == None:
                return None

            if nodeA == nodeB:
                nodeA = header
                while nodeA != nodeB:
                    nodeA = nodeA.next
                    nodeB = nodeB.next

                return nodeA

        return None

"""
# 二刷
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        header = ListNode(val = 0, next = head)
        slow = header
        fast = header
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                slow = header
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None
"""