# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
#
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

x = 82

def mySqrt(x):
    left = 0
    right = x
    while left <= right:
        middle = (left + right) // 2
        mid_num = middle * middle

        if mid_num == x:
            return middle
        elif mid_num > x:
            right = middle - 1
        else:
            left = middle + 1
    return right

print(mySqrt(x))