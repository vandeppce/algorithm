# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix = [[1,1,1,1,1,1],[1,2,2,2,2,1],[1,2,3,3,2,1],[1,2,2,2,2,1],[1,1,1,1,1,1]]
matrix = [[3],[2],[1]]
matrix = [[1]]

matrix = [[2,3,4],[5,6,7],[8,9,10],[11,12,13]]

def spiralOrder(matrix):
    m = len(matrix)
    n = len(matrix[0])
    res = []

    top = 0
    bottom = m - 1
    left = 0
    right = n - 1

    if m == 1:
        res = matrix[0]
        return res

    if n == 1:
        for i in range(m):
            res.append(matrix[i][0])
        return res

    loop = min(m, n) // 2

    for i in range(loop):
        # top row
        for j in range(left, right):
            res.append(matrix[top][j])
        # right column
        for j in range(top, bottom):
            res.append(matrix[j][right])
        # bottom row
        for j in range(right, left, -1):
            res.append(matrix[bottom][j])
        # left column
        for j in range(bottom, top, -1):
            res.append(matrix[j][left])

        top += 1
        left += 1
        right -= 1
        bottom -= 1

    if min(m, n) % 2 != 0:
        if top == bottom:
            for j in range(left, right + 1):
                res.append(matrix[top][j])
        else:
            for j in range(top, bottom + 1):
                res.append(matrix[j][left])
    return res

print(spiralOrder(matrix))