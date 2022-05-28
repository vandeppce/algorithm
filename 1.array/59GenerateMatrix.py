# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
# 边界条件

n = 6
xstart = 0
ystart = 0
count = 0
loop = n // 2
res = [[0] * n for _ in range(n)]

for i in range(loop):
    xstart = i
    ystart = i

    for j in range(xstart, n - 1 - xstart):
        count += 1
        res[i][j] = count

    for j in range(ystart, n - 1 - ystart):
        count += 1
        res[j][n - 1 - ystart] = count

    for j in range(n - 1 - xstart, xstart, -1):
        count += 1
        res[n - 1 - xstart][j] = count

    for j in range(n - 1 - ystart, ystart, -1):
        count += 1
        res[j][ystart] = count

if n % 2 != 0:
    res[loop][loop] = n ** 2

print(res)

"""
# 二刷
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        loop = n // 2
        cnt = 0
        matrix = [[0] * n for _ in range(n)]

        for i in range(loop):
            left = i
            right = n - i - 1
            top = i
            bottom = n - i - 1
            # top row
            for j in range(left, right):
                cnt += 1
                matrix[top][j] = cnt
            # right column
            for j in range(top, bottom):
                cnt += 1
                matrix[j][right] = cnt
            # bottom row
            for j in range(right, left, -1):
                cnt += 1
                matrix[bottom][j] = cnt
            # left column
            for j in range(bottom, top, -1):
                cnt += 1
                matrix[j][left] = cnt
            
        if n % 2 == 1:
            matrix[loop][loop] = cnt + 1
        return matrix
"""