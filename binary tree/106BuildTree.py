# 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历，
# postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 从后序的最后一个数开始
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return

        rootNode = postorder[-1]
        root = TreeNode(val=rootNode)

        splitIdx = inorder.index(rootNode)

        leftTreeInorder = inorder[:splitIdx]
        rightTreeInorder = inorder[splitIdx + 1:]

        leftTreePostorder = postorder[:splitIdx]
        rightTreePostorder = postorder[splitIdx:-1]

        root.left = self.buildTree(leftTreeInorder, leftTreePostorder)
        root.right = self.buildTree(rightTreeInorder, rightTreePostorder)

        return root