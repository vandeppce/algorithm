# 删除与获得点数
# 给你一个整数数组 nums ，你可以对它进行一些操作。
#
# 每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i] + 1 的元素。
#
# 开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。
#
#  
#
# 示例 1：
#
# 输入：nums = [3,4,2]
# 输出：6
# 解释：
# 删除 4 获得 4 个点数，因此 3 也被删除。
# 之后，删除 2 获得 2 个点数。总共获得 6 个点数。

# 将点数相同的元素求和，并记录在箱中，箱索引为点数，转为不相邻子序列最大和问题

nums = [2,2,3,3,3,4]
nums = [3,4,2]
nums = [2,2,2,2,3,3,3,4,5,5,7,7,7]
nums = sorted(nums)

count = [0] * (max(nums) + 1)
for item in nums:
    count[item] += item

while count[0] == 0:
    count.pop(0)

length = len(count)
if length < 3:
    print(max(count))

dp = [0] * length
dp[0] = count[0]
dp[1] = count[1]
dp[2] = count[0] + count[2]

for i in range(3, length):
    dp[i] = count[i] + max(dp[i - 2], dp[i - 3])
print(max(dp))