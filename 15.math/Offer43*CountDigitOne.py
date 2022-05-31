# 输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
#
# 例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。
#

# 动态规划，遍历。超时
class Solution:
    def countDigitOne(self, n: int) -> int:
        dp = 1
        for i in range(2, n + 1):
            count = 0
            t = i
            while t:
                if t % 10 == 1:
                    count += 1
                t = t // 10
            dp += count
        return dp

# 将1-n的所有位数出现1的次数相加，就是1出现的总次数。
# 对于abcd，对于c，将ab记为高位，d记为低位，则c位中出现1的次数有以下三种情况。
# c=0，high*digit。以2304为例，出现1的数字范围为0010-2219，除去c位则为000-229
# c=1，high*digit+low+1，以2314为例，出现1的数字范围为0010-2314，除去c则为000-234
# c=2-9，(high+1)*digit，以2324为例，出现1的数字范围为0010-2319，除去c则为000-239

class Solution:
    def countDigitOne(self, n: int) -> int:
        digit = 1
        res = 0
        high = n // 10
        low = 0
        curr = n % 10
        while high or curr:
            if curr == 0:
                res += high * digit
            elif curr == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit

            curr = high % 10
            digit *= 10
            high = high // 10
            low = n % digit
        return res