# 解码方法
# 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：
#
# "AAJF" ，将消息分组为 (1 1 10 6)
# "KJF" ，将消息分组为 (11 10 6)
# 注意，消息不能分组为  (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。
#
# 给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。
#
# 题目数据保证答案肯定是一个 32 位 的整数。

# 输入：s = "12"
# 输出：2
# 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。

s = "2260232"
# s = "226"
# s = "12"
# s = "2101"
# s = "0"
# s = "10"
# s = "2611055971756562"
s = "17"
# s = "27"

# 以2260232为例，拆以3以上或者0为间隔，拆成226 0 23 2，分别计算每一个子串的编码数，然后相乘。对于一般子串，编码数为斐波那契数列。
# 需要考虑边界条件，边界条件为末位为0，此时最后两位绑定，考虑前n-2位的编码数。末位>2并且倒数第二位为2，此时最后两位无法一起编码，因此考虑前n-1位编码数
length = len(s)
queue = []

def calculate(ll):
    if ll == ["0"]:
        return 0
    else:
        if ll[-1] == "7" or ll[-1] == "8" or ll[-1] == "9":
            if len(ll) == 1:
                return 1
            else:
                tmp = []
                for i in range(len(ll)):
                    if i < 3:
                        tmp.append(i + 1)
                    else:
                        tmp.append(tmp[i - 1] + tmp[i - 2])
                tmpp = [0]
                if ll[-2] == "2":
                    if len(ll) == 2:
                        tmpp.append(1)
                    for i in range(len(ll) - 2):
                        if i < 3:
                            tmpp.append(i + 1)
                        else:
                            tmpp.append(tmpp[i - 1] + tmpp[i - 2])
                return tmp[-1] - tmpp[-1]

        elif ll[-1] == "0":
            if len(ll) == 2:
                return 1
            else:
                tmp = []
                for i in range(len(ll) - 2):
                    if i < 3:
                        tmp.append(i + 1)
                    else:
                        tmp.append(tmp[i - 1] + tmp[i - 2])
                return tmp[-1]
        else:
            tmp = []
            for i in range(len(ll)):
                if i < 3:
                    tmp.append(i + 1)
                else:
                    tmp.append(tmp[i - 1] + tmp[i - 2])
            return tmp[-1]

cnt = []
for i in range(length):
    if s[i] == "1" or s[i] == "2":
        queue.append(s[i])
    else:
        queue.append(s[i])
        cnt.append(calculate(queue))
        queue = []
if queue:
    cnt.append(calculate(queue))
print(cnt)
