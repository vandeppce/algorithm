# 给定一个二叉树，判断它是否是高度平衡的二叉树。
#
# 本题中，一棵高度平衡二叉树定义为：
#
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

# 判断左右子树高度
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 求深度，前序遍历，求高度，后序遍历
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getHeight(root):
            if not root:
                return 0
            leftHeight = getHeight(root.left)
            rightHeight = getHeight(root.right)
            if leftHeight == -1:
                return -1
            if rightHeight == -1:
                return -1
            if abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1
        height = getHeight(root)
        if height == -1:
            return False
        else:
            return True