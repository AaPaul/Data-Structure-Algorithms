from typing import List


class UnionFind:
    def __init__(self, n) -> None:
        self.n = n
        # self.parent = [i for i in range(n)]
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, idx: int) -> int:
        if self.parent[idx] == idx:
            return idx
        else:
            self.parent[idx] = self.find(self.parent[idx])
            return self.parent[idx]
    
    def connect(self, a: int, b: int) -> None:
        fa = self.find(a)
        fb = self.find(b)

        if self.size[fa] > self.size[fb]:
            self.parent[fa] = fb
            self.size[fa] += self.size[fb]
        else:``
            self.parent[fb] = fa
            self.size[fb] += self.size[fa]

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        ans = []
        uf = UnionFind(n)
        
        for req in requests:
            u, v = uf.find(req[0]), uf.find(req[1])
            if u == v:
                ans.append(True)
            else:
                valid = True
                for res in restrictions:
                    p, q = uf.find(res[0]), uf.find(res[1])
                    if (u == p and v == q) \
                       or (u == q and v == p):
                        valid = False
                        break
                if valid:
                    uf.connect(u, v)
                    ans.append(True)
                else:
                    ans.append(False)
        return ans