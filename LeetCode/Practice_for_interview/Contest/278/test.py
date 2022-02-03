from collections import defaultdict


class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        mp = defaultdict()
        mp['a'] = 1
        for i in range(1, 26):
            mp[chr(ord('a') + i)] = i + 1
        n = len(s)
        dp = 0
        for p in range(k):
            dp += mp[s[p]] * pow(power, p)
        if dp % modulo == hashValue:
            return s[: i+k]
        i = 1
        while i <= n - k:
            if dp % modulo == hashValue:
                print(i)
                return s[i-1: i+k-1]
            dp = (dp - mp[s[i-1]] * pow(power, i-1)) * power + mp[s[i+k-1]] * pow(power, k-1)
            i += 1
            
        return s[i:]

s1 = Solution()
s= "xmmhdakfursinye"

p = 96
m = 45
k = 15
h = 21
print(s1.subStrHash(s, p , m, k, h))