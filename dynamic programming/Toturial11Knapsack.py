# 物品0，重量1，价值15；物品1，重量3，价值20；物品2，重量4，价值30。背包最大重量4

bag_size = 4
weight = [1, 3, 4]
value = [15, 20, 30]

# 使用二维数组，定义dp数组: dp[i][j] 前i个物品里，放进容量为j的背包，价值总和最大是多少。
def test_2_wei_bag_problem1(bag_size, weight, value):
    rows = len(weight)
    cols = bag_size + 1

    dp = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        dp[i][0] = 0

    first_item_weight, first_item_value = weight[0], value[0]
    for j in range(1, cols):
        if first_item_weight <= j:
            dp[0][j] = first_item_value

    # 更新dp数组，先遍历物品，再遍历背包
    for i in range(1, rows):
        cur_weight = weight[i]
        cur_val = value[i]
        for j in range(1, cols):
            if cur_weight > j: # 说明背包装不下当前物品.
                dp[i][j] = dp[i - 1][j]
            else:
                # 定义dp数组: dp[i][j] 前i个物品里，放进容量为j的背包，价值总和最大是多少。
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cur_weight] + cur_val)
    print(dp)

# 使用一维数组
def test_1_wei_bag_problem(bag_size, weight, value):
    dp = [0] * (bag_size + 1)
    # 先遍历物品，再遍历背包容量
    for i in range(len(weight)):
        for j in range(bag_size, weight[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    print(dp)

test_1_wei_bag_problem(bag_size, weight, value)
test_2_wei_bag_problem1(bag_size, weight, value)