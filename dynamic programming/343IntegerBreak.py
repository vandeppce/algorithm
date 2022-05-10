# 给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
#
# 返回 你可以获得的最大乘积 。

# 遍历过程中，若把i拆分成j+(i-j)，则最大乘积值为j*(i,j)和j*res(i-j)中的较大值
n = 10

def integerBreak(n):
    res = [0] * (n + 1)
    res[1] = 1

    for i in range(2, n + 1):
        for j in range(1, n):
            res[i] = max(res[i], j * (i - j), j * res[i - j])
    print(res)

print(integerBreak(n))