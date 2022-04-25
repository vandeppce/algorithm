# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
#
# 叶子节点 是指没有子节点的节点。

# 回溯
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, root, path, res):
        path.append(root.val)
        if not root.left and not root.right:
            tmp = ""
            for item in path[:-1]:
                tmp = tmp + str(item) + '->'
            res.append(tmp + str(path[-1]))
            return
        if root.left:
            self.traversal(root.left, path, res)
            path.pop()
        if root.right:
            self.traversal(root.right, path, res)
            path.pop()

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        res = []
        self.traversal(root, path, res)
        return res