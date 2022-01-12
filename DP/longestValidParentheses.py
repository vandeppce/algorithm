# 最长有效括号
# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
#
#  
#
# 示例 1：
#
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"

s = "(()"
#s = ")()())"
#s = ""
#s = "()(()"

# 栈，记录每个位置的括号是否被匹配，匹配标志位为1，计算最长的1序列
queue = []
queue_idx = []

length = len(s)
idxs = [0] * length

cnt = 0
count = 0
flag = 0

for i in range(length):
    if s[i] == "(":
        queue.append(s[i])
        queue_idx.append(i)
    else:
        if queue:
            queue.pop()
            idx = queue_idx.pop()
            idxs[idx] = 1
            idxs[i] = 1
print(idxs)
count = 0
tmp = 0
while idxs:
    x = idxs.pop(0)
    if x == 0:
        count = max(tmp, count)
        tmp = 0
    else:
        tmp += 1
print(count)