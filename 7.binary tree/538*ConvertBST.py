# 给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），
# 使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
#
# 提醒一下，二叉搜索树满足下列约束条件：
#
# 节点的左子树仅包含键 小于 节点键的节点。
# 节点的右子树仅包含键 大于 节点键的节点。
# 左右子树也必须是二叉搜索树。
# 右中左方式的反中序遍历，设置prev值记录前一个节点的值
# Definition for a 7.binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = 0

    def traversal(self, root):
        if not root:
            return

        self.traversal(root.right)
        root.val += self.prev
        self.prev = root.val
        self.traversal(root.left)

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traversal(root)
        return root
