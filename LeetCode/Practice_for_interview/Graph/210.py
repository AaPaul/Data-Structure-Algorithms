# DFS three color
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(idx):
            visited[idx] = 1
            nonlocal valid
            for child in graph[idx]:
                if visited[child] == 0:
                    dfs(child)
                elif visited[child] == 1:
                    valid = False
                    return
            visited[idx] = 2
            ans.append(idx)
        
        outdegree = [0] * numCourses
        graph = defaultdict(list)
        for i in range(len(prerequisites)):
            curr, prev = prerequisites[i][0], prerequisites[i][1]
            graph[prev].append(curr)
            outdegree[prev] += 1
        # 0: not visited, 1: in Processing, 2: visited
        visited = [0] * numCourses
        valid = True
        ans = []
        for i in range(numCourses):
            if visited[i] == 0:
                dfs(i)
        ans = ans[::-1]
        return ans if valid else []