class Solution:
    # This is faster than the mehod using collections.Counter()
    def longestPalindrome(self, s: str) -> int:
        cnt = [0] * 256
        for i in s:
            cnt[ord(i)] += 1
        res = 0
        for c in cnt:
            res += c // 2 * 2
        return res + 1 if res < len(s) else res