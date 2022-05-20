# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        leftNode = self.lowestCommonAncestor(root.left, p, q)
        rightNode = self.lowestCommonAncestor(root.right, p, q)

        if leftNode != None and rightNode != None:
            return root
        if leftNode == None and rightNode != None:
            return rightNode
        if leftNode != None and rightNode == None:
            return leftNode
        else:
            return None

