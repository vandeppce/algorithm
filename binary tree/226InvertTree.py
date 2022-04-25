# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
# 前序遍历，先反转，然后深度优先搜索

# Definition for a binary tree node.
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