class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        max_val = 0
        prev_profit = 0
        for i in range(len(prices)):
            if prices[i] <= min_val:
                prev_profit = max(prev_profit, max_val - min_val)
                min_val = prices[i]
                max_val = 0
            else:
                max_val = max(max_val, prices[i])  
        return max(prev_profit, max_val - min_val)

        