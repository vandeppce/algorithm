# 在柠檬水摊上，每一杯柠檬水的售价为 5 美元。顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
#
# 每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
#
# 注意，一开始你手头没有任何零钱。
#
# 给你一个整数数组 bills ，其中 bills[i] 是第 i 位顾客付的账。如果你能给每位顾客正确找零，返回 true ，否则返回 false 。
#

# 遇到20元时，先消耗10，再消耗5
bills = [5,5,5,10,20]
bills = [5,5,10,10,20]
bills = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]

def lemonadeChange(bills):
    rest = {5: 0, 10: 0}
    for bill in bills:
        if bill == 5:
            rest[5] += 1
        elif bill == 10:
            if rest[5] > 0:
                rest[5] -= 1
                rest[10] += 1
            else:
                return False
        else:
            if rest[5] >= 1 and rest[10] >= 1:
                rest[5] -= 1
                rest[10] -= 1
            elif rest[5] >= 3:
                rest[5] -= 3
            else:
                return False
    return True

print(lemonadeChange(bills))