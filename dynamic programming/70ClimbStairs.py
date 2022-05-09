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