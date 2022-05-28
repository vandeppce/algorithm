# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

"""
# 数组模拟
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = [head.val]
        while head.next != None:
            head = head.next
            nums.append(head.val)
        return nums == nums[::-1]

"""

"""
# 分成如下几步
# 用快慢指针，快指针有两步，慢指针走一步，快指针遇到终止位置时，慢指针就在链表中间位置
# 同时用pre记录慢指针指向节点的前一个节点，用来分割链表
# 将链表分为前后均等两部分，如果链表长度是奇数，那么后半部分多一个节点
# 将后半部分反转 ，得cur2，前半部分为cur1
# 按照cur1的长度，一次比较cur1和cur2的节点数值
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True
        slow, fast = head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        
        pre.next = None # 分割链表
        cur1 = head # 前半部分
        cur2 = self.reverseList(slow) # 反转后半部分，总链表长度如果是奇数，cur2比cur1多一个节点
        while cur1:
            if cur1.val != cur2.val:
                return False
            cur1 = cur1.next
            cur2 = cur2.next
        return True

    def reverseList(self, head: ListNode) -> ListNode:
        cur = head   
        pre = None
        while(cur!=None):
            temp = cur.next # 保存一下cur的下一个节点
            cur.next = pre # 反转
            pre = cur
            cur = temp
        return pre
"""