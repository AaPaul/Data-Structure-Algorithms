from collections import Counter
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        idx = 0
        ans = []
        for i, j in enumerate(cnt.keys()):
            if i == 0:
                ans.append([j])
            else:
                if j - ans[idx][-1] == 1:
                    ans[idx].append(j)
                else:
                    idx += 1
                    ans.append([j])
        res = 0
        for i in ans:
            n = len(i)
            res = max(res, n)
        return res

s = Solution()
nums = [100,4, 200, 1, 3, 2]
print(s.longestConsecutive(nums))