# 在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
#
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
#
# 给定两个整数数组 gas 和 cost ，如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一 的。
#
# 从头开始遍历，记录下到每个加油站后剩余的总油量，如果大于0，说明可以到达下一个，继续走，如果小于0，则将起始加油站变为当前到达加油站的下一个
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
gas = [2,3,4]
cost = [3,4,3]
def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    step = 0
    i = 0
    start = 0
    prev = 0
    while step < len(gas):
        curr = gas[i] - cost[i]
        if curr + prev >= 0:
            i = (i + 1) % len(gas)
            step += 1
            prev += curr

        else:
            i = (i + 1) % len(gas)
            start = i
            step = 0
            prev = 0
    return start

print(canCompleteCircuit(gas, cost))