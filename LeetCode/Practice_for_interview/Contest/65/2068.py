from typing import DefaultDict


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        w1 = DefaultDict(int)
        for ch in word1:
            w1[ch] += 1
        for ch in word2:
            w1[ch] -= 1
        return all(abs(x) <= 3 for x in w1.values())

s1 = Solution()
word1 = "aaaa"
word2 = "bccb"
print(s1.checkAlmostEquivalent(word1, word2))