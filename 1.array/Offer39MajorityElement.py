# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 哈希
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numHash = {}
        for num in nums:
            numHash[num] = numHash.get(num, 0) + 1
            if numHash[num] > len(nums) // 2:
                return num

# 摩尔投票
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

# 分治
# 如果a是数组的众数，如果将数组分成两部分，那么a至少是其中一部分的众数
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def majority_element_rec(lo, hi) -> int:
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid + 1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums) - 1)