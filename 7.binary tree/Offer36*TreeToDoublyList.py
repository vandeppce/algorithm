# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。
# 中序遍历二叉树，保存节点在列表中，然后遍历列表构造指向
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return
        nodeList = []
        def traversal(root):
            if not root:
                return
            traversal(root.left)
            nodeList.append(root)
            traversal(root.right)
        traversal(root)
        prev = nodeList[-1]
        for i in range(len(nodeList)):
            curr = nodeList[i]
            prev.right = curr
            curr.left = prev
            prev = curr
        return nodeList[0]

# 递归法
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur: return
            dfs(cur.left)  # 递归左子树
            if self.pre:  # 修改节点引用
                self.pre.right, cur.left = cur, self.pre
            else:  # 记录头节点
                self.head = cur
            self.pre = cur  # 保存 cur
            dfs(cur.right)  # 递归右子树

        if not root: return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head