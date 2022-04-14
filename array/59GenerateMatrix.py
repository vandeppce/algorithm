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