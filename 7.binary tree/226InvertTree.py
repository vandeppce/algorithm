# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
# 前序遍历，先反转，然后深度优先搜索

# Definition for a 7.binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(root):
            if root == None:
                return
            root.left, root.right = root.right, root.left
            invert(root.left)
            invert(root.right)
        invert(root)
        return root

"""
# 二刷，带返回值
# Definition for a 7.binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        leftNode = self.invertTree(root.right)
        rightNode = self.invertTree(root.left)

        root.left = leftNode
        root.right = rightNode
        return root
"""

"""
二刷，迭代，前序遍历
# Definition for a 7.binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        stack = [root]
        while stack:
            node = stack.pop(0)
            node.left, node.right = node.right, node.left
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return root
"""