from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s or not g:
            return 0
        i, j = 0, 0
        res = 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                res += 1

            s += 1

        return res