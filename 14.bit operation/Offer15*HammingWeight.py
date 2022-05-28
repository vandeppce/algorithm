# 编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为 汉明重量).）。
#
#  
#
# 提示：
#
# 请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，
# 因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
# 在 Java 中，编译器使用 二进制补码 记法来表示有符号整数。因此，在上面的 示例 3 中，输入表示有符号整数 -3。
#
# 当作十进制来做了
class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        while n:
            total += n % 2
            n = n // 2
        return total

# python位运算
# 我们可以直接循环检查给定整数n二进制位的每一位是否为1。
# 具体代码中，当检查第i 位时，我们可以让n与2^i进行与运算，当且仅当n的第i位为1时，运算结果不为0
class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = sum(1 for i in range(32) if n & (1 << i))
        return ret