# 俄罗斯套娃信封问题
# 给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。
#
# 当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
#
# 请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
#
# 注意：不允许旋转信封。
#
#  
# 示例 1：
#
# 输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
# 输出：3
# 解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
# 排序 + 最长递增子序列

envelopes = [[5,4],[6,4],[6,7],[2,3]]
envelopes = [[1,1],[1,1],[1,1]]
sorted_env = sorted(envelopes)
length = len(envelopes)
nums = [1] * length

for i in range(length):
    tmp = 1
    for j in range(i):
        if sorted_env[i][0] > sorted_env[j][0] and sorted_env[i][1] > sorted_env[j][1]:
            tmp = max(tmp, nums[j] + 1)
    nums[i] = tmp
print(max(nums))
