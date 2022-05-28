# 给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。
#
# 树的序列化输入是用层序遍历，每组子节点都由 null 值分隔

# 把二叉树中左右节点换成孩子节点

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]

        while queue:
            tmp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.children:
                    for child in node.children:
                        queue.append(child)
            res.append(tmp)
        return res