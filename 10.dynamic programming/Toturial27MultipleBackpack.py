#  物品0，重量1，价值15，数量2；物品1，重量3，价值20，数量3；物品2，重量4，价值30，数量2。背包最大重量10。

# 可以转成如下的01背包问题
# 物品0，重量1，价值15；物品0，重量1，价值15；
# 物品1，重量3，价值20；物品1，重量3，价值20；物品1，重量3，价值20；
# 物品2，重量4，价值30。物品2，重量4，价值30。
# 背包最大重量4。

weight = [1, 3, 4]
value = [15, 20, 30]
nums = [2, 3, 2]
bag_weight = 10

def test_multi_pack(weight, value, nums, bag_weight):
    for i in range(len(nums)):
        while nums[i] > 1:
            weight.append(weight[i])
            value.append(value[i])
            nums[i] -= 1
    dp = [0] * (bag_weight + 1)

    for i in range(len(weight)):
        for j in range(bag_weight, weight[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    print(dp)
    return dp[-1]

print(test_multi_pack(weight, value, nums, bag_weight))