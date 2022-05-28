# 物品0，重量1，价值15；物品1，重量3，价值20；物品2，重量4，价值30。背包最大重量4。
# 每种物品无数个

weight = [1, 3, 4]
value = [15, 20, 30]
bag_weight = 4

# 先遍历物品再遍历背包容量
def test_complete_pack1(weight, value, bag_weight):
    dp = [0] * (bag_weight + 1)
    for i in range(len(weight)):
        for j in range(weight[i], bag_weight + 1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    print(dp[-1])

# 先遍历背包容量再遍历物品
def test_complete_pack2(weight, value, bag_weight):
    dp = [0] * (bag_weight + 1)
    for j in range(bag_weight + 1):
        for i in range(len(weight)):
            if j >= weight[i]:
                dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    print(dp[-1])

test_complete_pack1(weight, value, bag_weight)
test_complete_pack2(weight, value, bag_weight)