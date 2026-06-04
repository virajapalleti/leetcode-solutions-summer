class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totprofit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                totprofit += prices[i] - prices[i - 1]
                
        return totprofit
                        

                    
            