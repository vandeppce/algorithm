# 你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
#
# 你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。
#
name = "alex"
typed = "aaleex"
name = "saeed"
typed = "ssaaedd"
# 模拟法
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name = list(name)
        typed = list(typed)
        i = 0
        j = 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                count1 = 1
                count2 = 1
                while i < len(name) - 1 and name[i] == name[i + 1]:
                    i += 1
                    count1 += 1
                while j < len(typed) - 1 and typed[j] == typed[j + 1]:
                    j += 1
                    count2 += 1
                i += 1
                j += 1
                if count1 > count2:
                    return False
            else:
                return False
        if i == len(name) and j == len(typed):
            return True
        else:
            return False

solu = Solution()
print(solu.isLongPressedName(name, typed))