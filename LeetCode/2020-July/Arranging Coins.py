class Solution:
    def arrangeCoins(self, n: int) -> int:
        if not n:
            return n
        count = 0
        flag = 1
        while (flag <= n):
            count += 1
            n -= flag
            flag += 1
        return count
