class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        minp=10000000
        for i in range(0,len(prices)):
            minp=min(minp,prices[i])
            maxp=max(maxp,prices[i]-minp)
        return maxp