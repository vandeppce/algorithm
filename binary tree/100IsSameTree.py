# 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
#
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 左子树等于左子树，右子树等于右子树
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def compare(treeP, treeQ):
            if treeP == None and treeQ != None:
                return False
            elif treeP != None and treeQ == None:
                return False
            elif treeP == None and treeQ == None:
                return True
            elif treeP.val != treeQ.val:
                return False

            res_l = compare(treeP.left, treeQ.left)
            res_r = compare(treeP.right, treeQ.right)
            return res_l and res_r

        return compare(p, q)