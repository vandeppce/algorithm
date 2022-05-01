# 给定二叉树的根节点 root ，返回所有左叶子之和。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 左子树和右子树分别递归
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftSum = self.sumOfLeftLeaves(root.left)
        rightSum = self.sumOfLeftLeaves(root.right)

        currentVal = 0
        if root.left and not root.left.left and not root.left.right:
            currentVal = root.left.val
        return leftSum + rightSum + currentVal

"""
# 二刷
class Solution:
    def __init__(self):
            self.total = 0

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def traversal(root):
            if not root:
                return 
            if root.left and not root.left.left and not root.left.right:
                self.total += root.left.val
            traversal(root.left)
            traversal(root.right)
        traversal(root)
        return self.total
"""