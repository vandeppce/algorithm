# 你正在探访一家农场，农场从左到右种植了一排果树。这些树用一个整数数组 fruits 表示，其中 fruits[i] 是第 i 棵树上的水果 种类 。
#
# 你想要尽可能多地收集水果。然而，农场的主人设定了一些严格的规矩，你必须按照要求采摘水果：
#
# 你只有 两个 篮子，并且每个篮子只能装 单一类型 的水果。每个篮子能够装的水果总量没有限制。
# 你可以选择任意一棵树开始采摘，你必须从 每棵 树（包括开始采摘的树）上 恰好摘一个水果 。
# 采摘的水果应当符合篮子中的水果类型。每采摘一次，你将会向右移动到下一棵树，并继续采摘。
# 一旦你走到某棵树前，但水果不符合篮子的水果类型，那么就必须停止采摘。
# 给你一个整数数组 fruits ，返回你可以收集的水果的 最大 数目。
#

# 滑动窗口

fruits = [3,3,3,1,2,1,1,2,3,3,4]
fruits = [1,2,1]
fruits = [0,1,2,2]
fruits = [1,2,3,2,2]
fruits = [4,1,1,1,3,1,7,5]
fruits = [3,3,3,1,2,1,1,2,3,3,4,3,4,4,4]
def totalFruit(fruits):
    length = len(fruits)
    slow = 0
    fast = 0
    currentFruit = []
    maxFruit = 0

    while fast < length:
        tmp = fruits[fast]
        if tmp not in currentFruit:
            if len(currentFruit) < 2:
                currentFruit.append(tmp)
                fast += 1
            else:
                maxFruit = max(maxFruit, fast - slow)
                retainFruit = fruits[fast - 1]
                tmp1 = fast - 1
                updateSlow = 0
                while tmp1 > slow:
                    tmp1 -= 1
                    if fruits[tmp1] != retainFruit:
                        updateSlow = tmp1 + 1
                        break
                slow = updateSlow
                currentFruit = [retainFruit, tmp]
                fast += 1
        else:
            fast += 1
    return max(maxFruit, fast - slow)

"""
# 二刷，单指针，使用hash
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hasFruit = []
        selected = []
        maxNum = 0
        for i in range(len(fruits)):
            if fruits[i] in hasFruit:
                selected.append(fruits[i])
            else:
                if len(hasFruit) < 2:
                    hasFruit.append(fruits[i])
                    selected.append(fruits[i])
                else:
                    maxNum = max(maxNum, len(selected))
                    prev = selected[-1]
                    j = len(selected) - 1
                    while j >= 0 and selected[j - 1] == selected[j]:
                        j = j - 1
                    selected = selected[j:]
                    selected.append(fruits[i])
                    hasFruit = [prev]
                    hasFruit.append(fruits[i])
        return max(maxNum, len(selected))
"""
print(totalFruit(fruits))