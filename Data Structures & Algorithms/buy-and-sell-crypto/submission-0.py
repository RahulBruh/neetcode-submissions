class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        profit = 0

        while sell < len(prices):
            if prices[sell] - prices[buy] > 0:
                if prices[sell] - prices[buy] > profit:
                    profit = prices[sell] - prices[buy]
                sell += 1
            else:
                buy = sell
                sell += 1

        return profit