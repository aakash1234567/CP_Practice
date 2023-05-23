class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # p = 0
        # n = len(prices)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if prices[j]-prices[i]>p:
        #             p = prices[j]-prices[i]
        # return p
        
        profit = 0
        n = len(prices)
        mn = prices[0]
        for i in range(1, n):
            cost = prices[i]-mn
            profit = max(cost, profit)
            mn = min(mn, prices[i])
        return profit