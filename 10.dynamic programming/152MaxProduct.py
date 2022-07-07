# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
#
# 测试用例的答案是一个 32-位 整数。
#
# 子数组 是数组的连续子序列。
#
# 记录到每个位置的最大值和最小值。
nums = [2, 3, -2, 4]
nums = [-2, 0, -1]
nums = [-2, 3, -4]
def maxProduct(nums):
    maxNums = nums.copy()
    minNums = nums.copy()

    for i in range(1, len(nums)):
        pMax = maxNums[i - 1]
        pMin = minNums[i - 1]
        if nums[i] < 0:
            pMax, pMin = pMin, pMax

        maxNums[i] = max(nums[i], pMax * nums[i])
        minNums[i] = min(nums[i], pMin * nums[i])
    return max(max(maxNums), max(minNums))

print(maxProduct(nums))