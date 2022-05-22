# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用 一次 。
#
# 注意：解集不能包含重复的组合。
#
# 注意和39，216解法上的区别
class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def backtracking(self, candidates, target, total, start):
        if total > target:
            return
        if total == target:
            self.res.append(self.path[:])
            return

        for i in range(start, len(candidates)):
            # 这里判断同层的重复元素
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            self.path.append(candidates[i])
            total += candidates[i]
            self.backtracking(candidates, target, total, i + 1)
            total -= candidates[i]
            self.path.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.backtracking(sorted(candidates), target, 0, 0)
        return self.res