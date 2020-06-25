class Solution:
    # h(i) = si* 26^start+L-1-i
    # Rabin-Karp
    def longestDupSubstring(self, S: str) -> str:
        def search(m, MOD):
            h = 0
            for i in range(m):
                h = (h * 26 + nums[i]) % MOD
            s = {h}
            aL = pow(26, m, MOD)
            for pos in range(1, n - m + 1):
                h = (h * 26 - nums[pos - 1] * aL + nums[pos + m - 1]) % MOD
                if h in s:
                    return pos
                s.add(h)
            return -1
        # S is '', return ''
        if not S:
            return ""
        n = len(S)
        nums = [ord(c) - ord('a') for c in S]
        l = 1
        r = n
        pos = 0
        MOD = 2 ** 63 - 1
        while l <= r:
            m = (l + r) // 2
            cur = search(m, MOD)
            if cur != -1:
                l = m + 1
                pos = cur
            else:
                r = m - 1
        return S[pos:pos + l - 1]

s1 = Solution()
test = s1.longestDupSubstring('banana')

# Reference: https://blog.csdn.net/lemonmillie/article/details/90182133
# https://blog.csdn.net/weixin_44110891/article/details/106878093?%3E