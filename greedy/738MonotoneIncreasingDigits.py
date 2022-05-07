# 当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。
#
# 给定一个整数 n ，返回 小于或等于 n 的最大数字，且数字呈 单调递增 。
#

n = 10
# n = 1234
# n = 342
# n = 120

# 贪心，遇到小于前数的位置时，追溯到最先出现前数的位置，减一，余下的位全部变成9
def monotoneIncreasingDigits(n):
    if n < 10:
        return n

    nums = []
    while n:
        nums.insert(0, n % 10)
        n = n // 10

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            j = i - 1
            while j >= 1 and nums[j - 1] == nums[j]:
                j -= 1

            nums[j] -= 1
            nums[j + 1:] = [9] * len(nums[j + 1:])

    ret = nums[-1]
    pow = 10
    for i in range(len(nums) - 2, -1, -1):
        ret += nums[i] * pow
        pow *= 10
    return ret

"""
# 二刷，差不多，从数组重构数值的过程不一样
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n < 10:
            return n
            
        nums = []
        while n:
            nums.insert(0, n % 10)
            n = n // 10
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                j = i - 1
                while j > 0 and nums[j - 1] == nums[j]:
                    j -= 1
                nums[j] -= 1
                nums[j + 1:] = [9] * (len(nums) - j - 1)
        
        ret = nums.pop()
        flag = 10

        while nums:
            ret += nums.pop() * flag
            flag *= 10
        return ret
"""
print(monotoneIncreasingDigits(n))