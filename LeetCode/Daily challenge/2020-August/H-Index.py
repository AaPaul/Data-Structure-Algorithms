# This problem is another version of hIndex (In June).
# H-Index is just a kind of a index number essentially. Based on that, we can use the index in array
# to represent H-Index (sort_ci[i-1], `i-1` is an index number).
# h of N papers at least have h citations, while other N-h papers are all cited less than h times.


from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        sort_ci = sorted(citations, reverse=True)
        res = 0
        if sort_ci[-1] >= len(sort_ci):
            return len(sort_ci)
        for i in range(1, len(sort_ci)+1):
            if sort_ci[i-1] < i:
                res = i - 1
                break
        return res