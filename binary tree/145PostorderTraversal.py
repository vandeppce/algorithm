# 给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traversal(root):
            if root == None:
                return

            traversal(root.left)
            traversal(root.right)
            res.append(root.val)

        traversal(root)
        return res

# 迭代法，中左右顺序入栈，相当于结果里顺序是中右左，倒序即可
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]