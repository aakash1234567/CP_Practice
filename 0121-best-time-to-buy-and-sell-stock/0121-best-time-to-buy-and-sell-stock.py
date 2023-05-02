class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # p = 0
        # n = len(prices)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if prices[j]-prices[i]>p:
        #             p = prices[j]-prices[i]
        # return p
        
        p = 0
        n = len(prices)
        mn = prices[0]
        for i in range(1,n):
            c = prices[i]-mn
            p = max(c, p)
            mn = min(mn, prices[i])
        return p