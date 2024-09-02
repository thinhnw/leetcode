class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        bought_price = prices[0]
        profit = 0

        for price in prices[1:]:
            profit = max(profit, price - bought_price)
            bought_price = min(bought_price, price)
        return profit