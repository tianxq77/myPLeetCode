# LeetCode 刷题项目

## 图论题目求解方法指南

图论是算法题中的常见题型，掌握系统性的解题方法非常重要。以下是图论题目的完整求解思路和技巧：

一、图论基础准备

1. 图的表示方式：
   • 邻接矩阵：适合稠密图（空间O(V²)）

   • 邻接表：适合稀疏图（空间O(V+E)）

   • 边列表：适合需要处理所有边的场景

2. 必备算法模板：
# 邻接表表示法（常用）
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

# 邻接矩阵表示法
adj_matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]


二、解题四步法

1. 问题转化：
   • 明确顶点和边的定义（如：社交网络中人是顶点，关系是边）

   • 判断图的性质：有向/无向、加权/无权、是否有环

2. 算法选择：
   问题类型 典型算法 时间复杂度
连通性问题 DFS/BFS/并查集 O(V+E)
最短路径 Dijkstra/Bellman-Ford/Floyd O(ElogV)
最小生成树 Prim/Kruskal O(ElogV)
拓扑排序 Kahn's算法/DFS O(V+E)
欧拉路径 Hierholzer算法 O(E)
强连通分量 Kosaraju/Tarjan O(V+E)

3. 边界处理：
   • 空图处理

   • 孤立顶点处理

   • 自环和重边处理

   • 大规模图的优化（如使用堆优化Dijkstra）

4. 编码实现：
   • 使用合适的图表示法

   • 注意递归深度（DFS可能栈溢出）

   • 必要时进行剪枝优化

三、经典题型实战

1. 连通性问题（LeetCode 323）：
def countComponents(n, edges):
    parent = list(range(n))
    
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    
    for u, v in edges:
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            parent[root_v] = root_u
            n -= 1
    return n


2. 最短路径（LeetCode 743）：
def networkDelayTime(times, n, k):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    
    heap = [(0, k)]
    dist = {node: float('inf') for node in range(1, n+1)}
    dist[k] = 0
    
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))
    
    max_dist = max(dist.values())
    return max_dist if max_dist < float('inf') else -1


3. 拓扑排序（LeetCode 207）：
def canFinish(numCourses, prerequisites):
    indegree = [0] * numCourses
    adj = [[] for _ in range(numCourses)]
    
    for dest, src in prerequisites:
        adj[src].append(dest)
        indegree[dest] += 1
    
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    visited = 0
    
    while queue:
        node = queue.popleft()
        visited += 1
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return visited == numCourses


四、进阶技巧

1. 双向BFS优化：
   • 适用于起点和终点都已知的最短路径问题

   • 时间复杂度从O(b^d)降到O(b^(d/2))，b为分支因子，d为深度

2. A*算法：
   • 带启发式函数的Dijkstra

   • 需要设计合理的启发函数（如曼哈顿距离）

3. 分层图技巧：
   • 处理有特殊条件的最短路径（如可消除k个障碍）

   • 通过状态扩展将问题转化为分层图

4. 缩点算法：
   • 将有向图的强连通分量缩成超级节点

   • 适用于需要处理环的场景

五、调试技巧

1. 可视化小规模图：
   • 手工绘制图的邻接关系

   • 验证算法每一步的执行结果

2. 特殊测试用例：
   # 自环测试
   test_case = [(0,0), (1,1)], n=2
   # 完全图测试
   test_case = [(i,j) for i in range(3) for j in range(3) if i!=j], n=3
   

3. 性能分析：
   • 使用Python的timeit模块测试运行时间

   • 对于大规模数据，检查是否超出时间限制

六、推荐练习题单

1. 基础题：
   • 133.克隆图

   • 200.岛屿数量

   • 207.课程表

2. 中等题：
   • 399.除法求值

   • 547.省份数量

   • 787.K站中转内最便宜的航班

3. 难题：
   • 685.冗余连接II

   • 711.不同岛屿的数量II

   • 749.隔离病毒

掌握这套方法论后，遇到图论题目时可以：
1. 快速识别问题类型
2. 选择合适算法模板
3. 处理边界条件
4. 高效实现代码
