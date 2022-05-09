# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。
#
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
#
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
#

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
obstacleGrid = [[0,1],[0,0]]
obstacleGrid = [[0,0],[0,1]]

def uniquePathsWithObstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    steps = [[0] * n for _ in range(m)]
    if obstacleGrid[0][0] != 1:
        steps[0][0] = 1
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if obstacleGrid[i][j] != 1:
                if i == 0 and obstacleGrid[i][j - 1] != 1:
                    steps[i][j] = steps[i][j - 1]
                if j == 0 and obstacleGrid[i - 1][j] != 1:
                    steps[i][j] = steps[i - 1][j]
                if i > 0 and j > 0:
                    steps[i][j] = (1 - obstacleGrid[i][j - 1]) * steps[i][j - 1] + (1 - obstacleGrid[i - 1][j]) * steps[i - 1][j]
    return steps[-1][-1]

print(uniquePathsWithObstacles(obstacleGrid))