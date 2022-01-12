# 分割回文串 II
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
#
# 返回符合要求的 最少分割次数 。
#
#  
#
# 示例 1：
#
# 输入：s = "aab"
# 输出：1
# 解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。

s = "aab"
# s = "a"
# s = "ab"
# s = "aabcaccad"
# s = "aabbaaaaa"
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

# cnt[i]记录到第i个元素时最少需要分割次数，将已遍历元素存在box中，则考虑以下几种情况：
# s[i]不在box中，说明是新元素，则cnt[i]=cnt[i-1]+1
# box+s[i]成为回文串，则cnt[i]=0
# 若在i之前存在最近的k，使cnt[k-1]>cnt[k]，说明在k位置时构成了一个新的回文长串，
# 因此重新计算k之后到i的s串是否构成回文，如果是，则cnt[i]可能的值为cnt[k]+1，记为a
# 并且，对于每一个s[i]，寻找box中距离它最远的可以构成回文串的位置t，则cnt[i]可能的值为cnt[t]+1，记为b
# cnt[i] = min(a, b)

box = s[0]
length = len(s)
cnt = [0] * length
for i in range(1, length):
    if not s[i] in box:
        cnt[i] = cnt[i - 1] + 1
    else:
        x = box + s[i]
        if x[::-1] == x:
            cnt[i] = 0
        else:
            a = ""
            m = cnt[i - 1] + 1
            flag = 0
            for k in range(i - 1, -1, -1):
                if cnt[k] < cnt[k - 1]:
                    a = box[k + 1:] + s[i]
                    break
            if a != "" and a[::-1] == a:
                m = cnt[k] + 1
            for j in range(len(box)):
                if box[j] == s[i]:
                    tmp = box[j:] + s[i]
                    if tmp == tmp[::-1]:
                        flag = 1
                        if j == 0:
                            cnt[i] = 0
                        else:
                            cnt[i] = min(cnt[j - 1] + 1, cnt[i - 1] + 1, m)
                        break
            if flag == 0:
                cnt[i] = cnt[i - 1] + 1
    box += s[i]
print(cnt)