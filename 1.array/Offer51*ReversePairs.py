# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
# 归并排序
class Solution:
    def __init__(self):
        self.count = 0
    def merge(self, left, right):
        i = 0
        j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
                self.count += len(left) - i
        if i == len(left):
            res.extend(right[j:])
        else:
            res.extend(left[i:])
        return res
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return self.merge(left, right)
    def reversePairs(self, nums):
        if len(nums) <= 1:
            return 0
        nums = self.mergeSort(nums)
        return self.count

nums = [7,3,2,6,0,1,5,4]
solu = Solution()
print(solu.reversePairs(nums))