# 给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true ；否则，返回 false 。
#
# 二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 层序遍历每一个子树，然后分别和subRoot比较是否相同，比较过程又是后序遍历

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:

        def compare(node1, node2):
            if node1 and not node2:
                return False
            elif not node1 and node2:
                return False
            elif not node1 and not node2:
                return True
            elif node1.val != node2.val:
                return False

            return compare(node1.left, node2.left) and compare(node1.right, node2.right)

        queue = [root]
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                flag = compare(node, subRoot)
                if flag:
                    return True
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return False