class Solution:
    def palin(self, n: str) -> bool:
        i, j = 0, len(n) - 1
        while i < j:
            if n[i] != n[j]:
                return False
            i += 1
            j -= 1
        return True
    def transferation(self, k: int, n: int) -> str:
        res = []
        while n:
            t = n % k
            res.insert(0, str(t))
            n //= k
        n_str = "".join(res)
        # print(n_str)
        return n_str
        
    def kMirror(self, k: int, n: int) -> int:
        ans = 0
        # candidate = []
        cnt = 0
        i = 1
        while cnt < n:
            t = self.transferation(k, i)
            if self.palin(t) and self.palin(str(i)):
                print(t)
                ans += i
                cnt += 1
            i += 1
        return ans

s1 = Solution()
print(s1.kMirror(7, 17))