from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)

        # Method 1 Brute force
        def calMax1(prices, start):
            # the reason why define this variable is that we need to state it so that
            # we can prevent reference error when we process the tail of the list.
            maxtotal = 0
            for i in range(start, l, 1):
                maxprofit = 0
                for j in range(i + 1, l, 1):
                    if prices[j] > prices[i]:
                        profit = prices[j] - prices[i] + calMax1(prices, j + 1)
                        if profit > maxprofit:
                            maxprofit = profit
                if maxprofit > maxtotal:
                    maxtotal = maxprofit

            return maxtotal

        # Method 2
        # The key point of this method is to calculate the difference between
        # each pair of the consecutive peak and valley
        def calMax2(prices, start):
            maxtotal = 0
            count = 0
            for i in range(l):
                if (i+1 < l and prices[i] < prices[i + 1]):
                    count += 1
                else:
                    # if prices[i] >= prices[i+1]:
                    maxtotal += prices[i] - prices[i - count]
                    count = 0 # To count next difference between next peak and valley
                    # if we don't initial count to 0, we will have an error
                    # that we will between next value and this value which should not be considered. like (3, 2)
            return maxtotal

        # m1 = calMax1(prices, 0)
        # print(m1)
        m2 = calMax2(prices, 0)
        print(m2)


s1 = Solution()
# s1.maxProfit([1, 2, 3, 4, 5])
# s1.maxProfit([7,1,5,3,6,4])
# s1.maxProfit([5, 4, 3, 2, 1])
s1.maxProfit([0, 1, 0, 0])

# Reference
# https://medium.com/@punitkmr/best-time-to-buy-and-sell-stock-ii-7826845144eb