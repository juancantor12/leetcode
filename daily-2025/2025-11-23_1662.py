"""
Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.
"""
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        neg_inf = -10**18
        dp = [0, neg_inf, neg_inf]
        for x in nums:
            add = x % 3
            new = dp.copy()
            for r in range(3):
                nr = (r + add) % 3
                candidate = dp[r] + x
                if candidate > new[nr]:
                    new[nr] = candidate
            dp = new
        return max(0, dp[0])  