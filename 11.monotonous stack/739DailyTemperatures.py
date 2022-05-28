# 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，
# 其中 answer[i] 是指在第 i 天之后，才会有更高的温度。如果气温在这之后都不会升高，请在该位置用 0 来代替。
#

temperatures = [73,74,75,71,69,72,76,73]
temperatures = [30,40,50,60]
temperatures = [30,60,90]

# 用二元数组，一个表示温度，一个表示索引
def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    stack = [[temperatures[0], 0]]
    for i in range(1, len(temperatures)):
        while stack and temperatures[i] > stack[-1][0]:
            idx = stack.pop()[1]
            res[idx] = i - idx
        stack.append([temperatures[i], i])
    return res

# 方法二，栈中只保存索引
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res
print(dailyTemperatures(temperatures))