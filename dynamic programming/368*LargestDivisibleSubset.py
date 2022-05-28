# 给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，
# 子集中每一元素对 (answer[i], answer[j]) 都应当满足：
# answer[i] % answer[j] == 0 ，或
# answer[j] % answer[i] == 0
# 如果存在多个有效解子集，返回其中任何一个均可。
#

nums = [1,2,3]
nums = [1,2,4,8]
nums = [1,2,3,4,6,8,10,17,19,78,126,24]
nums = [5,9,18,54,108,540,90,180,360,720]

def largestDivisibleSubset(nums):
    dp = [1] * len(nums)
    # 先排序
    nums = sorted(nums)
    maxSet = [[nums[i]] for i in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    tmp = maxSet[j].copy()
                    tmp.append(nums[i])
                    maxSet[i] = tmp
    return maxSet[dp.index(max(dp))]

print(largestDivisibleSubset(nums))