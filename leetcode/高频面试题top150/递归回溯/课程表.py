import collections
from typing import List

from self import self


def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    edges = collections.defaultdict(list)
    indegree = [0] * numCourses
    for pre in prerequisites:
        edges[pre[0]].append(pre[1])
        indegree[pre[1]] += 1

    # 把入度为0的节点全部加入队列
    q = collections.deque(u for u in range(numCourses) if indegree[u] == 0)
    visited = 0
    while q:
        visited += 1
        cur = q.popleft()
        for e in edges[cur]:
            # 相邻节点的入度全部减1
            indegree[e] -= 1
            # 如果相邻节点入度为0，就加入队列
            if indegree[e] == 0:
                q.append(e)
    return visited == numCourses


numCourses = 2
prerequisites = [[0, 1]]
print(canFinish(self, numCourses, prerequisites))
