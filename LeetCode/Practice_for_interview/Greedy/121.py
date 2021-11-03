class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        sofarMin = prices[0]
        n = len(prices)
        res = 0
        
        for i in range(n):
            if prices[i] < sofarMin:
                sofarMin = prices[i]
            else:
                res = max(res, prices[i] - sofarMin)
        
        return res