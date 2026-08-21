class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        for i in range(len(prices)):
            current_buy = prices[i]
            for j in range(len(prices))[i+1:]:
                current_sell = prices[j]
                current_profit = current_sell - current_buy
                if current_profit > best_profit:
                    best_profit = current_profit
        return best_profit