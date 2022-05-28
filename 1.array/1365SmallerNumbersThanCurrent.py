# 给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。
#
# 换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。
#
# 以数组形式返回答案。
#
nums = [8,1,2,2,3]
nums = [6,5,4,8]
nums = [7,7,7,7]
# 先排序
def smallerNumbersThanCurrent(nums):
    sortedNums = sorted(nums)
    res = [0] * len(nums)
    for i in range(len(nums)):
        curr = nums[i]
        idx = sortedNums.index(curr)
        res[i] = idx
    return res

print(smallerNumbersThanCurrent(nums))
