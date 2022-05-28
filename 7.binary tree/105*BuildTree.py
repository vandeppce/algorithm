# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
#

# 从前序数组的首位开始
# Definition for a 7.binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return

        rootVal = preorder[0]
        splitIdx = inorder.index(rootVal)
        rootNode = TreeNode(val=rootVal)

        leftTreeInorder = inorder[:splitIdx]
        rightTreeInorder = inorder[splitIdx + 1:]

        leftTreePreorder = preorder[1: splitIdx + 1]
        rightTreePreorder = preorder[splitIdx + 1:]

        rootNode.left = self.buildTree(leftTreePreorder, leftTreeInorder)
        rootNode.right = self.buildTree(rightTreePreorder, rightTreeInorder)

        return rootNode