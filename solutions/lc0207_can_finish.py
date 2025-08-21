import collections
from typing import List


class Solution:
    # 创建一个邻接表,表示有向图
    # 环检测算法：
    # 创建入度表，以及入度=0的顶点队列（先进先出）
    # 删除入度=0的顶点，并更新其邻接顶点的入度-1，如果入度=0，则加入队列
    # 循环结束后，如果所有顶点入度=0，则不存在环
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for i in range(numCourses)]
        in_degree=[0]*numCourses #入度表示任务依赖数
        for course,pre in prerequisites:
            adj[pre].append(course)
            in_degree[course]+=1

        count_num=0
        queue= collections.deque()
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)

        while queue:
            course=queue.popleft()
            count_num+=1
            for next_course in adj[course]:
                in_degree[next_course]-=1
                if in_degree[next_course]==0:
                    queue.append(next_course)
        return count_num==numCourses

if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1,0]]
    print(Solution().canFinish(numCourses, prerequisites))