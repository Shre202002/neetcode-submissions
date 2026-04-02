class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = prices[0]
        diff = 0
        for i in range(1,len(prices)):
            if minn > prices[i]:
                minn = prices[i]
            if diff < prices[i] - minn:
                diff =  prices[i] - minn
        return diff
