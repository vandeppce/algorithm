# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

# 观察前面几个数找递推公式，可以发现就是斐波那契数列
class Solution:
    def climbStairs(self, n: int) -> int:
        nums = [1, 2]
        for i in range(2, n):
            nums.append(nums[i - 1] + nums[i - 2])
        return nums[n - 1]

# 完全背包问题
def climbStairs(n):
    nums = [1, 2]
    dp = [0] * (n + 1)
    dp[0] = 1

    for j in range(n + 1):
        for i in range(len(nums)):
            if j >= nums[i]:
                dp[j] += dp[j - nums[i]]
    print(dp)

"""
# 二刷，背包问题
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for j in range(1, n + 1):
            for i in range(1, 3):
                if j >= i:
                    dp[j] += dp[j - i]
        return dp[-1]
"""
n = 3
print(climbStairs(n))