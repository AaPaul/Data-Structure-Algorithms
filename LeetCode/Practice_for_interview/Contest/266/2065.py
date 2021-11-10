class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        paths = collections.defaultdict(list)
        for x, y, z in edges:
            paths[x].append((y, z))
            paths[y].append((x, z))
        
        visited = {0}

        def dfs(node, time, val):
            if node == 0:
                nonlocal maxVal
                maxVal = max(maxVal, val)
            for n, tm in paths[node]:            
                if time - tm >= 0:
                    if n not in visited:
                        visited.add(n)
                        dfs(n, time - tm, val+values[n])
                        visited.discard(n)
                    else:
                        dfs(n, time - tm, val)


        maxVal = 0
        dfs(0, maxTime, values[0])
        return maxVal