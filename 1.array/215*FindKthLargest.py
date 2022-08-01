# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
#
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

# 堆
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        hp = nums[:k]
        heapq.heapify(hp)
        for i in range(k, n):
            if nums[i] > hp[0]:
                heapq.heappush(hp, nums[i])
            if len(hp) > k:
                heapq.heappop(hp)
        return hp[0]