class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        n = len(time)
        # 余数数组
        arr = [0 for _ in range(60)]
        res = 0
        for t in time:
            # i 表示余数
            
            i = 60 - t % 60
            res += arr[i % 60]
            arr[t % 60] += 1
        return res