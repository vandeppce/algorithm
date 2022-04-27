# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
#
# 有效 二叉搜索树定义如下：
#
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
#
# 判断中序遍历的结果是否递增
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traversal(root):
            if not root:
                return
            traversal(root.left)
            nums.append(root.val)
            traversal(root.right)

        nums = []
        traversal(root)

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                return False

        return True