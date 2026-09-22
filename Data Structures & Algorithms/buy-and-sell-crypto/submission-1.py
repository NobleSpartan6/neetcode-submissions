class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # entry 
        # exit 
        # maximize the profit = (exit - entry)
        l, r = 0, 1 # left is buying right is selling
        maxProfit = 0

        while r < len(prices):
            # is it profitable? 
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit