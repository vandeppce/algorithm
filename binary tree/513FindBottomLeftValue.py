# 给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。
#
# 假设二叉树中至少有一个节点。

# 层序遍历，记录每一层第一个节点的值
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        ret = 0
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if i == 0:
                    ret = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ret