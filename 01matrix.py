# 01 矩阵
# 给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。
#
# 两个相邻元素间的距离为 1 。

mat = [[0,0,0],[0,1,0],[1,1,1]]
#mat = [[0,0,0],[0,1,0],[0,0,0]]
mat = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],
 [0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]
mat = [[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],
       [1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[0,0,0]]

# bfs for every 1, overtime
'''
numRows = len(mat)
numCols = len(mat[0])

res = []

for i in range(numRows):
    tmp = []
    for j in range(numCols):
        val = mat[i][j]
        if val == 0:
            tmp.append(0)
        else:
            queue = [[i, j]]
            flag = 1
            cnt = -1
            while queue and flag:
                cnt += 1
                for k in range(len(queue)):
                    present = queue.pop(0)
                    q_val = mat[present[0]][present[1]]
                    if q_val == 0:
                        flag = 0
                        break
                    if present[0] - 1 >= 0:
                        queue.append([present[0] - 1, present[1]])
                    if present[0] + 1 < numRows:
                        queue.append([present[0] + 1, present[1]])
                    if present[1] - 1 >= 0:
                        queue.append([present[0], present[1] - 1])
                    if present[1] + 1 < numCols:
                        queue.append([present[0], present[1] + 1])
            tmp.append(cnt)
    res.append(tmp)
print(res)
'''

numRows = len(mat)
numCols = len(mat[0])

res = [[-1 for _ in range(numCols)] for __ in range(numRows)]
queue = []

for i in range(numRows):
    for j in range(numCols):
        if mat[i][j] == 0:
            res[i][j] = 0
            queue.append([i, j])

lr = [-1, 0, 1, 0]
ud = [0, -1, 0, 1]
# 从0开始，遍历每个点四周
while queue:
    present = queue.pop(0)
    x = present[0]
    y = present[1]

    for i in range(4):
        if x + lr[i] >= 0 and x + lr[i] < numRows and y + ud[i] >= 0 and y + ud[i] < numCols and res[x + lr[i]][y + ud[i]] == -1:
            res[x + lr[i]][y + ud[i]] = res[x][y] + 1
            queue.append([x + lr[i], y + ud[i]])
print(res)