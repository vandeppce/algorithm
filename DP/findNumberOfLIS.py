# 最长递增子序列的个数
# 给定一个未排序的整数数组，找到最长递增子序列的个数。
#
# 示例 1:
#
# 输入: [1,3,5,4,7]
# 输出: 2
# 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。

nums = [1, 3, 5, 4, 2, 1, 2, 3, 7]
# nums = [1,3,5,4,2]
# nums = [2,2,2,2,2]

# 计算每个位置的最长上升子序列
length = len(nums)
LIS = [1] * length

for i in range(length):
    tmp = 1
    for j in range(i):
        if nums[i] > nums[j]:
            tmp = max(LIS[j] + 1, tmp)
    LIS[i] = tmp

numLIS = [0] * length

# 计算每个位置的最长上升子序列个数。具体包括，如果最长上升子序列是1，那么该位置的numLIS也是1；否则查看该位置前面所有
# 最长上升子序列为该位置最长上升子序列数-1的所有元素，如果该位置元素大于检查元素，则表明该位置可以和该元素及其之前组成上升子序列，
# 则该位置的最长上升子序列个数为当前个数+检查元素对应最长上升子序列个数
for i in range(length):
    present = LIS[i]
    if present == 1:
        numLIS[i] = 1
    for j in range(i):
        if LIS[j] == present - 1 and nums[j] < nums[i]:
            numLIS[i] += numLIS[j]

# 查看最长上升子序列，所有最大最长上升子序列的个数和即为最长上升子序列个数
max_idx = max(LIS)
cnt = 0
for i in range(length):
    if LIS[i] == max_idx:
        cnt += numLIS[i]
print(cnt)