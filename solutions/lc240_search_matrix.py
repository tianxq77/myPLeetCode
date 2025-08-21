from typing import List

from sqlalchemy.sql.operators import truediv


class Solution:

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        #标准题解:每一步都能排除一行或一列，确保时间复杂度为 O(m + n)
        # 从右上角（0，n-1）搜索,
        #if  target < matrix[i][j]:
        #       j=j-1
        #elseif target >matrix[i][j]:
        #         i=i+1

        m,n=len(matrix),len(matrix[0])
        row=0
        col=n-1
        while row<m and col>=0:
            if target<matrix[row][col]:
                col-=1
            elif target>matrix[row][col]:
                row+=1
            else:
                return True

        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#我的答案尝试通过以下步骤搜索：
#
# 1.沿对角线移动：从 (0, 0)开始，找到第一个满足 matrix[end][end] > target的位置 end。
#
# 2.划分子矩阵：假设 target可能存在于以下两个区域：
# 区域1：第 0到 end-1行，第 end到 n-1列（右上部分）。
#
# 区域2：第 end到 m-1行，第 0到 end-1列（左下部分）。
#
# 3.
# 搜索子矩阵：在这两个区域中遍历搜索 target

        # 根据对角线，找到一个需要遍历的子矩阵
        m, n = len(matrix), len(matrix[0])
        # 处理单行或单列的情况
        if m == 1 or n == 1:
            for row in matrix:
                for num in row:
                    if num == target:
                        return True
            return False
        minlen=min(m,n)
        end=0
        while end<minlen-1 and matrix[end][end]<target :
            if matrix[end][end]==target :
                return True
            else:
                end=end+1
        if matrix[end-1][end-1]<target<matrix[end][end] :
            for i in range (end):
                for j in range(end,n):
                    if matrix[i][j]==target:
                        return True
            for i in range(end,m):
                for j in range(end):
                    if matrix[i][j]==target:
                        return True
        else:
            for i in range(m):
                for j in range(end,n):
                    if matrix[i][j]==target:
                        return True
        return False

if __name__=="__main__":
    matrix =[[4,6,9,10,15],[9,12,13,15,16]]
    target = 14
    s=Solution()
    print(s.searchMatrix2(matrix,target))






