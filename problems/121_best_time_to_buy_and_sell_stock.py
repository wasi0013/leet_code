class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float("inf")
        for p in prices:
            min_price = min(p, min_price)
            profit = p - min_price
            max_profit = max(max_profit, profit)
        return max_profit
    
