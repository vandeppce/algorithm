# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

nums = [1,5,11,5]

# 转化为01背包问题的思路，用i遍历nums中元素，也就是背包物品，用j遍历背包最大重量。在这个问题中，物品的重量和价值是一样的。
# 问题转化为01背包问题的思路为，以最大重量（总重量的一半）为11为例，如果当j=11时，价值总和恰好为11，则说明可以找到分割点。
# 为什么这样是对的呢？因为当背包重量为11时，由于重量和价值一样，最大价值也是11，所以如果可以找到最大价值为11，则说明此时背包填满，重量也是11，因此找到了分割点。
class Solution:
    def canPartition(self, nums) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        dp = [0] * 10001
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        print(dp[:target + 1])
        return dp[target] == target

solu = Solution()
print(solu.canPartition(nums))