# 写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数。
#
#  
#
# 首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
#
# 当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；
# 假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
#
# 该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
#
# 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
#
# 在任何情况下，若函数不能进行有效的转换时，请返回 0。
#
# 说明：
#
# 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。
# 如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
#
str = "4193 with words"
str = "   -42"
str = "words and 987"
str = "-91283472332"

# 各种情况
class Solution:
    def strToInt(self, str: str) -> int:
        numList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        signList = ['+', '-']
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        sign = 1
        start = 0
        res = 0
        while start < len(str) and str[start] == ' ':
            start += 1
        if start == len(str):
            return 0
        if str[start] not in numList and str[start] not in signList:
            return 0
        if str[start] not in numList:
            if start == len(str) - 1:
                return 0
            elif str[start + 1] not in numList:
                return 0
        if str[start] == '-':
            sign = -1
            start += 1
        if str[start] == '+':
            start += 1
        while start < len(str) and str[start] in numList:
            res = res * 10 + numList.index(str[start])
            if sign * res >= INT_MAX or sign * res <= INT_MIN:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            start += 1
        return sign * res

print(strToInt(str))