# 斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
# F(0) = 0，F(1) = 1
# F(n) = F(n - 1) + F(n - 2)，其中 n > 1
# 给定 n ，请计算 F(n) 。

# 动规
class Solution:
    def fib(self, n: int) -> int:
        nums = [0, 1]

        for i in range(2, n + 1):
            nums.append(nums[i - 1] + nums[i - 2])
        return nums[n]

# 递归
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)