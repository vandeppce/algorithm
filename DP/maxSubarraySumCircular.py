# 环形子数组的最大和
# 给定一个由整数数组 A 表示的环形数组 C，求 C 的非空子数组的最大可能和。
#
# 在此处，环形数组意味着数组的末端将会与开头相连呈环状。（形式上，当0 <= i < A.length 时 C[i] = A[i]，且当 i >= 0 时 C[i+A.length] = C[i]）
#
# 此外，子数组最多只能包含固定缓冲区 A 中的每个元素一次。（形式上，对于子数组 C[i], C[i+1], ..., C[j]，不存在 i <= k1, k2 <= j 其中 k1 % A.length = k2 % A.length）
#
#  
#
# 示例 1：
#
# 输入：[1,-2,3,-2]
# 输出：3
# 解释：从子数组 [3] 得到最大和 3

nums = [1,-2,3,-2]
nums = [5,-3,5]
length = len(nums)
fromzero = [0] * length
fromzero[0] = 1
sub = nums
for i in range(1, length):
    tmp = nums[i]
    tmp_sum = tmp + sub[i - 1]
    if tmp_sum >= tmp:
        sub[i] = tmp_sum
        if fromzero[i - 1] == 1:
            fromzero[i] = 1

if sub[-1] > 0:
    for i in range(length - 1):
        if fromzero[i] == 1:
            sub[i] += sub[-1]
print(max(sub))