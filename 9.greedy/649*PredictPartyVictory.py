# Dota2 的世界里有两个阵营：Radiant(天辉)和 Dire(夜魇)
#
# Dota2 参议院由来自两派的参议员组成。现在参议院希望对一个 Dota2 游戏里的改变作出决定。他们以一个基于轮为过程的投票进行。
# 在每一轮中，每一位参议员都可以行使两项权利中的一项：
#
# 禁止一名参议员的权利：
#
# 参议员可以让另一位参议员在这一轮和随后的几轮中丧失所有的权利。
#
# 宣布胜利：
#
#           如果参议员发现有权利投票的参议员都是同一个阵营的，他可以宣布胜利并决定在游戏中的有关变化。
#
#  
#
# 给定一个字符串代表每个参议员的阵营。字母 “R” 和 “D” 分别代表了 Radiant（天辉）和 Dire（夜魇）。然后，如果有 n 个参议员，给定字符串的大小将是 n。
#
# 以轮为基础的过程从给定顺序的第一个参议员开始到最后一个参议员结束。这一过程将持续到投票结束。所有失去权利的参议员将在过程中被跳过。
#
# 假设每一位参议员都足够聪明，会为自己的政党做出最好的策略，你需要预测哪一方最终会宣布胜利并在 Dota2 游戏中决定改变。输出应该是 Radiant 或 Dire。
#

senate = "DRRDRDRDRDDRDRDRD"

"""
# 方法一，超时
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        status = [1] * len(senate)
        while True:
            pre_status = status.copy()
            nextHash = {}
            for i in range(len(senate)):
                if status[i] == 0:
                    pass
                else:
                    if senate[i] not in nextHash.keys():
                        nextIdx = i + 1
                    else:
                        nextIdx = max(nextHash[senate[i]], i + 1)
                    for j in range(nextIdx, len(senate) + i + 1):
                        if senate[j % len(senate)] != senate[i] and status[j % len(senate)] == 1:
                            status[j % len(senate)] = 0
                            nextHash[senate[i]] = j % len(senate) + 1
                            break
            if pre_status == status:
                for i in range(len(status)):
                    if status[i] == 1:
                        team = senate[i]
                        if team == "R":
                            return "Radiant"
                        else:
                            return "Dire"
"""

"""
# 方法二，仍然超时
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = 2.list(senate)
        while True:
            pre = senate.copy()
            outList = []
            for i in range(len(senate)):
                if i in outList:
                    continue
                for j in range(i + 1, len(senate) + i + 1):
                    if senate[j % len(senate)] != senate[i] and j % len(senate) not in outList:
                        outList.append(j % len(senate))
                        break
            outList = sorted(outList, reverse=True)
            for idx in outList:
                senate.pop(idx)
            if pre == senate:
                return "Radiant" if senate[0] == "R" else "Dire"
"""
senate = "DDR"

def predictRartyVictory(senate):
    senate = list(senate)
    flag = 0
    R = True
    D = True

    while R and D:
        R = False
        D = False
        for i in range(len(senate)):
            if senate[i] == "R":
                if flag < 0: #说明前面D多，消灭
                    senate[i] = "0"
                else:
                    R = True
                flag += 1 # flag操作放在判断之外，因为如果消灭，抵消掉一个D，flag+1，如果不消灭，增加一个R，flag+1
            if senate[i] == "D":
                if flag > 0:
                    senate[i] = "0"
                else:
                    D = True
                    flag -= 1
    return "Radiant" if R else "Dire"

print(predictRartyVictory(senate))