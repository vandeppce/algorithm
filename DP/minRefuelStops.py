# 最低加油次数
# 汽车从起点出发驶向目的地，该目的地位于出发位置东面 target 英里处。
#
# 沿途有加油站，每个 station[i] 代表一个加油站，它位于出发位置东面 station[i][0] 英里处，并且有 station[i][1] 升汽油。
#
# 假设汽车油箱的容量是无限的，其中最初有 startFuel 升燃料。它每行驶 1 英里就会用掉 1 升汽油。
#
# 当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。
#
# 为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 -1 。
#
# 注意：如果汽车到达加油站时剩余燃料为 0，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地。

# 输入：target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
# 输出：2
# 解释：
# 我们出发时有 10 升燃料。
# 我们开车来到距起点 10 英里处的加油站，消耗 10 升燃料。将汽油从 0 升加到 60 升。
# 然后，我们从 10 英里处的加油站开到 60 英里处的加油站（消耗 50 升燃料），
# 并将汽油从 10 升加到 50 升。然后我们开车抵达目的地。
# 我们沿途在1两个加油站停靠，所以返回 2 。

target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]

target = 1
startFuel = 1
stations = []

target = 100
startFuel = 50
stations = [[25,50],[50,25]]

# 错误示范，不能记录每个位置的最少加油次数
'''
stations.append([target, 0])

start = startFuel - stations[0][0]

if start < 0:
    print(-1)

addF = start + stations[0][1]
addN = start
current = stations[0][0]

length = len(stations)
cnt = 0
for i in range(1, length):
    needF = stations[i][0] - current
    remainF = addF - needF
    remainN = addN - needF

    if remainF < 0:
        print(-1)
    if remainF >= 0 and remainN < 0:
        cnt += 1
        addF = remainF + stations[i][1]
        addN = remainF
    if remainN >= 0:
        addF = remainN + stations[i][1]
        addN = remainN
    current = stations[i][0]
print(cnt)
'''
# 栈
length = len(stations)

for i in range(length):

