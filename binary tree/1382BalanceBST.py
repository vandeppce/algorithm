# 给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。如果有多种构造方法，请你返回任意一种。
#
# 如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 平衡的 。
#

# 中序遍历+重构
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
        def traversal(root):
            if not root:
                return
            traversal(root.left)
            nums.append(root.val)
            traversal(root.right)
        traversal(root)
        def construct(nums):
            if not nums:
                return
            mid = len(nums) // 2
            root = TreeNode(val = nums[mid])
            root.left = construct(nums[:mid])
            root.right = construct(nums[mid + 1:])
            return root
        return construct(nums)