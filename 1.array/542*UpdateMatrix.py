# 给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。
#
# 两个相邻元素间的距离为 1 。
#

mat = [[0,0,0],[0,1,0],[0,0,0]]
mat = [[0,0,0],[0,1,0],[1,1,1]]
mat = [[1,1,0,0,1,0,0,1,1,0],[1,0,0,1,0,1,1,1,1,1],[1,1,1,0,0,1,1,1,1,0],[0,1,1,1,0,1,1,1,1,1],[0,0,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,0,1,1,1],[0,1,1,1,1,1,1,0,0,1],[1,1,1,1,1,0,0,1,1,1],[0,1,0,1,1,0,1,1,1,1],[1,1,1,0,1,0,1,1,1,1]]

# 先查找0的位置，然后再从所有的0开始搜索1

# 动态规划解法，这里由于是先搜索完0再搜索距离为1的1然后再搜索距离为2的1的临域，所以每次dp[i][j]+1即可
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        dp = [[-1] * col for _ in range(row)]
        stack = []

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                    stack.append([i, j])

        while stack:
            present = stack.pop(0)
            x = present[0]
            y = present[1]
            # 上
            if x > 0 and dp[x - 1][y] == -1:
                stack.append([x - 1, y])
                dp[x - 1][y] = dp[x][y] + 1
            # 下
            if x < row - 1 and dp[x + 1][y] == -1:
                stack.append([x + 1, y])
                dp[x + 1][y] = dp[x][y] + 1
            # 左
            if y > 0 and dp[x][y - 1] == -1:
                stack.append([x, y - 1])
                dp[x][y - 1] = dp[x][y] + 1
            # 右
            if y < col - 1 and dp[x][y + 1] == -1:
                stack.append([x, y + 1])
                dp[x][y + 1] = dp[x][y] + 1

        return dp

# 广度优先搜索解法，记录搜索轮数，每一轮的轮数是最近距离
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        dp = [[-1] * col for _ in range(row)]
        stack = []

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                    stack.append([i, j])
        dis = 0
        while stack:
            dis += 1
            for i in range(len(stack)):
                present = stack.pop(0)
                x = present[0]
                y = present[1]
                # 上
                if x > 0 and dp[x - 1][y] == -1:
                    stack.append([x - 1, y])
                    dp[x - 1][y] = dis
                # 下
                if x < row - 1 and dp[x + 1][y] == -1:
                    stack.append([x + 1, y])
                    dp[x + 1][y] = dis
                # 左
                if y > 0 and dp[x][y - 1] == -1:
                    stack.append([x, y - 1])
                    dp[x][y - 1] = dis
                # 右
                if y < col - 1 and dp[x][y + 1] == -1:
                    stack.append([x, y + 1])
                    dp[x][y + 1] = dis

        return dp

print(updateMatrix(mat))
