matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
matrix = [[2,5],[8,4],[0,-1]]
class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        loop = min(m, n) // 2
        res = []
        if m == 1:
            res = matrix[0]
            return res

        if n == 1:
            for i in range(m):
                res.append(matrix[i][0])
            return res
        for i in range(loop):
            left = i
            top = i
            right = n - 1 - i
            bottom = m - 1 - i

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
        bottom -= 1
        left += 1
        right -= 1

        if min(m, n) % 2 == 1:
            if top == bottom:
                for j in range(left, right + 1):
                    res.append(matrix[top][j])
            else:
                for j in range(top, bottom + 1):
                    res.append(matrix[j][left])
        return res

solu = Solution()
print(solu.spiralOrder(matrix))