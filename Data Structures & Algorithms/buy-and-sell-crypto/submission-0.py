class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1         # l- buy, r- sell
        max_profit = 0

        while r <= len(prices) - 1:

            if prices[l] > prices[r]:
                l = r
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
            r += 1
        
        return max_profit
