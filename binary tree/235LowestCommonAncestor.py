# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
# 根据搜索树的性质判断
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return

        if root.val > p.val and root.val > q.val:
            leftNode = self.lowestCommonAncestor(root.left, p, q)
            if leftNode:
                return leftNode
        elif root.val < p.val and root.val < q.val:
            rightNode = self.lowestCommonAncestor(root.right, p, q)
            if rightNode:
                return rightNode
        else:
            return root