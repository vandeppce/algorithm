# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。
# 判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。
#
# 叶子节点 是指没有子节点的节点。
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def calSum(root, count):
            if not root.left and not root.right and not count:
                return True
            if not root.left and not root.right and count:
                return False

            if root.left:
                count = count - root.left.val
                ret = calSum(root.left, count)
                if ret:
                    return True
                count = count + root.left.val
            if root.right:
                count = count - root.right.val
                ret = calSum(root.right, count)
                if ret:
                    return True
                count = count + root.right.val

            return False

        if not root:
            return False
        else:
            return calSum(root, targetSum - root.val)