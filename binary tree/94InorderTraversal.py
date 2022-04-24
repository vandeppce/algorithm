# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traversal(root):
            if root == None:
                return
            traversal(root.left)
            res.append(root.val)
            traversal(root.right)

        traversal(root)
        return res