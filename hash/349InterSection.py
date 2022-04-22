# 给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。

nums1 = [1,2,2,1]
nums2 = [2,2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

# return list(set(nums1) & set(nums2))

def intersection(nums1, nums2):
    # return list(set(nums1) & set(nums2))
    nums1 = set(nums1)
    nums2 = set(nums2)

    hash1 = {}
    ret = []

    for num in nums1:
        if num not in hash1.keys():
            hash1[num] = 1
        else:
            hash1[num] += 1
    for num in nums2:
        if num in hash1.keys():
            ret.append(num)

    return ret

print(intersection(nums1, nums2))