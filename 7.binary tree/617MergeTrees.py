# 给你两棵二叉树： root1 和 root2 。
#
# 想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。
# 你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；
# 否则，不为 null 的节点将直接作为新二叉树的节点。
#
# 返回合并后的二叉树。
#

# 同时遍历两个树
# Definition for a 7.binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1

        mergeRoot = TreeNode()
        mergeRoot.val = root1.val + root2.val
        mergeRoot.left = self.mergeTrees(root1.left, root2.left)
        mergeRoot.right = self.mergeTrees(root1.right, root2.right)

        return mergeRoot