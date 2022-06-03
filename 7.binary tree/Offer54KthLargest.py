# 给定一棵二叉搜索树，请找出其中第 k 大的节点的值。

# 中序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        res = []
        def traversal(root):
            if not root:
                return
            traversal(root.left)
            res.append(root.val)
            traversal(root.right)
        traversal(root)
        return res[-k]

# 中序遍历倒序，提前返回
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.res = 0
        def traversal(root):
            if not root:
                return
            traversal(root.right)
            if self.k == 0:
                return
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            traversal(root.left)

        self.k = k
        traversal(root)
        return self.res