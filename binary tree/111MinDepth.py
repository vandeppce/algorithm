# 给定一个二叉树，找出其最小深度。
#
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# 说明：叶子节点是指没有子节点的节点。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 迭代法，遇见左右子节点均为空时直接返回
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        count = 0
        while queue:
            count += 1
            for i in range(len(queue)):
                node = queue.pop(0)
                if not node.left and not node.right:
                    return count
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        return count
