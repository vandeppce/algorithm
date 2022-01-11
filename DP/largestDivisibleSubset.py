# 最大整除子集
# 给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：
# answer[i] % answer[j] == 0 ，或
# answer[j] % answer[i] == 0
# 如果存在多个有效解子集，返回其中任何一个均可。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[1,2]
# 解释：[1,3] 也会被视为正确答案。
import collections

nums = [1,2,3,4,6,8,10]
# nums = [1,2,3]
# nums = [4,8,10,240]
nums = [1,2,4,8,9,72]
nums = sorted(nums)
length = len(nums)
dp = [1] * length
ans = 0

for i in range(length):
    for j in range(i):
        if nums[i] % nums[j] == 0:
            dp[i] = max(dp[j] + 1, dp[i])

max_idx = dp.index(max(dp))
idx = max_idx
base = nums[max_idx]
ret = [base]
print(dp)
for i in range(idx):
    if base % nums[i] == 0:
        if len(ret) == 1:
            ret.append(nums[i])
        elif nums[i] % ret[1] == 0:
            ret.append(nums[i])

print(ret)
