import collections
from typing import List

from self import self


def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    ans = []
    # 1、构图
    edges = collections.defaultdict(list)
    indgree = [0] * numCourses
    for pre in prerequisites:
        edges[pre[1]].append(pre[0])
        indgree[pre[0]] += 1
    # 2、入度为0节点入队列
    q = collections.deque(u for u in range(numCourses) if indgree[u] == 0)
    visited = 0
    while q:
        visited += 1
        cur = q.popleft()
        ans.append(cur)
        # 3、相邻节点入度减去1
        for nex in edges[cur]:
            indgree[nex] -= 1
            # 4、入度为0节点入队列
            if indgree[nex] == 0:
                q.append(nex)
    return ans if visited == numCourses else []


numCourses = 2
prerequisites = [[1, 0], [0, 1]]
print(findOrder(self, numCourses, prerequisites))
