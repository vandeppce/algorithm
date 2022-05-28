# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

n = 10
# 只需要数每个子树的节点个数，例如(1,2)和(3,4)构成的二叉搜索树个数一样
def numTrees(n):
    nums = [0] * (n + 1)
    nums[0] = nums[1] = 1

    for i in range(2, n + 1):
        for j in range(1, i + 1):
            nums[i] += nums[j - 1] * nums[i - j]
    print(nums)

"""
# 二刷
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                left = j - 1
                right = i - j
                dp[i] += dp[left] * dp[right]
        return dp[-1]
"""
print(numTrees(n))