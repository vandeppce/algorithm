# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。
# 判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。
#
# 叶子节点 是指没有子节点的节点。
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def calSum(root, count):
            if not root.left and not root.right and not count:
                return True
            if not root.left and not root.right and count:
                return False

            if root.left:
                count = count - root.left.val
                ret = calSum(root.left, count)
                if ret:
                    return True
                count = count + root.left.val
            if root.right:
                count = count - root.right.val
                ret = calSum(root.right, count)
                if ret:
                    return True
                count = count + root.right.val

            return False

        if not root:
            return False
        else:
            return calSum(root, targetSum - root.val)

"""
# 二刷，append的位置
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def calSum(root, total):
            path.append(root.val)
            if not root.left and not root.right and not total:
                res.append(path[:])
                return
            if not root.left and not root.right and total:
                return
            
            if root.left:
                # path.append(root.left.val)
                total -= root.left.val
                calSum(root.left, total)
                total += root.left.val
                path.pop()
            
            if root.right:
                # path.append(root.right.val)
                total -= root.right.val
                calSum(root.right, total)
                total += root.right.val
                path.pop()
        
        res = []
        if not root:
            return res

        path = []
        calSum(root, targetSum - root.val)
        return res
"""
"""
# 三刷，考虑负数
class Solution:
    def traversal(self, root, targetSum, total):
        if not root.left and not root.right and total != targetSum:
            return False
        if not root.left and not root.right and total == targetSum:
            return True
        
        if root.left:
            total += root.left.val
            if self.traversal(root.left, targetSum, total):
                return True
            total -= root.left.val
        if root.right:
            total += root.right.val
            if self.traversal(root.right, targetSum, total):
                return True
            total -= root.right.val
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.traversal(root, targetSum, root.val)

"""