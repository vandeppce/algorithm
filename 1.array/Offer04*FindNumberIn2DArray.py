# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
#

# 观察可知，右上角元素是每行最大的，并是该列最小的。因此从右上角开始搜索，若小于target则下移，大于则左移
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

target = 17

def findNumberIn2DArray(matrix, target):
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])
    x = n - 1
    y = 0
    while x >= 0 and y <= m - 1:
        if matrix[y][x] == target:
            return True
        elif matrix[y][x] > target:
            x -= 1
        else:
            y += 1
    return False

print(findNumberIn2DArray(matrix, target))