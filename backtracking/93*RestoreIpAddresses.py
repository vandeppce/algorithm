# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
#
# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
# 给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，
# 这些地址可以通过在 s 中插入 '.' 来形成。你 不能 重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。
#

# 回溯，两种情况判断
class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def backtracking(self, s, start):
        if start >= len(s):
            if len(self.path) == 4:
                path = ""
                for item in self.path[:-1]:
                    path = path + str(item) + "."
                self.res.append(path + str(self.path[-1]))
            return

        for i in range(start, len(s)):
            substr = s[start: i + 1]
            if len(substr) > 1 and int(substr) <= 255 and substr[0] != '0':
                self.path.append(substr)
                self.backtracking(s, i + 1)
                self.path.pop()

            elif len(substr) == 1:
                self.path.append(substr)
                self.backtracking(s, i + 1)
                self.path.pop()

            else:
                break
    def restoreIpAddresses(self, s: str):
        self.backtracking(s, 0)
        return self.res

"""
# 二刷，注意判断条件
class Solution:
    def __init__(self):
        self.path = []
        self.res = []
    
    def backtracking(self, s, start):
        if start >= len(s):
            if len(self.path) == 4:
                ip = ""
                for tmp in self.path:
                    ip += tmp + "."
                self.res.append(ip[:-1])
            return
        for i in range(start, len(s)):
            curr = s[start: i + 1]
            if (curr[0] == '0' and len(curr) == 1) or (curr[0] != '0' and int(curr) <= 255):
                self.path.append(curr)
                self.backtracking(s, i + 1)
                self.path.pop()

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.backtracking(s, 0)
        return self.res
"""