# 给定一个含有 n 个正整数的数组和一个正整数 target 。
#
# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

# 快慢指针（滑动窗口）

target = 7
nums = [2,3,1,2,4,3]

# target = 4
# nums = [1,4,4]


# target = 11
# nums = [1,1,1,1,1,1,1,1]

# target = 4
# nums = [4]

# target = 15
# nums = [5,1,3,5,10,7,4,9,2,8]
target = 11
nums = [1,1,1,1,1,1,1,1]
length = len(nums)
slow = 0
fast = 0
current_min = length

print(sum(nums))
if sum(nums) < target:
    print(0)
while fast < length:
    if slow == fast:
        count = nums[fast]
    else:
        count = sum(nums[slow: fast + 1])

    if count < target:
        fast += 1
    else:
        current_min = min(fast - slow + 1, current_min)
        slow += 1

print(current_min)

"""
# 二刷，双指针
def minSubArrayLen(target, nums):
    slow = 0
    fast = 0

    total = 0
    minLength = float("inf")
    if sum(nums) < target:
        return 0

    while fast < len(nums):
        while total < target and fast < len(nums):
            total += nums[fast]
            fast += 1

        while total >= target and slow < fast:
            total -= nums[slow]
            slow += 1

        minLength = min(minLength, fast - slow + 1)
    return minLength
"""