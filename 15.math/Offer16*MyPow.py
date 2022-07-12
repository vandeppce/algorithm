# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。
# 直接递归/迭代，超时
"""
class Solution:
    def __init__(self):
        self.res = 1
    def myPow(self, x: float, n: int) -> float:
        def dfs(x, n, i):
            if i >= n:
                return
            self.res *= x
            dfs(x, n, i + 1)
        if n > 0:
            dfs(x, n, 0)
        else:
            n = -n
            dfs(x, n, 0)
            self.res = 1 / self.res
        return self.res
"""
# 另一种递归。可知，如果n为奇数，那么x^n=x^(n/2)*x^(n/2)*x，否则x^n=x^(n/2)*x^(n/2)，因此每次二分即可
# 这种方法叫快速幂算法，本质上是分治
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def dfs(x, n):
            if n <= 1:
                return x
            if n % 2 == 1:
                mid = self.myPow(x, n // 2)
                return mid * mid * x
            else:
                mid = self.myPow(x, n // 2)
                return mid * mid
        if n == 0:
            return 1
        elif n < 0:
            return 1 / dfs(x, -n)
        else:
            return dfs(x, n)

# 迭代法
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N % 2 == 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N //= 2
            return ans

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

"""
# 二刷
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def dfs(x, n):
            if n == 1:
                return x
            if n % 2 == 0:
                semi = dfs(x, n // 2)
                return semi * semi
            else:
                semi = dfs(x, n // 2)
                return semi * semi * x
        if n == 0:
            return 1
        elif n > 0:
            return dfs(x, n)
        else:
            return 1 / dfs(x, -n)
"""
x = 2.10000
n = 3
solu = Solution()
print(solu.myPow(x, n))