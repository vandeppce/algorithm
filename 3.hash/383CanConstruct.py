# 给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
#
# 如果可以，返回 true ；否则返回 false 。
#
# magazine 中的每个字符只能在 ransomNote 中使用一次。

ransomNote = "a"
magazine = "b"

ransomNote = "aa"
magazine = "ab"

ransomNote = "aa"
magazine = "aab"
def canConstruct(ransomNote, magazine):
    hashM = {}
    for chr in magazine:
        if chr not in hashM.keys():
            hashM[chr] = 1
        else:
            hashM[chr] += 1

    for chr in ransomNote:
        if chr in hashM:
            hashM[chr] -= 1
            if hashM[chr] == 0:
                del hashM[chr]
        else:
            return False
    return True

print(canConstruct(ransomNote, magazine))

"""
# 二刷
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashM = {}
        for chrM in magazine:
            hashM[chrM] = hashM.get(chrM, 0) + 1
        
        for chrR in ransomNote:
            if chrR in hashM.keys():
                hashM[chrR] -= 1
                if hashM[chrR] == 0:
                    del hashM[chrR]
            else:
                return False
        return True
"""