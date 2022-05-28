# 给你一个整数数组 nums，返回 nums 中最长等差子序列的长度。
#
# 回想一下，nums 的子序列是一个列表 nums[i1], nums[i2], ..., nums[ik] ，且 0 <= i1 < i2 < ... < ik <= nums.length - 1。
# 并且如果 seq[i+1] - seq[i]( 0 <= i < seq.length - 1) 的值都相同，那么序列 seq 是等差的。
#

nums = [3,6,9,12]
nums = [9,4,7,2,10]
nums = [20,1,15,3,10,5,8]
nums = [3, 6, 9]
nums = [83,20,17,43,52,78,68,45]
nums = [12,28,13,6,34,36,53,24,29,2,23,0,22,25,53,34,23,50,35,43,53,11,48,56,44,53,31,6,31,57,46,6,17,42,48,28,5,24,0,14,43,12,21,6,30,37,16,56,19,45,51,10,22,38,39,23,8,29,60,18]
nums = [6,6,6,6]
# 和最长斐波那契那题差不多，只不过这里由于nums是无序的，而且可能包含重复值，因此不能提前扫描得到hash，要边遍历边填充hash
def longestArithSeqLength(nums):
    dp = [[0] * len(nums) for _ in range(len(nums))]
    idxHash = {}
    idxHash[nums[0]] = 0
    maxLenghth = 0
    for i in range(1, len(nums)):
        for j in range(i + 1, len(nums)):
            k = idxHash.get(2 * nums[i] - nums[j], -1)
            if k != -1 and k <= i:
                dp[i][j] = dp[k][i] + 1
                maxLenghth = max(maxLenghth, dp[i][j])
        idxHash[nums[i]] = i
    return maxLenghth + 2

print(longestArithSeqLength(nums))
