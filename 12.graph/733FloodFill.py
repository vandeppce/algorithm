# 有一幅以 m x n 的二维整数数组表示的图画 image ，其中 image[i][j] 表示该图画的像素值大小。
#
# 你也被给予三个整数 sr ,  sc 和 newColor 。你应该从像素 image[sr][sc] 开始对图像进行 上色填充 。
#
# 为了完成 上色工作 ，从初始像素开始，记录初始坐标的 上下左右四个方向上 像素值与初始坐标相同的相连像素点，
# 接着再记录这四个方向上符合条件的像素点与他们对应 四个方向上 像素值与初始坐标相同的相连像素点，……，重复该过程。
# 将所有有记录的像素点的颜色值改为 newColor 。
#
# 最后返回 经过上色渲染后的图像 。
#
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
newColor = 2

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        if color == newColor:
            return image
        numRow = len(image)
        numCol = len(image[0])

        def dfs(image, i, j):
            if i < 0 or i > numRow - 1 or j < 0 or j > numCol - 1:
                return
            if image[i][j] == color:
                image[i][j] = newColor
                dfs(image, i - 1, j)
                dfs(image, i + 1, j)
                dfs(image, i, j - 1)
                dfs(image, i, j + 1)
        dfs(image, sr, sc)
        return image