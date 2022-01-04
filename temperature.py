# 根据每日 气温 列表 temperatures ，请计算在每一天需要等几天才会有更高的温度。如果气温在这之后都不会升高，请在该位置用 0 来代替。
# 输入: temperatures = [73,74,75,71,69,72,76,73]
# 输出: [1,1,4,2,1,1,0,0]

temperatures = [73,74,75,71,69,72,76,73]
temperatures = [30,40,50,60]
temperatures = [30,60,90]
temperatures = [90]

length = len(temperatures)
res = [0] * length
stack = []
for i in range(length):
    present = temperatures[i]

    while stack != [] and present > temperatures[stack[-1]]:
        previous = stack.pop()
        res[previous] = i - previous
    # append 比 insert效率高
    stack.append(i)
print(res)