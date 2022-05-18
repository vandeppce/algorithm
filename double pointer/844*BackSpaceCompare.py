class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def find(s):
            s = list(s)
            slow = 0
            fast = 0
            while fast < len(s):
                if s[fast] != "#":
                    s[slow] = s[fast]
                    slow += 1
                    fast += 1
                else:
                    slow = max(slow - 1, 0)
                    fast += 1
            return s[:slow]
        return find(s) == find(t)