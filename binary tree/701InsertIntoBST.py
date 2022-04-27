# 给定二叉搜索树（BST）的根节点 root 和要插入树中的值 value ，将值插入二叉搜索树。
# 返回插入后二叉搜索树的根节点。 输入数据 保证 ，新值和原始二叉搜索树中的任意节点值都不同。
#
# 沿二叉树搜索，遇到空的位置即为插入位置返回即可
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            node = TreeNode(val=val)
            return node

        if root.val > val:
            ret = self.insertIntoBST(root.left, val)
            root.left = ret
            return root
        else:
            ret = self.insertIntoBST(root.right, val)
            root.right = ret
            return root