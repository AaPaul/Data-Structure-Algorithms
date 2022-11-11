from collections import defaultdict, deque
from typing import List


class Solution:
    # bfs Khan topological sort
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * n
        for i in range(len(prerequisites)):
            pre, nxt = prerequisites[i]
            # if pre not in graph:
            #     graph[pre] = [nxt]
            # else:
            graph[pre].append(nxt)
            indegree[nxt] += 1
        print(graph)
        # print(indegree)
        queue = deque()
        for i, de in enumerate(indegree):
            if de == 0:
                queue.append(i)
        print(queue)
        count = 0
        while queue:
            count += 1
            curr = queue.popleft()
            # if graph[curr]:
            # if curr not in graph:
            #     continue
            # temp = graph.get(curr, -1) # if not in graph hashmap, we can skip it and also we do count++, the return val should be count == n.
            for i in graph[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        print(count)
        return count == len(graph)

n = 8
pre = [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]
s1 = Solution()
print(s1.canFinish(n, pre))