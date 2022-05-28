# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
#
# 问总共有多少条不同的路径？
#

m = 7
n = 3

def uniquePaths(m, n):
    steps = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            steps[i][j] = steps[i - 1][j] + steps[i][j - 1]
    return steps[-1][-1]
print(uniquePaths(m, n))