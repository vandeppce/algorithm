# 给定两个 01 字符串 a 和 b ，请计算它们的和，并以二进制字符串的形式输出。
#
# 输入为 非空 字符串且只包含数字 1 和 0。

a = '11'
b = '10'
a = "11010"
b = "1011"
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        y = 0
        res = []
        while a and b:
            a1 = int(a.pop())
            b1 = int(b.pop())

            if y:
                x = a1 ^ y
                tmp = a1 & y
                a1 = x
                x = a1 ^ b1
                y = a1 & b1
                tmp = tmp ^ y
                y = tmp
            else:
                x = a1 ^ b1
                y = a1 & b1
            res.insert(0, str(x))

        if a or b:
            if b:
                a = b
            while a:
                a1 = int(a.pop())
                x = a1 ^ y
                y = a1 & y
                res.insert(0, str(x))
        if y:
            res.insert(0, str(y))
        return "".join(res)

class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]

print(addBinary(a, b))