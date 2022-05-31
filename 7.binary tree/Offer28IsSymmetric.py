# 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def compare(left, right):
            if left and not right:
                return False
            if not left and right:
                return False
            if not left and not right:
                return True
            if left.val != right.val:
                return False

            resIn = compare(left.right, right.left)
            resOut = compare(left.left, right.right)
            return resIn and resOut

        if not root:
            return True
        return compare(root.left, root.right)