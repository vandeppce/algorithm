# 给你一个字符串 s ，颠倒字符串中 单词 的顺序。

s = "the sky is blue"
s = "  hello world  "
s = "a good   example"

# 正常方法
def reverseWords(s):
    s_list = s.split(" ")[::-1]
    res = ""
    for s in s_list:
        if s != "":
            res = res + s + " "
    return res[:-1]

print(reverseWords(s))