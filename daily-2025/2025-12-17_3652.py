"""
You are given two integer arrays prices and strategy, where:
prices[i] is the price of a given stock on the ith day.
strategy[i] represents a trading action on the ith day, where:
-1 indicates buying one unit of the stock.
0 indicates holding the stock.
1 indicates selling one unit of the stock.
You are also given an even integer k, and may perform at most one modification to strategy. A modification consists of:
Selecting exactly k consecutive elements in strategy.
Set the first k / 2 elements to 0 (hold).
Set the last k / 2 elements to 1 (sell).
The profit is defined as the sum of strategy[i] * prices[i] across all days.
Return the maximum possible profit you can achieve.
Note: There are no constraints on budget or stock ownership, so all buy and sell operations are feasible regardless of past actions.
"""
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        profit_at = [0]*(len(prices)+1)
        profit_selling = [0]*(len(prices)+1)
        max_profit = 0
        for i in range(1, len(prices)+1):
            profit_at[i] = (prices[i-1] * strategy[i-1]) + profit_at[i-1]
            profit_selling[i] = prices[i-1] + profit_selling[i-1]
        max_profit = profit_at[-1]
        for i in range(0, len(prices)-k+1):
            window_contrib = profit_at[i+k] - profit_at[i]
            sell_earn = profit_selling[i+k] - profit_selling[i+(k//2)]
            new_profit = profit_at[-1] - window_contrib + sell_earn
            max_profit = max(max_profit, new_profit)
        return max(max_profit, profit_at[-1])