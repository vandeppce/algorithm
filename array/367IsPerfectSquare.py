# 给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。

num = 14

def isPerfectSquare(num):
    left = 0
    right = num

    while left <= right:
        middle = (left + right) // 2
        mid_num = middle * middle

        if mid_num == num:
            return True
        elif mid_num > num:
            right = middle - 1
        else:
            left = middle + 1

    return False

print(isPerfectSquare(num))