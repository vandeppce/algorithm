# 假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。
# 每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。
#
# 请你重新构造并返回输入数组 people 所表示的队列。返回的队列应该格式化为数组 queue ，
# 其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性（queue[0] 是排在队列前面的人）。
#

# h升序，k降序，则k代表当前剩余位置中的索引
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]

def reconstructQueue(people):
    res = [[0, 0]] * len(people)
    index = list(range(len(people)))
    people = sorted(people, key = lambda item: (item[0], -item[1]))
    for p in people:
        idx = index[p[1]]
        res[idx] = p
        index.pop(p[1])
    return res

print(reconstructQueue(people))