# 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
# 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
#
# 必须在不使用库的sort函数的情况下解决这个问题。
#
# 双指针
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        i = 0
        while left <= right and i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
                i -= 1
            i += 1
        print(nums)

nums = [2,0,2,1,1,0]
# nums = [2,0,1]
# nums = [1,2,0]
solu = Solution()
solu.sortColors(nums)