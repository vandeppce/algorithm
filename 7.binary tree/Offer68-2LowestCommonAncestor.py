# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
# 满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
# 例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def traversal(root):
            if not root:
                return None
            if root == p or root == q:
                return root
            left = traversal(root.left)
            right = traversal(root.right)
            if left and not right:
                return left
            if right and not left:
                return right
            if left and right:
                return root

        return traversal(root)