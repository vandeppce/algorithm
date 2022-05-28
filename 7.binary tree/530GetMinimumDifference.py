# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
#
# 差值是一个正数，其数值等于两值之差的绝对值。
# 中序遍历的结果递增，遍历判断即可
# Definition for a 7.binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def traversal(root):
            if not root:
                return

            traversal(root.left)
            nums.append(root.val)
            traversal(root.right)

        nums = []
        traversal(root)

        minDiff = float("inf")
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] < minDiff:
                minDiff = nums[i] - nums[i - 1]
        return minDiff