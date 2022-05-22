# 给定一个非负整数数组 nums，  nums 中一半整数是 奇数 ，一半整数是 偶数 。
#
# 对数组进行排序，以便当 nums[i] 为奇数时，i 也是 奇数 ；当 nums[i] 为偶数时， i 也是 偶数 。
#
# 你可以返回 任何满足上述条件的数组作为答案 。
#

nums = [4,2,5,7]
nums = [2, 3]
def sortArrayByParity(nums):
    nums1 = []
    nums2 = []
    res = []
    for num in nums:
        if num % 2 == 1:
            nums1.append(num)
        else:
            nums2.append(num)
    for i in range(len(nums1)):
        res.append(nums2[i])
        res.append(nums1[i])
    return res

print(sortArrayByParity(nums))