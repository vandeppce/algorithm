# 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
#
# 完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，
# 并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
#

# 设置全局变量，类似前序遍历，每遍历一个节点计数值+1

# Definition for a 7.binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cnt = 0

    def countNodes(self, root: TreeNode) -> int:
        def count(root):
            if not root:
                return 0
            self.cnt += 1
            count(root.left)
            count(root.right)
            return self.cnt
        return count(root)

# 递归，左子树+右子树
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def count(root):
            if not root:
                return 0
            leftCount = count(root.left)
            rightCount = count(root.right)
            return leftCount + rightCount + 1

        return count(root)