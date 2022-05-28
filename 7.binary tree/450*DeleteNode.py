# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，
# 并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
#
# 一般来说，删除节点可分为两个步骤：
#
# 首先找到需要删除的节点；
# 如果找到了，删除它。
#
# 递归返回值接住新子树
# Definition for a 7.binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return

        if root.val == key:
            if not root.left and not root.right:
                return
            if not root.left and root.right:
                return root.right
            if not root.right and root.left:
                return root.left
            if root.left and root.right:
                curr = root.right
                while curr.left:
                    curr = curr.left
                curr.left = root.left
                return root.right

        if root.val > key:
            leftNode = self.deleteNode(root.left, key)
            root.left = leftNode
        else:
            rightNode = self.deleteNode(root.right, key)
            root.right = rightNode
        return root