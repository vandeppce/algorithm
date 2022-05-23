# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：
#
# L0 → L1 → … → Ln - 1 → Ln
# 请将其重新排列后变为：
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#

# 方式一，这种方式得到的右侧数组会比左侧多，处理起来很麻烦
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next:
            slow = head
            fast = head
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            # 反转后半数组
            prev.next = None

            pre = None
            while slow:
                tmp = slow.next
                slow.next = pre
                pre = slow
                slow = tmp
            slow = pre

            # 连接
            head2 = slow
            while head and head.next:
                next1 = head.next
                next2 = head2.next
                head.next = head2
                head2.next = next1
                head = next1
                head2 = next2

            if head2.next:
                head2.next.next = None
                head.next = head2
            else:
                head2.next = None
                head.next = head2

# 方式二，这种方式是左侧比右侧多，简单
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 切开
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None

        # 反转右边
        prev = None
        while right:
            nxt = right.next
            right.next = prev
            prev = right
            right = nxt

        # 插入
        while prev:
            next1 = head.next
            next2 = prev.next
            head.next = prev
            prev.next = next1
            head = next1
            prev = next2

# 方式三，双向队列
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 节点入栈
        node = head
        stack = []
        while node.next:
            stack.append(node.next)
            node = node.next

        # 重新构造链表
        while stack:
            # 弹出栈顶
            node1 = stack.pop()
            head.next = node1
            head = head.next

            # 弹出栈尾
            if stack:
                node2 = stack.pop(0)
                head.next = node2
                head = head.next
        head.next = None