class Solution:
    # double pointers
    def isSubsequence(self, s: str, t: str) -> bool:
        i=j=0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        if i == len(s):
            return True
        return False

    # binary seach
    def isSubsequence2(self, s: str, t: str) -> bool:
        hashSet = {}
        for i, c in enumerate(t):
            if c not in hashSet.keys():
                hashSet[c] = [i]
            else:
                hashSet[c].append(i)
        
        lastidx = -1    
        for c in s:
            if c not in hashSet.keys():
                return False
            
            cList = hashSet[c]
            left = 0
            right = len(cList)
            while left < right:
                mid = left + (right - left) // 2
                if cList[mid] > lastidx:
                    right = mid
                else:
                    left = mid + 1
            if left == len(cList):
                return False
            lastidx = cList[left]
        return True

    # dynamic programming
    def isSubsequence3(self, s: str, t: str) -> bool:
        m = len(t)
        n = len(s)
        dp = [[0] * 26 for _ in range(m)]
        dp.append([m] * 26)

        for i in range(m-1, -1, -1):
            for j in range(26):
                if j == (ord(t[i]) - ord('a')):
                    dp[i][j] = i
                else:
                    dp[i][j] = dp[i+1][j]
        
        add = 0
        for i in range(n):
            if dp[add][ord(s[i]) - ord('a')] == m:
                return False
            add = dp[add][ord(s[i]) - ord('a')] + 1
        return True
        