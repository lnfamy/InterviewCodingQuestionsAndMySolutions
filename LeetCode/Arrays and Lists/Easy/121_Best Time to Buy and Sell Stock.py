"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""


class Solution:
    # basically find the min and max, as long as max is ahead of min
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > profit:
                profit = prices[i] - min_price

        return profit
