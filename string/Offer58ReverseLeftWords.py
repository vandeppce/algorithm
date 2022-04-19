# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
# 请定义一个函数实现字符串左旋转操作的功能。
# 比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。
#

s = "abcdefg"
k = 2

'''
# 申请额外空间
def reverseLeftWords(s, n):
    return "".join(s[n:]) + s[:n]
'''

# 先反转前k个，再反转后k个，最后反转整个字符串
def reverseLeftWords(s, n):
    s = list(s)
    s[:n] = s[:n][::-1]
    s[n:] = s[n:][::-1]
    return "".join(s[::-1])

print(reverseLeftWords(s, k))