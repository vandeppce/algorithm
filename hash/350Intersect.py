# 给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，
# 应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。
#

nums1 = [1,2,2,1]
nums2 = [2,2]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

def intersect(nums1, nums2):

    hash1 = {}
    for num in nums1:
        if num not in hash1.keys():
            hash1[num] = 1
        else:
            hash1[num] += 1

    hash2 = {}
    for num in nums2:
        if num not in hash2.keys():
            hash2[num] = 1
        else:
            hash2[num] += 1

    collections = list(set(nums1) & set(nums2))
    ret = []
    for collection in collections:
        number = min(hash1[collection], hash2[collection])
        for i in range(number):
            ret.append(collection)

    return ret

print(intersect(nums1, nums2))
