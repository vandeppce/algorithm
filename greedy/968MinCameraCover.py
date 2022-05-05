# 给定一个二叉树，我们在树的节点上安装摄像头。
#
# 节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。
#
# 计算监控树的所有节点所需的最小摄像头数量。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 贪心算法，后序遍历二叉树，节点共有三种状态
# Definition: 0, not covered; 1, cameraed; 2, covered
class Solution:
    def __init__(self):
        self.count = 0

    def minCameraCover(self, root: TreeNode) -> int:
        count = 0

        def traversal(root):
            if not root:
                return 2

            left = traversal(root.left)
            right = traversal(root.right)

            if left == 2 and right == 2:
                root.val = 0
            elif left == 0 or right == 0:
                # left == 2 and right == 0
                # left == 0 and right == 2
                # left == 1 and right == 0
                # left == 0 and right == 1
                # left == 0 and right == 0
                root.val = 1
                self.count += 1
            elif left == 1 or right == 1:
                root.val = 2
            return root.val

        rootRet = traversal(root)
        if not rootRet:
            self.count += 1
        return self.count