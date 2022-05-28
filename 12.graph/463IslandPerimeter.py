# 给定一个 row x col 的二维网格地图 grid ，其中：grid[i][j] = 1 表示陆地， grid[i][j] = 0 表示水域。
#
# 网格中的格子 水平和垂直 方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
#
# 岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。
#

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
grid = [[1]]
grid = [[1,0]]
# 模拟法，一个岛屿4条边，只要相邻则减去两条边
def islandPerimeter(grid):
    row = len(grid)
    col = len(grid[0])
    numsIslands = 0
    edges = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                numsIslands += 1
                if j > 0 and grid[i][j - 1] == 1:
                    edges += 1
                if i > 0 and grid[i - 1][j] == 1:
                    edges += 1
    return 4 * numsIslands - 2 * edges

print(islandPerimeter(grid))