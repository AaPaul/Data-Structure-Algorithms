from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_sorted = sorted(stones, reverse=True)
        # s_copy = stones_sorted.copy()
        # i = 0
        while len(stones_sorted) > 1:
            diff = stones_sorted[0] - stones_sorted[1]
            stones_sorted.pop(0) # ATTENTION!
            stones_sorted.pop(0)

            if diff:
                stones_sorted.append(diff)
                stones_sorted = sorted(stones_sorted, reverse=True)
        if stones_sorted:
            return stones_sorted[0]
        else:
            return 0


s1 = Solution()
ans = s1.lastStoneWeight([2,7,4,1,8,1])
print(ans)

"""
Note: Pay attention to the function pop(). When you call it once, the list will
del the element on the specific position and the remaining elements in the list will be shifted forward
"""