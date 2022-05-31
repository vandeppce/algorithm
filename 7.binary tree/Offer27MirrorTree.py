# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 这题就是invert二叉树
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def traversal(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            traversal(root.left)
            traversal(root.right)
        traversal(root)
        return root