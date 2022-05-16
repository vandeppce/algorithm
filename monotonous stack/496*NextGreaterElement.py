# nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。
#
# 给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。
#
# 对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。
# 如果不存在下一个更大元素，那么本次查询的答案是 -1 。
#
# 返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。
#

nums1 = [4,1,2]
nums2 = [1,3,4,2]
nums1 = [2,4]
nums2 = [1,2,3,4]

# 栈记录nums2中的递减序列，当遇到nums2[i]大于栈顶值时，说明有可能遇到了更大的值，则出栈并检查nums1中索引
def nextGreaterElement(nums1, nums2):
    res = [-1] * len(nums1)
    stack = [0]

    for i in range(1, len(nums2)):
        if nums2[i] <= nums2[stack[-1]]:
            stack.append(i)
        else:
            while stack and nums2[i] > nums2[stack[-1]]:
                idx = stack.pop()
                if nums2[idx] in nums1:
                    res[nums1.index(nums2[idx])] = nums2[i]
            stack.append(i)
    return res

"""
# 二刷
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        stack = [[0, nums2[0]]]
        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1][1]:
                temp = stack.pop()
                idx = temp[0]
                value = temp[1]
                if value in nums1:
                    res[nums1.index(value)] = nums2[i]
            stack.append([i, nums2[i]])
        return res
"""
print(nextGreaterElement(nums1, nums2))