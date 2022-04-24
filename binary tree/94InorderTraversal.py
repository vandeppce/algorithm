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

# 迭代法，先可着左节点来
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        node = root

        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        return res