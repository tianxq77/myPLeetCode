from typing import List


class Solution:
    # 辅助函数仅被单个函数使用,使用嵌套函数,比如在主函数内部定义辅助的dfs函数，
    # 优点在于内层函数可以访问外层函数的变量，避免重复计算或额外参数

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_island = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            # 先检查边界条件
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '1':
                return
            # 标记为已访问
            grid[i][j] = '0'
            # 四个方向递归搜索
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    num_island += 1
                    dfs(i, j)

        return num_island


#  遍历整个网格 grid：
# 遇到一个 '1' 时，就表示发现了一个新岛屿，nums_island 增加 1。
# 同时通过深度优先搜索淹没整个岛屿（即将与当前 '1' 相连的所有 '1' 变为 '0'），以免重复计数。
# 调用顺序依次处理：
#先执行 dfs(i+1,j)并完全深入这个方向
# 直到该路径无法继续（遇到边界或水域）
# 然后回溯执行 dfs(i-1,j)
# 重复上述深入过程
# DFS 的作用：
# 从当前点开始，递归地访问它的上下左右相邻的点，检查是否是 '1'。
# 如果是 '1'，则继续递归，直到所有相连的 '1' 都被处理成 '0'。
# def numIslands(self, grid: List[List[str]]) -> int:
#     num_island = 0
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j] == '1':
#                 num_island += 1
#                 self.dfs(grid, i, j)
#
#
#     return num_island;
#
# def dfs(self, grid, i, j):
#     if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
#         return
#     grid[i][j] = '0'
#     self.dfs(grid, i + 1, j)
#     self.dfs(grid, i - 1, j)
#     self.dfs(grid, i, j + 1)
#     self.dfs(grid, i, j - 1)

if __name__ == '__main__':
    s = Solution()
    print(s.numIslands(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
