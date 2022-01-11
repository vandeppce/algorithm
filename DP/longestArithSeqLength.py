# 最长等差数列
# 给你一个整数数组 nums，返回 nums 中最长等差子序列的长度。
#
# 回想一下，nums 的子序列是一个列表 nums[i1], nums[i2], ..., nums[ik] ，且 0 <= i1 < i2 < ... < ik <= nums.length - 1。并且如果 seq[i+1] - seq[i]( 0 <= i < seq.length - 1) 的值都相同，那么序列 seq 是等差的。
#
#  
#
# 示例 1：
#
# 输入：nums = [3,6,9,12]
# 输出：4
# 解释：
# 整个数组是公差为 3 的等差数列。
import collections

nums = [3,6,9,12]
# nums = [9,4,7,2,10]
# nums = [20,1,15,3,10,5,8]
# nums = [3, 6, 9]
nums = [83,20,17,43,52,78,68,45]
nums = [12,28,13,6,34,36,53,24,29,2,23,0,22,25,53,34,23,50,35,43,53,11,48,56,44,53,31,6,31,57,46,6,17,42,48,28,5,24,0,14,43,12,21,6,30,37,16,56,19,45,51,10,22,38,39,23,8,29,60,18]
# nums = [6,6,6,6]
dic = {}
longest = collections.defaultdict(lambda: 2)
length = len(nums)
max_cnt = 2

for i in range(length):
    for j in range(i + 1, length):
        tmp = 2 * nums[i] - nums[j]
        if tmp in dic:
            ans = longest[i, j] = longest[dic[tmp], i] + 1
            max_cnt = max(ans, max_cnt)
    dic[nums[i]] = i
print(max_cnt)