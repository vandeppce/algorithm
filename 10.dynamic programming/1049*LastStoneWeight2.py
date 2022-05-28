# 有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。
#
# 每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
#
# 如果 x == y，那么两块石头都会被完全粉碎；
# 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
# 最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。
#

# 其实还是把stones分成两个堆，两个堆重量最接近时，最后石头的重量最小，就成了类似416中的问题。
stones = [2,7,4,1,8,1]
stones = [31,26,33,21,40]

def lastStoneWeight2(stones):
    target = sum(stones) // 2
    dp = [0] * (target + 1)

    for i in range(len(stones)):
        for j in range(target, stones[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
    return sum(stones) - dp[-1] - dp[-1]

print(lastStoneWeight2(stones))