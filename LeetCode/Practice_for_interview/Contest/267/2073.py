class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for i in range(len(tickets)):
            if i <= k:
                ans += min(tickets[i], tickets[k])
            else:
                temp = tickets[i] if tickets[i] < tickets[k] else tickets[k] -1 
                ans += temp
        return ans