# 编写一个算法来判断一个数 n 是不是快乐数。
#
# 「快乐数」 定义为：
#
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果这个过程 结果为 1，那么这个数就是快乐数。
# 如果 n 是 快乐数 就返回 true ；不是，则返回 false 。

n = 19
n = 2
# 注意为false的条件，既然无限循环，则肯定会出现历史结果
def isHappy(n):
    history = []
    while True:
        cnt = 0
        while n != 0:
            a = n % 10
            cnt += a * a
            n = (n - a) // 10

        if cnt == 1:
            return True
        if cnt in history:
            return False
        else:
            history.append(cnt)
            n = cnt

print(isHappy(n))