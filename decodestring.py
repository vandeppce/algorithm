# 字符串解码
# 给定一个经过编码的字符串，返回它解码后的字符串。
#
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
#
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
#
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

s = "3[a]2[bc]"
s = "3[a2[c]]"
s = "2[abc]3[cd]ef"
s = "abc3[cd]xyz"
s = "100[leetcode]"
s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
if s == "":
    print(s)

stack = []
for item in s:
    if item != ']':
        stack.append(item)
    else:
        tmp = ""
        cnt = ""
        cpy = ""
        while stack != []:
            a = stack.pop()
            if a != '[':
                tmp = a + tmp
            else:
                break
        while stack != [] and stack[-1] in num_list:
            b = stack.pop()
            cnt += b
        for i in range(int(cnt[::-1])):
            cpy += tmp
        stack.append(cpy)
ret = ""
for item in stack:
    ret += item
print(ret)