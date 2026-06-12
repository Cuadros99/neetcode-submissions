class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        profit = 0
        top_p = 0
        start_p = prices[0]

        for i in range(len(prices)):
            if prices[i] >= top_p:
                top_p = prices[i]
                profit = top_p - start_p
            
            if prices[i] < start_p:
                max_profit = max(profit, max_profit)
                profit = 0
                start_p = prices[i]
                top_p = prices[i]

        max_profit = max(profit, max_profit)

        return max_profit
            