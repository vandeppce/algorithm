# 给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
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