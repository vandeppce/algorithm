# 整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。
#
# 例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
# 整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。
#
# 例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
# 类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
# 而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
# 给你一个整数数组 nums ，找出 nums 的下一个排列。
#
# 必须 原地 修改，只允许使用额外常数空间。
#

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = len(nums) - 2
        while j >= 0 and nums[j] >= nums[j + 1]:
            j -= 1
        if j >= 0:
            left = j
            right = len(nums) - 1
            while nums[right] <= nums[j]:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
            nums[left + 1:] = nums[left + 1:][::-1]
        else:
            nums[:] = nums[::-1]

"""
# 更简单的写法
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # 查找临近对
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
        
            # 交换
            nums[i], nums[j] = nums[j], nums[i]

        # 后面反向
        nums[i + 1:] = nums[i + 1:][::-1]
        return nums
"""