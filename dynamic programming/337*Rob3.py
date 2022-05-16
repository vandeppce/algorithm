# 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。
#
# 除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，
# 聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。
#
# 给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
# 后序遍历，对于每一个节点的最大值，可能有两个来源。1是选择其自身，跳过子节点，然后选择子节点的子节点。二是不选择自身，选择子节点。比较较大值。
# 递归的方式会超时。
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0

        # 抢劫根节点
        val1 = 0
        val1 += root.val
        if root.left:
            val1 = val1 + self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val1 = val1 + self.rob(root.right.left) + self.rob(root.right.right)

        # 不抢劫根节点
        val2 = 0
        val2 = self.rob(root.left) + self.rob(root.right)
        return max(val1, val2)
'''
'''
# 记忆化递归，把所有已经遍历过的节点放到字典中
class Solution:
    def __init__(self):
        self.memory = {}
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        if self.memory.get(root):
            return self.memory[root]
        # 抢劫根节点
        val1 = 0
        val1 += root.val
        if root.left:
            val1 = val1 + self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val1 = val1 + self.rob(root.right.left) + self.rob(root.right.right)
        
        # 不抢劫根节点
        val2 = 0
        val2 = self.rob(root.left) + self.rob(root.right)
        self.memory[root] = max(val1, val2)
        return max(val1, val2)
'''

'''
# 动态规划，递归过程中返回每个节点选择和不选择的最大值
# 树的动态规划
class Solution:
    def traversal(self, root):
        if not root:
            return [0, 0]
        
        left = self.traversal(root.left)
        right = self.traversal(root.right)
        # 选择本节点
        val1 = root.val + left[0] + right[0]
        # 不选择本节点
        val2 = max(left[0], left[1]) + max(right[0], right[1])

        return [val2, val1]

    def rob(self, root: TreeNode) -> int:
        res = self.traversal(root)
        return max(res[0], res[1])
'''