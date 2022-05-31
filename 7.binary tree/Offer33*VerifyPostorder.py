# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

# 观察可知，对于某一个节点，其后序遍历时若出现比其小的值，那么必从list[0]开始并且是连续的一段，例如6 8 11 10 7 4，根据这个原理判断
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        for i in range(1, len(postorder)):
            j = 0
            while j < i and postorder[j] < postorder[i]:
                j += 1
            while j < i:
                if postorder[j] < postorder[i]:
                    return False
                j += 1
        return True

# 官方解法，递归分治。
# 根据二叉搜索树的定义，可以通过递归，判断所有子树的 正确性 （即其后序遍历是否满足二叉搜索树的定义） ，若所有子树都正确，则此序列为二叉搜索树的后序遍历。
# 终止条件：当i>=j，说明此子树节点数量<=1，直接返回true
# 递推工作：
# 1。 划分左右子树。遍历后序遍历的[i,j]区间元素，寻找第一个大于根节点的节点，索引记为m。此时左子树区间为[i,m-1]，右子树区间为[m,j-1]，根节点索引为j
# 2。 判断是否为二叉搜索树。左子树区间所有节点小于postorder[j]，右子树区间节点大于postorder[j]，实现方式为遍历。
class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        def recur(i, j):
            if i >= j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j]: p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)