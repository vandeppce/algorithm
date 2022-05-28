# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
# 它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
# 例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
#

m = 7
n = 2
k = 3

class Solution:
    def __init__(self):
        self.count = 0
    def calSum(self, i, j):
        num1 = 0
        for c in str(i):
            num1 += int(c)
        num2 = 0
        for c in str(j):
            num2 += int(c)
        return num1 + num2
    def backtracking(self, m, n, i, j, k, hasSeen):
        # 注意这里没有显式的回溯过程，因为这里只需要可以遍历到的节点即可，对于节点ij来说，先往上走，上面的所有路径走完以后，就会回退到
        # 自身，然后接着往下走即可，不需要回溯
        if i < 0 or i > m - 1 or j < 0 or j > n - 1:
            return
        if self.calSum(i, j) > k:
            return
        if hasSeen[i][j] != 1:
            hasSeen[i][j] = 1
            self.count += 1
            self.backtracking(m, n, i - 1, j, k, hasSeen)
            self.backtracking(m, n, i + 1, j, k, hasSeen)
            self.backtracking(m, n, i, j - 1, k, hasSeen)
            self.backtracking(m, n, i, j + 1, k, hasSeen)

    def movingCount(self, m: int, n: int, k: int) -> int:
        hasSeen = [[0] * n for _ in range(m)]
        self.backtracking(m, n, 0, 0, k, hasSeen)
        return self.count

solu = Solution()
print(solu.movingCount(m, n, k))