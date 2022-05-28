# 给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。

class Solution:
    def backtracking(self, nums, index, path, target):
        if index >= len(nums):
            for p in path:
                if p != target:
                    return False
            return True

        for i in range(len(path)):
            if path[i] + nums[index] > target:
                continue
            path[i] += nums[index]
            if self.backtracking(nums, index + 1, path, target):
                return True
            path[i] -= nums[index]
            # 剪枝的关键
            # 这里由于是按照path遍历，所以是一个一个path去填满，即递归填满了第一个后再去填第二个。所以如果当前项复原后为0，那么说明后面的
            # 项依然为0。既然当前项不行，后面的项肯定也不行。
            if (path[i] == 0):
                break
        return False

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        target = sum(nums) // k
        path = [0] * k
        return self.backtracking(sorted(nums, reverse=True), 0, path, target)