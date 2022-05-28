# 给定一个整数数组 arr，如果它是有效的山脉数组就返回 true，否则返回 false。
#
# 让我们回顾一下，如果 arr 满足下述条件，那么它是一个山脉数组：
#
# arr.length >= 3
# 在 0 < i < arr.length - 1 条件下，存在 i 使得：
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
#

arr = [0,3,2,1]
#arr = [3,5,5]
#arr = [2,1]
#arr = [0,2,3,5,2,1,0]
#arr = [1,2]
# 左右指针移动，必在山峰处相遇
def validMountainArray(arr):
    left = 0
    right = len(arr) - 1

    while left < len(arr) - 1 and arr[left] < arr[left + 1]:
        left += 1
    while right > 0 and arr[right] < arr[right - 1]:
        right -= 1
    return left == right and left != 0 and left != len(arr) - 1

print(validMountainArray(arr))