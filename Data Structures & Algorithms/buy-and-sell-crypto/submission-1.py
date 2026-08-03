class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep track of min and max?
        # the min needs to be before the max 
        # sliding window
        # - compare 10, 1 bad time to buy and sell
        # - compare 1, 5
        minNum = float('inf')
        profit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                minNum = min(prices[i], minNum)
                profit = max(prices[i+1] - minNum, profit)
            else:
                continue
        if minNum == float('inf'):
            return 0
        return profit
            
            
        
