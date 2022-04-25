# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
# 判断左子树和右子树是否翻转

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def compare(left, right):
            if left == None and right != None:
                return False
            elif left != None and right == None:
                return False
            elif left == None and right == None:
                return True
            elif left.val != right.val:
                return False

            res_in = compare(left.right, right.left)
            res_out = compare(left.left, right.right)

            return res_in and res_out

        result = compare(root.left, root.right)
        return result