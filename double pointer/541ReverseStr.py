class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        slow = 0
        fast = 0
        res = ""
        while fast < len(s):
            if fast - slow < 2 * k:
                fast += 1
            else:
                res += s[slow: slow + k][::-1]
                res += s[slow + k: fast]
                slow = fast
        res += s[slow: slow + k][::-1]
        res += s[slow + k:]
        return res