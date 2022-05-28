# 如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。
#
# 例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
# 给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。
#
# 子数组 是数组中的一个连续序列。
#

nums = [1,2,3,4]
nums = [1]
nums = [1,3,5,7,9,15,20,25,28,29]
# 以nums[i]为结尾的数组，其等差数列的个数其中一个来源为其前一位的等差数列数量，例如1,2,3,4,5，4位的等差数列为1,2,3,4和2,3,4，5位则为前面整体后移，
# 即2,3,4,5和3,4,5。而另一个来源为其前一个数的最长等差数列加上自身，即1,2,3,4,5
def numberOfArithmeticSlices(nums):
    dp = [0] * len(nums)
    for i in range(2, len(nums)):
        if 2 * nums[i - 1] == nums[i - 2] + nums[i]:
            dp[i] = dp[i - 1] + 1
    print(dp)
    return sum(dp)

print(numberOfArithmeticSlices(nums))