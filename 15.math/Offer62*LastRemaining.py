# 0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。
#
# 例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。
#

"""
# 模拟法，递归，超时
class Solution:
    def dfs(self, nums, m, start):
        if len(nums) == 1:
            return nums[0]
        delIdx = (start + m - 1) % len(nums)
        nums.pop(delIdx)
        return self.dfs(nums, m, delIdx)

    def lastRemaining(self, n: int, m: int) -> int:
        nums = list(range(n))
        return self.dfs(nums, m, 0)
"""

# 动态规划，著名的约瑟夫环
# 若已知[n-1,m]问题的解为f(n-1)，则[n,m]问题的解为
# f(n)=(f(n-1)+m)%n

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        x = 0
        for i in range(2, n + 1):
            x = (x + m) % i
        return x
