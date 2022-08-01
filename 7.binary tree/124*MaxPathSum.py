# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
#
# 路径和 是路径中各节点值的总和。
#
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。
#

# 注意中间有个贪心的策略，就是当返回值小于0时，便不再考虑该分支
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxSum = -1000
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxOneSide(root):
            if not root:
                return 0
            left = max(0, maxOneSide(root.left))
            right = max(0, maxOneSide(root.right))
            self.maxSum = max(self.maxSum, left + right + root.val)
            return max(left, right) + root.val
        maxOneSide(root)
        return self.maxSum