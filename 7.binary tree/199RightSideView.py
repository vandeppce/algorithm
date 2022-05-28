# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

# Definition for a 7.binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 遍历到每层时，从右向左添加全部子节点，然后pop时第一个弹出到即为最右面的节点，加一层判断即可
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                if i == 0:
                    res.append(node.val)
        return res