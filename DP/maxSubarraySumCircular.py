# 环形子数组的最大和
# 给定一个由整数数组 A 表示的环形数组 C，求 C 的非空子数组的最大可能和。
#
# 在此处，环形数组意味着数组的末端将会与开头相连呈环状。（形式上，当0 <= i < A.length 时 C[i] = A[i]，且当 i >= 0 时 C[i+A.length] = C[i]）
#
# 此外，子数组最多只能包含固定缓冲区 A 中的每个元素一次。（形式上，对于子数组C[i], C[i+1], ..., C[j]，不存在 i <= k1, k2 <= j 其中 k1 % A.length = k2 % A.length）
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

count = nums.copy()
length = len(nums)
for i in range(1, length):
    count[i] = max(nums[i], nums[i] + count[i - 1])
if max(count) < 0:
    print(max(count))
else:
    ans = max(count)

# 对于环形，最大值=总和减去最小和子序列。例如5,-3,5，最大为5+5，即相当于总和减去-3
count = nums.copy()
for i in range(1, length):
    count[i] = min(nums[i], nums[i] + count[i - 1])
ans = max(ans, sum(nums) - min(count))
print(ans)