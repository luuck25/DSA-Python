class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit = 0
        start = end =0

        for end in range(len(prices)):
            
            if prices[end] > prices[start]:
                profit = prices[end] - prices[start]
                maxprofit = max(maxprofit,profit)
            else: # found lower price
                start = end    
            end += 1    
        
        return maxprofit            






        