# 如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的：
#
# n >= 3
# 对于所有 i + 2 <= n，都有 X_i + X_{i+1} = X_{i+2}
# 给定一个严格递增的正整数数组形成序列 arr ，找到 arr 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。
#
# （回想一下，子序列是从原序列  arr 中派生出来的，它从 arr 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。
# 例如， [3, 5, 8] 是 [3, 4, 5, 6, 7, 8] 的一个子序列）
#

arr = [1,2,3,4,5,6,7,8]
arr = [1,2,3,4,5,6,7,8,12,18]

'''
# 方法一，搜索，超时
def lenLongestFibSubseq(arr):
    dp = [0] * len(arr)
    for i in range(2, len(dp)):
        for j in range(i - 1, -1, -1):
            cnt = 0
            if (arr[i] - arr[j]) in arr and arr[i] - arr[j] < arr[j]:
                cnt = 2
            a1 = arr[i]
            a2 = arr[j]
            while (a1 - a2) in arr and a1 - a2 < a2:
                cnt += 1
                tmp = a1 - a2
                a1 = a2
                a2 = tmp
            dp[i] = max(dp[i], cnt)
    return dp
'''
'''
# 方法二，dp[i][j]表示以arr[i],arr[j]为最后两个元素的斐波那契数列长度，那么有如果arr[k]+arr[i]=arr[j]，因为
# 以arr[k]和arr[i]为结尾已经构成斐波那契数列，所以有dp[i][j]=dp[k][i]+1
# 三个for，超时
def lenLongestFibSubseq(arr):
    dp = [[0] * len(arr) for _ in range(len(arr))]
    maxLength = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            for k in range(i):
                if arr[j] == arr[i] + arr[k]:
                    dp[i][j] = max(dp[i][j], dp[k][i] + 1)
                    maxLength = max(maxLength, dp[i][j])
    if maxLength > 0:
        return maxLength + 2
    else:
        return maxLength
'''
# 方法三，把k的那层循环去掉，每次计算arr[j]-arr[i]是否在arr中（设序号为k），并且k<i，依然tmd超时
def lenLongestFibSubseq(arr):
    dp = [[0] * len(arr) for _ in range(len(arr))]
    maxLength = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if (arr[j] - arr[i]) in arr and arr[j] - arr[i] < arr[i]:
                k = arr.index(arr[j] - arr[i])
                dp[i][j] = max(dp[i][j], dp[k][i] + 1)
                maxLength = max(maxLength, dp[i][j])
    if maxLength > 0:
        return maxLength + 2
    else:
        return maxLength

# 方法四，使用hash寻找k的索引，其他不变，终于不超时了
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        dp = [[0] * len(arr) for _ in range(len(arr))]
        maxLength = 0
        idxHash = {}
        for i in range(len(arr)):
            idxHash[arr[i]] = i
        for i in range(1, len(arr) - 1):
            for j in range(i + 1, len(arr)):
                k = idxHash.get(arr[j] - arr[i], -1)
                if k != -1 and k < i:
                    dp[i][j] = max(dp[i][j], dp[k][i] + 1)
                    maxLength = max(maxLength, dp[i][j])
        if maxLength > 0:
            return maxLength + 2
        else:
            return maxLength
print(lenLongestFibSubseq(arr))