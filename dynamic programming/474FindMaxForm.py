# 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
#
# 请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。
#
# 如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。
#

strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3

# 转化为01背包问题，两个遍历量。转化成背包问题后变成了，选择子串最多，并且0和1的个数在m和n的限制下。
# 转化后，外循环遍历strs，相当于前面的背包问题外循环遍历物品，内循环则遍历0和1的个数。由于要遍历0和1，因此内循环为两层子循环。
# 两层子循环中，0和1谁外谁内都行。此时，重量就是该串中0或1的个数，价值为1，代表可不可选。
def findMaxForm(strs, m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for str in strs:
        zeroNum = 0
        oneNum = 0
        for c in str:
            if c == "0":
                zeroNum += 1
            else:
                oneNum += 1
        for i in range(m, zeroNum - 1, -1):
            for j in range(n, oneNum - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - zeroNum][j - oneNum] + 1)
    print(dp)

print(findMaxForm(strs, m, n))