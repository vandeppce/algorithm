# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
#
# 给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
#
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
#

##### 用数组的flag记录点是否被遍历过，要不从list中search要高

from collections import deque
n = 7168
class Solution:

    def numSquares(self, n: int) -> int:
        n_list = []
        for i in range(1, int(pow(n, 0.5)) + 1):
            n_list.append(i ** 2)
        count = 0
        queue = deque(n_list.copy())
        flag = [True] * (n + 1)

        while queue != []:
            count += 1
            for i in range(len(queue)):
                tmp = queue.popleft()
                if tmp == n:
                    return count
                else:
                    for item in n_list:
                        if tmp + item <= n and flag[tmp + item]:
                            queue.append(tmp + item)
                            flag[tmp + item] = False