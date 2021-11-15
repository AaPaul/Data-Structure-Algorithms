class Solution:

    def countBinarySubstrings(self, s:str) -> int:
        seq0, seq1 = 0, 1
        n = len(s)
        res = 0
        for i in range(1, n):
            if s[i] == s[i-1]:
                seq1 += 1
            else:
                res += min(seq0, seq1)
                seq0 = seq1
                seq1 = 1
        res += min(seq0, seq1)
        return res

    def countBinarySubstrings2(self, s:str) -> int:
        res = 0
        n = len(s)
        prev = 0
        i = 0
        while i < n:
            ch = s[i]
            count = 0
            while i < n and ch == s[i]:
                count += 1
                i += 1
            res += min(prev, count)
            prev = count
        return res
    

s1 = Solution()
print(s1.countBinarySubstrings("00110011"))