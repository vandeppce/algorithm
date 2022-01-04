# 给定一个含有 n 个正整数的数组和一个正整数 target 。
# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组

nums = [12,28,83,4,25,26,25,2,25,25,25,12]
target = 213

fast = 0
slow = 0
total = 0
res = len(nums)
while fast < len(nums):
    total += nums[fast]
    if total >= target:
        res = min(res, fast - slow + 1)
    while total - nums[slow] >= target:
        total -= nums[slow]
        slow += 1
        res = min(res, fast - slow + 1)
    fast += 1
print(res)