# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，
# 找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
#
# candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 
#
# 对于给定的输入，保证和为 target 的不同组合数少于 150 个。
#

class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def backtracking(self, candidates, target, total, start):
        if total == target:
            self.res.append(self.path[:])
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            self.path.append(candidates[i])
            total += candidates[i]
            self.backtracking(candidates, target, total, i)
            total -= candidates[i]
            self.path.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.backtracking(candidates, target, 0, 0)
        return self.res

candidates = [2,3,6,7]
target = 7

solu = Solution()
print(solu.combinationSum(candidates, target))