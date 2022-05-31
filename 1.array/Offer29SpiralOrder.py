# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

matrix = [[1,2,3],[4,5,6],[7,8,9]]

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
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