# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
#
# 叶子节点 是指没有子节点的节点。
#

# 需要遍历整个树，所以递归无返回值
# Definition for a 7.binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def calSum(self, root, count):
        if not root.left and not root.right and not count:
            self.res.append(self.path[:])
            return
        if not root.left and not root.right and count:
            return

        if root.left:
            self.path.append(root.left.val)
            count -= root.left.val
            self.calSum(root.left, count)
            count += root.left.val
            self.path.pop()
        if root.right:
            self.path.append(root.right.val)
            count -= root.right.val
            self.calSum(root.right, count)
            count += root.right.val
            self.path.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        self.path = [root.val]
        self.calSum(root, targetSum - root.val)
        return self.res