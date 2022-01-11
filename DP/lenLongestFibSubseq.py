# 最长的斐波那契子序列的长度
# 如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的：
#
# n >= 3
# 对于所有 i + 2 <= n，都有 X_i + X_{i+1} = X_{i+2}
# 给定一个严格递增的正整数数组形成序列 arr ，找到 arr 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。
#
# （回想一下，子序列是从原序列 arr 中派生出来的，它从 arr 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。例如， [3, 5, 8] 是 [3, 4, 5, 6, 7, 8] 的一个子序列）
#

# 输入: arr = [1,2,3,4,5,6,7,8]
# 输出: 5
# 解释: 最长的斐波那契式子序列为 [1,2,3,5,8] 。
import collections

arr = [1,2,3,4,5,6,7,8]
# arr = [1,3,7,11,12,14,18]

# 暴力搜索
'''
s = set(arr)

length = len(arr)
max_cnt = 0

for i in range(length):
    for j in range(i + 1, length):
        x = arr[i]
        y = arr[j]
        cnt = 2
        while x + y in s:
            x, y = y, x + y
            cnt += 1
        max_cnt = max(max_cnt, cnt)
print(max_cnt)
'''

# 动态规划
index = {x: i for i, x in enumerate(arr)}
longest = collections.defaultdict(lambda: 2)

ans = 0
for k, z in enumerate(arr):
    for j in range(k):
        i = index.get(z - arr[j], None)
        if i is not None and i < j:
            cand = longest[j, k] = longest[i, j] + 1
            ans = max(ans, cand)
if ans >= 3:
    print(ans)
else:
    print(0)