# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。
# 每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
#
# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
#
# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
#
# 字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。
#
# 广度优先搜索，主要在优化时间上，注意used和dead数组
deadends = ["8888"]
target = "0009"
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"

def neighbor(key):
    ret = []
    for i in range(4):
        x = int(key[i])
        for d in (-1, 1):
            y = (x + d) % 10
            # yield key[:i] + str(y) + key[i + 1:]
            ret.append(key[:i] + str(y) + key[i + 1:])
    return ret

def openLock(deadends, target):
    queue = ["0000"]
    used = {"0000"}
    dead = set(deadends)
    times = 0
    if "0000" in deadends:
        return -1

    while queue:
        for i in range(len(queue)):
            key = queue.pop(0)
            if key == target:
                return times
            for nei in neighbor(key):
                if nei not in used and nei not in dead:
                    queue.append(nei)
                    used.add(nei)
        times += 1
    return -1

print(openLock(deadends, target))