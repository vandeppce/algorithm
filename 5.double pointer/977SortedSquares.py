class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = []
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res.insert(0, nums[left] * nums[left])
                left += 1
            else:
                res.insert(0, nums[right] * nums[right])
                right -= 1
        return res