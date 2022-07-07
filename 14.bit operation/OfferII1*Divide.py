# 给定两个整数 a 和 b ，求它们的除法的商 a/b ，要求不得使用乘号 '*'、除号 '/' 以及求余符号 '%' 。
#
#  
#
# 注意：
#
# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231, 231−1]。本题中，如果除法结果溢出，则返回 231 − 1
#
# 二分查找，b不断翻倍，直到大于a，然后a减去b，再依次循环。
# 例如100，7。这种方式把100拆成了56，28，14，2，结果为8+4+2=14

a = 7
b = -3

class Solution:
    def divide(self, a: int, b: int) -> int:
        if a == 0:
            return 0
        sign = 1
        if a > 0 and b < 0:
            sign = -1
        elif a < 0 and b > 0:
            sign = -1
        a = abs(a)
        b = abs(b)
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        c = 1
        tmp = b
        res = 0
        while a >= 0:
            while a >= 0 and b + b <= a:
                b += b
                c += c
            a -= b
            b = tmp
            if a >= 0:
                res += c
            c = 1
        res = sign * res
        if res > INT_MAX:
            return INT_MAX
        if res < INT_MIN:
            return INT_MIN
        return res

solu = Solution()
print(solu.divide(a, b))