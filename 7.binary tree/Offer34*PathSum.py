# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
#
# 叶子节点 是指没有子节点的节点。
#
# 回溯
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def backtracking(self, root, target, total):
        if total == target:
            if not root.left and not root.right:
                self.res.append(self.path[:])
                return

        if root.left:
            self.path.append(root.left.val)
            total += root.left.val
            self.backtracking(root.left, target, total)
            total -= root.left.val
            self.path.pop()
        if root.right:
            self.path.append(root.right.val)
            total += root.right.val
            self.backtracking(root.right, target, total)
            total -= root.right.val
            self.path.pop()

    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:
            return self.res
        self.path.append(root.val)
        self.backtracking(root, target, root.val)
        return self.res