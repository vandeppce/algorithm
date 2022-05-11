# 你将得到一个整数数组 matchsticks ，其中 matchsticks[i] 是第 i 个火柴棒的长度。你要用 所有的火柴棍 拼成一个正方形。
# 你 不能折断 任何一根火柴棒，但你可以把它们连在一起，而且每根火柴棒必须 使用一次 。
#
# 如果你能使这个正方形，则返回 true ，否则返回 false 。
#

# 提前分出来4个子集
class Solution:
    def __init__(self):
        self.path = [0, 0, 0, 0]

    def backtracking(self, matchsticks, index, target):
        if index >= len(matchsticks):
            if self.path[0] == self.path[1] == self.path[2] == self.path[3]:
                return True
            return False

        for i in range(len(self.path)):
            if self.path[i] + matchsticks[index] > target:
                continue
            self.path[i] += matchsticks[index]
            if self.backtracking(matchsticks, index + 1, target):
                return True
            self.path[i] -= matchsticks[index]
        return False

    def makesquare(self, matchsticks) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        target = sum(matchsticks) // 4
        return self.backtracking(sorted(matchsticks, reverse=True), 0, target)

matchsticks = [5,5,5,5,4,4,4,4,3,3,3,3]
solu = Solution()
print(solu.makesquare(matchsticks))