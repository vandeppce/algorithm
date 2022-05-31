# 输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

nums = [3,30,34,5,9]
# 本质上是对字符串进行排序，对于字符串x，y，如果x+y>y+x，则x>y，反之亦然。使用快排对数组进行排序，然后拼接即可

def quick_sort(nums, l, r):
    if l >= r:
        return
    i, j = l, r
    while i < j:
        while i < j and nums[j] + nums[l] >= nums[l] + nums[j]:
            j -= 1
        while i < j and nums[i] + nums[l] <= nums[l] + nums[i]:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i], nums[l] = nums[l], nums[i]
    quick_sort(nums, l, i - 1)
    quick_sort(nums, i + 1, r)
    return nums

def minNumber(nums):
    if len(nums) == 1:
        return str(nums[0])
    nums = [str(num) for num in nums]
    nums = quick_sort(nums, 0, len(nums) - 1)
    return ''.join(nums)

print(minNumber(nums))