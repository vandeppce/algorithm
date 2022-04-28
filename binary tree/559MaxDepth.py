# 给定一个 N 叉树，找到其最大深度。
#
# 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
#
# N 叉树输入按层序遍历序列化表示，每组子节点由空值分隔（请参见示例）。
#

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        layerRes = []
        if root.children:
            for node in root.children:
                layerRes.append(self.maxDepth(node))
            return max(layerRes) + 1
        else:
            return self.maxDepth(root.children) + 1