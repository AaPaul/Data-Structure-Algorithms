class Solution:
    # manacher
    def countSubstrings2(self, s: str) -> int:
        n = len(s)
        t = '$#'
        for ch in s:
            t += ch
            t += '#'
        n = len(t)
        t += '~'
        f = [0] * n 
        rMax = iMax = cnt = 0
        for i in range(1, n):
            f[i] = min(f[], rMax - i + 1) if i <= rMax else 1
            while s[i - rMax] == s[i + rMax]: rMax += 1
             



    def countSubstrings2(self, s: str) -> int:
        res = 0
        n = len(s)
        def expandString(s1, start, end):
            nonlocal res
            while start >= 0 and end < n and s1[start] == s1[end]:
                start -= 1
                end += 1
                res += 1
        
        for i in range(n):
            expandString(s, i, i)
            expandString(s, i, i+1)
        return res
                
        
    