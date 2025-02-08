class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        maxp=0
        for i in range(1,len(prices)):
            cost=prices[i]-mini
            maxp=max(maxp,cost)
            mini=min(mini,prices[i])
        return maxp