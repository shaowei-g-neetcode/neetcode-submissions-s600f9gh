class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell= 0, 1
        res = 0

        while sell < len(prices):
            # buy price < sell price = has profit
            if prices[buy] < prices[sell]:
                res = max(res, prices[sell] - prices[buy])
            # buy price >= sell price = sell price can make more profit
            else:
                buy = sell
            sell += 1

        return res
                


  