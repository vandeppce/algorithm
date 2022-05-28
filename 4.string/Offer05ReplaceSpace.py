# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

s = "We are happy."

'''
# 申请新数组
def replaceSpace(s):
    s_list = s.split(" ")
    res = ""
    for s in s_list:
        res = res + s + "%20"
    return res[:-3]
'''

# 双指针法
def replaceSpace(s):
    counter = s.count(' ')

    res = list(s)
    # 每碰到一个空格就多拓展两个格子，1 + 2 = 3个位置存’%20‘
    res.extend([' '] * counter * 2)

    # 原始字符串的末尾，拓展后的末尾
    left, right = len(s) - 1, len(res) - 1

    while left >= 0:
        if res[left] != ' ':
            res[right] = res[left]
            right -= 1
        else:
            # [right - 2, right), 左闭右开
            res[right - 2: right + 1] = '%20'
            right -= 3
        left -= 1
    return ''.join(res)
print(replaceSpace(s))