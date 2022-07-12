# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

# 深度优先搜索
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        count = 0

        def dfs(grid, i, j):
            if i < 0 or i > numRows - 1 or j < 0 or j > numCols - 1:
                return
            if grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(grid, i - 1, j)
                dfs(grid, i + 1, j)
                dfs(grid, i, j - 1)
                dfs(grid, i, j + 1)

        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == "1":
                    count += 1
                    dfs(grid, i, j)

        return count

"""
# 二刷，dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        count = 0

        def dfs(i, j):
            grid[i][j] = "0"
            # 上
            if i > 0 and grid[i - 1][j] == "1":
                dfs(i - 1, j)
            # 下
            if i < numRows - 1 and grid[i + 1][j] == "1":
                dfs(i + 1, j)
            # 左
            if j > 0 and grid[i][j - 1] == "1":
                dfs(i, j - 1)
            # 右
            if j < numCols - 1 and grid[i][j + 1] == "1":
                dfs(i, j + 1)
        
        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count
"""