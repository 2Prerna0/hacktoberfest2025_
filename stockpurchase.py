class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0
        total = 0
        for i in range(len(prices)):
            total  = prices[i] - mini
            profit = max(profit,total)
            mini = min(mini,prices[i])
        return profit
