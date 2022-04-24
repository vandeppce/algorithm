s = "ababababab"
# needle = "actgpacy"
def getnext(needle):
    next = [0] * len(needle)
    j = 0
    for i in range(1, len(needle)):
        while (j > 0 and needle[i] != needle[j]):
            j = next[j - 1]
            # j -= 1 也可
        if (needle[i] == needle[j]):
            j += 1
        next[i] = j
    return next


print(getnext(s))