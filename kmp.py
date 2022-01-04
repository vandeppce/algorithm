p = "abaabac"
s = "ababaabaabac"
p = "abcabdddabcabc"

def getNext(x): # brute-force
    for i in range(x, 0, -1):
        if p[x - i + 1: x + 1] == p[:i]:
            return i
    return 0

nxt = [getNext(x) for x in range(len(p))]
print(nxt)

def buildNext():
    next = []
    next.append(0)
    x = 1
    now = x - 1

    while x < len(p):
        if p[x] == p[now]:
            now += 1
            x += 1
            next.append(now)
        elif now:
            now = next[now - 1]
        else:
            next.append(0)
            x += 1
    return next

next = buildNext()
print(next)

def search():
    tar = 0
    pos = 0
    while tar < len(s):
        if s[tar] == p[pos]:
            tar += 1
            pos += 1
        elif pos:
            pos = nxt[pos - 1]
        else:
            tar += 1
        if pos == len(p):
            print(tar - pos)
            pos = nxt[pos - 1]
search()