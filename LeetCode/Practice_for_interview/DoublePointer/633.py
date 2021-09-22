# 633. Sum of Square Numbers (Easy)
from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(sqrt(c))
        while l <= r:
            _sum = l**2 + r**2
            if _sum == c:
                return True
            elif _sum < c:
                l += 1
            else:
                r -= 1 
        return False

t1 = Solution()
print(t1.judgeSquareSum(5))