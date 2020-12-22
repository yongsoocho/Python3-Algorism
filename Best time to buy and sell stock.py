# Say you have an array for which the i-th element is the price of a given stock on day i
# If you were only permitted to complete at most one transcation
# Note that you cannot sell a stock before you buy one

import sys

class Solution:
    def maxProfit(self, prices):
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(price, min_price)

            profit = max(profit, price - min_price)

        return profit

prices = [7, 1, 5, 3, 6, 4]

output = Solution()
print(output.maxProfit(prices))
