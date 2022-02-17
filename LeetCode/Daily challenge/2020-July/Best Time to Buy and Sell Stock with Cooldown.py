class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        if l <= 1:
            return 0
        diff = [prices[i+1] - prices[i] for i in range(l-1)]
        stock, profit = [0]*(l+1), [0]*(l+1)
        for i in range(l-1):
            stock[i] = diff[i]+max(stock[i-1], profit[i-3])
            profit[i] = max(stock[i], profit[i-1])
        return profit[-3]

s1 = Solution()
print(s1.maxProfit([1,2,3,1,4]))

# reference:https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/761720/Python-dp-O(n)-solution-using-differences-explained