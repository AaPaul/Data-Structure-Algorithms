class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        low = 1
        high = max(quantities)
        
        while low <= high:
            cnt = 0
            mid = (low + high) // 2
            for i in quantities:
                cnt += i//mid
                if i % mid:
                    cnt += 1
            if cnt <= n:
                high = mid - 1
            else:
                low = mid + 1

        return low