# 找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：
#
# 只使用数字1到9
# 每个数字 最多使用一次 
# 返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。
#

class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def backtracking(self, k, n, start, total):
        if total > n:
            return

        if len(self.path) == k:
            if total == n:
                self.res.append(self.path[:])
            return

        for i in range(start, 10 - (k - len(self.path)) + 1):
            total += i
            self.path.append(i)
            self.backtracking(k, n, i + 1, total)
            self.path.pop()
            total -= i

    def combinationSum3(self, k: int, n: int):
        self.backtracking(k, n, 1, 0)
        return self.res

"""
# 二刷，直接在n上操作
class Solution:
    def __init__(self):
        self.path = []
        self.res = []
    
    def backtracking(self, k, n, start):
        if n < 0:
            return
            
        if len(self.path) == k:
            if not n:
                self.res.append(self.path[:])
        
        for i in range(start, 10):
            n -= i
            self.path.append(i)
            self.backtracking(k, n, i + 1)
            n += i
            self.path.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backtracking(k, n, 1)
        return self.res
"""
solu = Solution()
print(solu.combinationSum3(9, 45))