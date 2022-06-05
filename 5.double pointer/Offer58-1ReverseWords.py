# 输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，
# 则输出"student. a am I"。
#

class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        # 首部空格
        left = 0
        while left < len(s) and s[left] == ' ':
            left += 1
        # 尾部空格
        right = len(s) - 1
        while right >= 0 and s[right] == ' ':
            right -= 1
        # 中间空格
        tmp = ''
        while left <= right:
            if s[left] != ' ':
                tmp += s[left]
            else:
                if s[left - 1] != ' ':
                    tmp += s[left]
            left += 1
        tmp = list(tmp)

        # 字符串反向
        left = 0
        right = len(tmp) - 1
        while left <= right:
            tmp[left], tmp[right] = tmp[right], tmp[left]
            left += 1
            right -= 1

        # 单词反向
        tmp.append(' ')
        left = 0
        right = 0
        while right < len(tmp):
            if tmp[right] != ' ':
                right += 1
            else:
                tmp[left: right] = tmp[left: right][::-1]
                right += 1
                left = right
        return ''.join(tmp[:-1])