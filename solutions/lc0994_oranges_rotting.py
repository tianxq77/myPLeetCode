from collections import deque
from typing import List


class Solution:


    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # 初始化：统计新鲜橘子，腐烂橘子入队
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))  # 腐烂橘子入队

        minutes = 0

        # 多源BFS，层级腐烂扩散
        while queue and fresh > 0:
            # 处理当前分钟的所有腐烂橘子
            for _ in range(len(queue)):
                x, y = queue.popleft()  # 左端弹出，处理该橘子，将其周围 4 个方向上相邻 的新鲜橘子进行腐烂
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        queue.append((nx, ny))
            minutes += 1

        return minutes if fresh == 0 else -1


if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(Solution().orangesRotting(grid))