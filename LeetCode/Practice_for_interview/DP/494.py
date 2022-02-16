from typing import List

"""
Based on the solution of 0-1 backpack problem. 
P represents '+', N represents '-'. Therefore:
we want to find the number of P so that:
sum(P) - sum(N) = target
sum(P) + sum(P) + sum(N) - sum(N) = target + sum(P) + sum(N)
2 * sum(P) = target + sum(nums)

So, we want to find P so that
(target + sum(nums)) / 2 = sum(P)
 
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        _sum = sum(nums)
        if _sum < target or (_sum + target) % 2 == 1:
            return 0
        w = (_sum + target) // 2
        dp = [0] * (abs(w) + 1)
        
        dp[0] = 1
        for i in nums:
            j = w
            while j >= i:
                dp[j] = dp[j] + dp[j - i]
                j -= 1
        return dp[w]
        