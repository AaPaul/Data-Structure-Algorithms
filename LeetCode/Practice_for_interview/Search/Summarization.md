
1.如果只是要找到某一个结果是否存在，那么DFS会更高效。因为DFS会首先把一种可能的情况尝试到底，才会回溯去尝试下一种情况，只要找到一种情况，就可以返回了。但是BFS必须所有可能的情况同时尝试，在找到一种满足条件的结果的同时，也尝试了很多不必要的路径


2.如果是要找所有可能结果中最短的，那么BFS回更高效。因为DFS是一种一种的尝试，在把所有可能情况尝试完之前，无法确定哪个是最短，所以DFS必须把所有情况都找一遍，才能确定最终答案（DFS的优化就是剪枝，不剪枝很容易超时）。而BFS从一开始就是尝试所有情况，所以只要找到第一个达到的那个点，那就是最短的路径，可以直接返回了，其他情况都可以省略了，所以这种情况下，BFS更高效。

## BFS
```
q = queue
q.push(initial statu)
while !isEmpty(q){
    cur = q.pop()
    for node in (cur's neighbors){
        if node and not visited(node){
            q.push(node)) # record the number or the statu
        }
    }
}
```
Need to know the level in iteration
```
level = 0
while !isEmpty(q){
    size = q.size()
    while (size--){
        cur = q.pop()
        for node in  (cur's neighbors) {
            if (node satisfies) and not visited(node){
                queue.push(node)
            }
        }
    }
}
```

## DFS
Pay attention to the edge cases.
```
dfs(x, y): # position of the first statu
    if (find the res):
        
        return res

    for (different directions): # iteration with different directions which are not visited yet
        flag[a][b] = 1 # 1 represents that this point is visited
        dfs(a, b)
        flag[a][b] = 0 # backtracking. This operation can let pointer back to the old statu or position while it doesn't affect other situation where other point would visited this statu or the position
    return # no satisfing res
        
```

