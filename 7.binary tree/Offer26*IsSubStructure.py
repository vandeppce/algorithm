# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
#
# B是A的子结构， 即 A中有出现和B相同的结构和节点值。
#
# 注意区分和子树的区别

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def compare(self, t1, t2):
        if not t1 and t2:
            return False
        # t1不一定要为空
        if not t2 and t1:
            return True
        if not t1 and not t2:
            return True
        if t1.val != t2.val:
            return False
        left = self.compare(t1.left, t2.left)
        right = self.compare(t1.right, t2.right)
        return left and right

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        stack = [A]
        while stack:
            for i in range(len(stack)):
                node = stack.pop(0)
                if self.compare(node, B):
                    return True
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return False