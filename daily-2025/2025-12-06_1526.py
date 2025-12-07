"""
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
"""
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odds_until_low = (low // 2)
        odds_until_high = (high + 1) // 2
        return odds_until_high - odds_until_low