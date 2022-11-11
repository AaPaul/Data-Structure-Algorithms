# https://leetcode.com/discuss/interview-question/1845461/question
# https://www.1point3acres.com/bbs/thread-796464-1-1.html
# https://leetcode.com/discuss/interview-question/1954161/microsoft-online-assessment


# Preprocessing. get the visible area of all stranger
# bfs or dfs. mark the cell if you can pass withou being caught
from collections import deque


def fun(arr):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    m, n = len(arr[0]), len(arr)
    for i in range(n):
        arr[i] = list(arr[i])
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'A':
                start = (i, j)
            # right facing stranger
            elif arr[i][j] == '>':
                c = j + 1
                while c < m and (arr[i][c] == 'A' or arr[i][c] == '*' or arr[i][c] == '.'):
                    arr[i][c] = '*'
                    c += 1

            # left facing stranger
            elif arr[i][j] == '<':
                c = j - 1
                while c >= 0 and (arr[i][c] == 'A' or arr[i][c] == '*' or arr[i][c] == '.'):
                    arr[i][c] = '*'
                    c -= 1
                
            # up facing stranger
            elif arr[i][j] == '^':
                r = i - 1
                while r >= 0 and (arr[r][j] == 'A' or arr[r][j] == '*' or arr[r][j] == '.'):
                    arr[r][j] = '*'
                    r -= 1

            # down facing stranger
            elif arr[i][j] == 'v':
                r = i + 1
                while r < n and (arr[r][j] == 'A' or arr[r][j] == '*' or arr[r][j] == '.'):
                # while r < n and arr[r][j] != 'X': # this method is wrong as we may change other guard like '<' to '*'
                    arr[r][j] = '*'
                    r += 1
    
    # def dfs(loc):
    #     x, y = loc
    #     arr[x][y] = '#'
    #     if x == n - 1 and y == m - 1:
    #         return
    #     for xi, yi in directions:
    #         if 0 <= x + xi < n and 0 <= y + yi < m and arr[x + xi][y + yi] == '.':
    #             dfs((x + xi, y + yi))

    # dfs(start)

    # bfs
    q = deque([start])
    while q:
        x, y = q.popleft()
        for xi, yi in directions:
            if 0 <= x + xi < n and 0 <= y + yi < m and arr[x + xi][y + yi] == '.':
                arr[x + xi][y + yi] = '#'
                q.append((x + xi, y + yi))

        if arr[n-1][m-1] == '#':
            return True


    return arr[n-1][m-1] == '#'





arr = ['x.....>', '..v..x.','.>..x..', 'A......']
print(fun(arr))
arr = ['...xv', 'AX..^', '.XX..']
print(fun(arr))

arr = ["..>...<.v.",
                ".>..<.....",
                "....>.....",
                ".......A..",
                "....v..<^.",
                ".>..^.....",
                ".........."]
print(fun(arr))