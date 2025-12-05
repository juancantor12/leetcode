"""
You are given an integer array nums of length n.
A partition is defined as an index i where 0 <= i < n - 1, splitting the array into two non-empty subarrays such that:
Left subarray contains indices [0, i].
Right subarray contains indices [i + 1, n - 1].
Return the number of partitions where the difference between the sum of the left and right subarrays is even.
solution details:
https://leetcode.com/problems/count-partitions-with-even-sum-difference/solutions/7392459/solution-by-la_castille-0zwu/?envType=daily-question&envId=2025-12-05
"""
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return (len(nums) - 1) * (~sum(nums) & 1)