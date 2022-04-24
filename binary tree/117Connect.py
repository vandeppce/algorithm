# 给定一个二叉树
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
# 初始状态下，所有 next 指针都被设置为 NULL。

# 与116完全一样（迭代法）

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = [root]
        prev = None

        while queue:
            for i in range(len(queue)):
                if i == 0:
                    node = queue.pop(0)
                else:
                    node = queue.pop(0)
                    prev.next = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                prev = node
        return root