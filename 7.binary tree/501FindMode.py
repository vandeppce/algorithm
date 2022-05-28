# 给你一个含重复值的二叉搜索树（BST）的根节点 root ，找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。
#
# 如果树中有不止一个众数，可以按 任意顺序 返回。
#
# 假定 BST 满足如下定义：
#
# 结点左子树中所含节点的值 小于等于 当前节点的值
# 结点右子树中所含节点的值 大于等于 当前节点的值
# 左子树和右子树都是二叉搜索树
#
# 中序遍历+哈希
# Definition for a 7.binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def traversal(root):
            if not root:
                return
            traversal(root.left)
            nums.append(root.val)
            traversal(root.right)

        nums = []
        traversal(root)

        numTable = {}
        for num in nums:
            numTable[num] = numTable.get(num, 0) + 1

        maxNum = max(numTable.values())
        res = []
        for item in numTable.items():
            if item[1] == maxNum:
                res.append(item[0])
        return res