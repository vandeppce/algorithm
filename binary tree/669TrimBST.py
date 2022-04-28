# 给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low, high]中。
# 修剪树 不应该 改变保留在树中的元素的相对结构 (即，如果没有被移除，原有的父代子代关系都应当保留)。 可以证明，存在 唯一的答案 。
#
# 所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。
#

# 对于某个节点若小于low，则其左节点必小于low，遍历其右节点即可；若其大于high，则其右节点必大于high，遍历左子树即可
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return

        if root.val < low:
            r = self.trimBST(root.right, low, high)
            return r

        if root.val > high:
            l = self.trimBST(root.left, low, high)
            return l

        leftNode = self.trimBST(root.left, low, high)
        root.left = leftNode

        rightNode = self.trimBST(root.right, low, high)
        root.right = rightNode

        return root