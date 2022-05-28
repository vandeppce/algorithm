# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
#
# 高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。
#
# 类似654题思路，从有序数组中间取值作为根结点，左侧区间为左子树，右侧区间为右子树，递归构建树
# Definition for a 7.binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return

        mid_idx = len(nums) // 2

        rootNode = TreeNode(val = nums[mid_idx])
        leftNode = self.sortedArrayToBST(nums[:mid_idx])
        rightNode = self.sortedArrayToBST(nums[mid_idx + 1:])

        rootNode.left = leftNode
        rootNode.right = rightNode
        return rootNode