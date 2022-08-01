# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
#
# 如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
#
# 假设环境不允许存储 64 位整数（有符号或无符号）。
#

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        ret = 0
        intMin = -(2 ** 31)
        intMax = 2 ** 31
        if x < 0:
            sign = -1
            x = -x
        while x:
            ret = ret * 10 + x % 10
            x = x // 10
        ret = sign * ret
        if ret < intMin or ret > intMax:
            return 0
        return ret